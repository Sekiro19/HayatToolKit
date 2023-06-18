import sys
from core import *
from bin import *


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #--------------------------- signals ------------------------
        # ProductMapper
        self.formProductMapper = FormProductMapper()
        self.ui.pageProductMapper.layout().addWidget(self.formProductMapper)
        self.ui.btnPageProdMap.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageProductMapper))
        # FuzzPurge
        self.formFuzzPurge = FormFuzzPurge()
        self.ui.pageFuzzPurge.layout().addWidget(self.formFuzzPurge)
        self.ui.btnPageFuzzPurge.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageFuzzPurge))
        # FixExcelFiles
        self.formFixExcelFiles = FormFixExcelFiles()
        self.ui.pageFixExcelFiles.layout().addWidget(self.formFixExcelFiles)
        self.ui.btnPageFixExcelFiles.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageFixExcelFiles))
        
        
        self.show()

    def closeEvent(self, event: QCloseEvent) -> None:  # handle close window
        msg = QMessageBox.question(self, "Window close", "Close the window ?", QMessageBox.Yes, QMessageBox.No)
        if msg == QMessageBox.Yes:
            QThreadPool.globalInstance().clear()
            event.accept()
        else:
            event.ignore()
    

if __name__ == "__main__":
    app = QApplication()
    app.setApplicationName('Hayat Data ToolKit')
    app.setApplicationVersion('v1.0.0 (64-bit)')
    app.setWindowIcon(QIcon(r':/icons/bin/ui/icons/logo.svg'))
    mainWindows = MainWindow()
    mainWindows.setWindowTitle('Hayat Data ToolKit')
    sys.exit(app.exec())