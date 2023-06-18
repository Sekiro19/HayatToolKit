from functools import partial
from pathlib import Path
import pandas as pd
from core import *
from .pages.ui_pyProductMapper import Ui_Form_ProductMapper
from .widgets.pyFileButton import FileBtn
from ..modules import ProductDataMapper, Worker

class FormProductMapper(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Form_ProductMapper()
        self.ui.setupUi(self)
        # thread pool
        self.threadPool = QThreadPool.globalInstance()
        self.threadPool.setMaxThreadCount(1)
        self.mutex = QMutex()
        # defaults
        self.selectedButton = None
        self.products = None
        # ui
        self.ui.btnLoadProductsFiles.clicked.connect(self.loadProducts)
        self.ui.btnStart.clicked.connect(self.start)
        self.ui.btnLoadFiles.clicked.connect(self.loadFiles)
        self.ui.btnLoadFiles.setEnabled(False)
        self.ui.btnStart.setEnabled(False)
        self.ui.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.tableWidget.cellChanged.connect(self.handleCellChanged)
        self.setFileCheckBoxVisible(False)
        self.ui.chBoxIncludeAllCols.stateChanged.connect(self.includeAllCols)
        self.ui.chBoxIncludeAllSeets.stateChanged.connect(self.setIncludeAllSheets)

    def includeAllCols(self, state):
        self.selectedButton.data.includeNaLast = bool(state)
    
    def setIncludeAllSheets(self, state):
        for row in range(self.ui.tableWidget.rowCount()):
            if state:
                self.ui.tableWidget.item(row, 0).setCheckState(Qt.CheckState.Checked)
        
    def setRowEditState(self, row: int, isEditable: bool):
        for col in range(1, self.ui.tableWidget.columnCount()):
            item = self.ui.tableWidget.item(row, col)
            if item is not None:
                if isEditable:
                    item.setFlags(item.flags() | Qt.ItemIsEditable)
                else:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                    item.setText('')

    def handleCellChanged(self, row: int, col: int):
        item = self.ui.tableWidget.item(row, col)
        if item is None:
            return
        if col == 0:
            if item.checkState() == Qt.Checked:
                self.selectedButton.data.settings.iloc[row, 0] = True
                self.setRowEditState(row, True)
            else:
                self.selectedButton.data.settings.iloc[row, 0] = False
                self.setRowEditState(row, False)
                self.ui.chBoxIncludeAllSeets.setChecked(False)
        else:
            xlsxCol = item.text().strip().upper()
            if not xlsxCol:
                self.selectedButton.data.settings.iloc[row, col+1] = None
                item.setText('')
            elif xlsxCol.isalpha() and len(xlsxCol) <= 3:
                self.selectedButton.data.settings.iloc[row, col+1] = xlsxCol
            else:
                showMsg(f'"{xlsxCol}" is not a valid Excel column name', 'notice')
                item.setText('')

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
                    self.setFileCheckBoxVisible(False)
                    self.ui.terminal.setText(f'> Mapping Products...')
                    self.clearTable()
                    self.mapToExcelThread(btns, outputFolder)
    
    def setFileCheckBoxVisible(self, state):
        self.ui.chBoxIncludeAllCols.setVisible(state)
        self.ui.chBoxIncludeAllSeets.setVisible(state)
            
    def mapToExcelThread(self, btns: list, outputFolder: str=None):
        self.skipedFiles = False
        def updateUi(btn, result):
            self.mutex.lock()
            if result:
                btn.deleteBtn()
                self.ui.progressBar.setValue(self.ui.progressBar.value()+1)
            else:
                self.skipedFiles = True
            self.mutex.unlock()
                
        for btn in btns:
            mapWorker = Worker(btn.data.mapToExcel, 0, save=True, saveFolder=outputFolder)            
            mapWorker.signals.results.connect(partial(updateUi, btn))            
            self.threadPool.start(mapWorker)
        
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.checkThreadPool)
        self.timer.start()
        
    def checkThreadPool(self):
        if self.threadPool.activeThreadCount() == 0:
            self.timer.stop()
            if self.skipedFiles:
                self.ui.terminal.setText("> Files were skipped because the necessary parameters were not set.")
                self.ui.btnStart.setEnabled(True)
                
            self.ui.filesBtnArea.setEnabled(True)
            self.ui.progressBar.setValue(self.ui.progressBar.maximum())
            self.ui.terminal.setText(f'{self.ui.terminal.text()}\n> DONE!'.strip('\n'))

    def loadProducts(self):
        filesList = openDialogue(nameFilter="Csv file (*.csv)")
        if filesList:
            productsPath = filesList[0]
            self.products = pd.read_csv(productsPath)
            if 'NUM' in self.products.columns:
                mask = self.products['NUM'].duplicated()
                if mask.any():
                    showMsg(f"Products File contains duplicates!\n{self.products.loc[mask, 'NUM'].values}", 'error')
                else:
                    self.products.set_index('NUM', drop=True, inplace=True)
                    self.ui.btnLoadFiles.setEnabled(True)
                    self.ui.progressBar.setValue(100)
                    self.ui.terminal.setText('> Products loaded successfully.')
                    self.clearLayout()
            else:
                showMsg(f"Products File dose not contain 'NUM' column", 'error')

    def loadFiles(self):
        filesList = openDialogue(mode=QFileDialog.ExistingFiles, nameFilter="Excel files (*.xlsx)")
        if filesList:
            filePaths = filesList
            self.ui.progressBar.setValue(0)
            self.processFiles(filePaths)

    def processFiles(self, filePaths: list):
        numFiles = len(filePaths)
        self.ui.progressBar.setMaximum(numFiles)
        files = [btn.data.fileLoc for btn in self.getButtons()]
        for i in range(numFiles):
            if filePaths[i] in files:
                showMsg('File already selected', 'notice')
            else:
                self.ui.terminal.setText(f'> Loading Files...')
                worker = Worker(ProductDataMapper, 0, filePaths[i], self.products)
                worker.signals.results.connect(self.setButton)
                worker.signals.finished.connect(partial(self.ui.btnStart.setEnabled, True))
                self.threadPool.start(worker)

    def setButton(self, mapperInstance):
        fileBtn = FileBtn(text=Path(mapperInstance.fileLoc).name, data=mapperInstance)
        fileBtn.clicked.connect(self.showDataInfo)
        try:
            self.mutex.lock()
            self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)
            self.ui.filesBtnArea.layout().insertWidget(0, fileBtn)
            if self.threadPool.activeThreadCount() == 0:
                self.ui.terminal.setText('> DONE!')
        finally:
            self.mutex.unlock()

    def showDataInfo(self):
        btn = self.sender()
        self.setFileCheckBoxVisible(False)
        self.selectedButton = btn
        maperInstance = btn.data
        self.loadFileSettings(maperInstance.settings)
        self.ui.terminal.setText(f'Selected file settings: {maperInstance.fileLoc}')
        self.ui.chBoxIncludeAllCols.setChecked(maperInstance.includeNaLast)
        self.ui.chBoxIncludeAllSeets.setChecked(maperInstance.settings['Check'].all())
        self.setFileCheckBoxVisible(True)
 
    def loadFileSettings(self, df: pd.DataFrame):
        self.clearTable()
        cols = df.columns[1:]
        self.ui.tableWidget.setColumnCount(len(cols))
        self.ui.tableWidget.setRowCount(len(df.index))
        self.ui.tableWidget.setHorizontalHeaderLabels(cols)
        
        prototype = QTableWidgetItem()
        prototype.setFlags(prototype.flags() & ~Qt.ItemIsEditable)
        self.ui.tableWidget.setItemPrototype(prototype)

        
        for iRow, rowData in enumerate(df.values):
            for iCol, cellData in enumerate(rowData[1:]):
                item = self.ui.tableWidget.item(iRow, iCol)
                if not item:
                    item = QTableWidgetItem()
                if pd.isna(cellData):
                    data = ''
                else:
                    data = str(cellData)
                item.setData(Qt.EditRole, data)

                if iCol == 0:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                    if df.iloc[iRow, 0]:
                        item.setCheckState(Qt.CheckState.Checked)
                    else:
                        item.setCheckState(Qt.CheckState.Unchecked)
                else:
                    if self.ui.tableWidget.item(iRow, 0).checkState() == Qt.Checked:
                        item.setFlags(item.flags() | Qt.ItemIsEditable)
                    else:
                        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                    
                self.ui.tableWidget.setItem(iRow, iCol, item)
                
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        
    def clearLayout(self):
        while self.ui.filesBtnArea.layout().count() > 1:
            child = self.ui.filesBtnArea.layout().takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def clearTable(self):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(0)