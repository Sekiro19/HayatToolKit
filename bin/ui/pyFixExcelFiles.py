from functools import partial
import openpyxl
from core import *
from .pages.ui_pyFixExcelFiles import Ui_Form_FixExcelFiles
from pathlib import Path
from ..modules import Worker

class FormFixExcelFiles(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Form_FixExcelFiles()
        self.ui.setupUi(self)
        # thread pool
        self.threadPool = QThreadPool.globalInstance()
        # self.threadPool.setMaxThreadCount(1)
        self.mutex = QMutex()
        # defaults
        self.filesList = None
        # ui
        self.ui.btnLoadFiles.clicked.connect(self.loadFiles)
        self.ui.btnStart.clicked.connect(self.start)
        self.ui.btnStart.setEnabled(False)
    
            
    def loadFiles(self):
        self.filesList = openDialogue(mode=QFileDialog.ExistingFiles, nameFilter="Excel files (*.xlsx)")
        for f in self.filesList:
            self.ui.terminal.setText(f'{self.ui.terminal.text()}\n> {f}'.strip('\n'))
        if self.filesList:
            self.ui.btnStart.setEnabled(True)
            
    def start(self):
        if self.ui.chBoxInplace.isChecked():
            outputFolder = None
        else:
            filesList = openDialogue(mode=QFileDialog.Directory)
            if filesList:
                outputFolder = filesList[0]
                self.ui.progressBar.setMaximum(len(self.filesList))
                self.ui.terminal.setText('Processing files...')
                for f in self.filesList:
                    worker = Worker(self.fixExcel, 0, f, outputFolder)
                    self.threadPool.start(worker)   

    def fixExcel(self, fileLoc: str, saveFolder: str=None):
        workbook = openpyxl.load_workbook(fileLoc)
        
        if saveFolder is None:
            saveFolder = fileLoc
        else:
            fileLocPath = Path(fileLoc)
            saveFolder = Path(saveFolder) / f"{fileLocPath.stem}_output{fileLocPath.suffix}"
        
        workbook.save(saveFolder)
        self.ui.progressBar.setValue(self.ui.progressBar.value()+1)
        
        if not self.filesList:
            self.ui.btnStart.setEnabled(False)