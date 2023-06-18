from PySide6.QtWidgets import QPushButton, QToolButton
from PySide6.QtGui import QCursor, Qt

class FileBtn(QPushButton):
    def __init__(self, text="", parent=None, data=None):
        super().__init__(text, parent)
        self.data = data
        self.closeBtn = QToolButton(self)
        self.closeBtn.clicked.connect(self.deleteBtn)
        self.closeBtn.setMaximumHeight(18)
        self.closeBtn.setMaximumWidth(18)
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeBtn.setToolTip('Remove')
        self.closeBtn.setStyleSheet("""
QToolButton {background-color: transparent;
	image: url(:/icons/bin/ui/icons/icons8-x-48.png);
    margin: 1px;
}
QToolButton:hover {
	border: 4px solid transparent;
}
""")
        self.setStyleSheet("""
QPushButton {
	background-color: rgb(22, 145, 84);
	border-radius: 8px;
	font: 11pt "Consolas";
	color: rgb(255, 255, 255);
	padding-left: 20px;
    padding-right: 10px;
}
QPushButton:hover {
	background-color: rgb(25, 172, 101);
}
QPushButton:pressed {
	background-color: rgb(41, 194, 127);
}""")

    def deleteBtn(self):
        self.deleteLater()
        del self.data