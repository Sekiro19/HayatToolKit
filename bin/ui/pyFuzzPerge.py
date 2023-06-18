from pathlib import Path
from core import *
from .pages.ui_pyFuzzPerge import Ui_Form_FuzzyPerge
from ..modules import OutletCleaner, Worker
from .widgets.pyFileButton import FileBtn
from functools import partial
import traceback

class FormFuzzPurge(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Form_FuzzyPerge()
        self.ui.setupUi(self)
        # thread pool
        self.threadPool = QThreadPool.globalInstance()
        self.threadPool.setMaxThreadCount(1)
        self.mutex = QMutex()
        # defaults
        self.format = None
        # ui
        self.ui.btnLoadFiles.clicked.connect(self.loadFiles)
        self.ui.btnStart.clicked.connect(self.start)
        self.ui.btnStart.setEnabled(False)
    
    def loadFiles(self):
        if self.ui.cboxFileType.currentText() == 'Supervisor Outlet':
            self.format = internalPaths['CityData']
            filesList = openDialogue(mode=QFileDialog.ExistingFiles, nameFilter="Excel files (*.xlsx)")
            
        if filesList:
            self.ui.progressBar.setValue(0)
            self.processFiles(filesList)
    
    def processFiles(self, filePaths: list):
        numFiles = len(filePaths)
        self.ui.progressBar.setMaximum(numFiles)
        files = [btn.data.fileLoc for btn in self.getButtons()]
        for i in range(numFiles):
            if filePaths[i] in files:
                showMsg('File already selected', 'notice')
            else:
                self.ui.terminal.setText(f'> Loading Files...')
                worker = Worker(OutletCleaner, 0, filePaths[i], self.format)
                worker.signals.results.connect(self.setButton)
                worker.signals.finished.connect(partial(self.ui.btnStart.setEnabled, True))
                self.threadPool.start(worker)
    
    def checkCols(self, cols, dfCols):
        for col in cols:
            if col not in dfCols:
                return f"column {col} not found!"
        return True
    
    def setButton(self, data):
        fileName = Path(data.fileLoc).name
        allColsFound = self.checkCols(['Outlet Type', 'City', 'Town', 'jour de visite'], data.dfOutlet.columns)
        if allColsFound == True:
            fileBtn = FileBtn(text=fileName, data=data)
            try:
                self.mutex.lock()
                self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)
                self.ui.filesBtnArea.layout().insertWidget(0, fileBtn)
                if self.threadPool.activeThreadCount() == 0:
                    self.ui.terminal.setText('> DONE!')
            finally:
                self.mutex.unlock()
        else:
            self.ui.terminal.setText(f'{self.ui.terminal.text()}\n> file "{fileName}": {allColsFound}')
    
    def getButtons(self):
        btns = list()
        for i in range(self.ui.filesBtnArea.layout().count()):
            item = self.ui.filesBtnArea.layout().itemAt(i)
            if item and item.widget():
                btn = item.widget()
                btns.append(btn)
        return btns
        
    def start(self):
        btns = self.getButtons()
        if (self.threadPool.activeThreadCount() == 0) and (len(btns) > 0):
            if self.ui.chBoxInplace.isChecked():
                outputFolder = None
            else:
                filesList = openDialogue(mode=QFileDialog.Directory)
                if filesList:
                    outputFolder = filesList[0]
                    self.ui.progressBar.setMaximum(len(btns))
                    self.ui.progressBar.setValue(0)
                    self.ui.btnStart.setEnabled(False)
                    self.ui.filesBtnArea.setEnabled(False)
                    self.ui.terminal.setText(f'> Processing Files...')
                    self.startPerge(btns, outputFolder)
                    
    def startPerge(self, btns: list, outputFolder: str=None):
        def updateUi(btn):
            self.mutex.lock()
            btn.deleteBtn()
            self.ui.progressBar.setValue(self.ui.progressBar.value()+1)
            self.mutex.unlock()
                
        for btn in btns:
            mapWorker = Worker(self.pergeFuzz, 0, data=btn.data, saveFolder=outputFolder)
            mapWorker.signals.finished.connect(partial(updateUi, btn))            
            self.threadPool.start(mapWorker)
        
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.checkThreadPool)
        self.timer.start()

    def checkThreadPool(self):
        if self.threadPool.activeThreadCount() == 0:
            self.timer.stop()
            self.ui.filesBtnArea.setEnabled(True)
            self.ui.progressBar.setValue(self.ui.progressBar.maximum())
            self.ui.terminal.setText('> DONE!')
            
    def pergeFuzz(self, data, saveFolder):
        data.correctSpelling()
        data.fuzzyMap()
        data.save(saveFolder)