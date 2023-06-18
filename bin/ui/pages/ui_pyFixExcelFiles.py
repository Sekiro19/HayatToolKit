# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_pyFixExcelFilesCADqFi.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form_FixExcelFiles(object):
    def setupUi(self, Form_FixExcelFiles):
        if not Form_FixExcelFiles.objectName():
            Form_FixExcelFiles.setObjectName(u"Form_FixExcelFiles")
        Form_FixExcelFiles.resize(661, 401)
        Form_FixExcelFiles.setStyleSheet(u"/*_______________Fixed_Styles______________*/\n"
"QLabel {font: 12pt \"Arial\";}\n"
"/*QPlainTextEdit*/\n"
"QPlainTextEdit {\n"
"	border: 1px solid rgb(200, 200, 200);\n"
"	border-radius: 5px;\n"
"	background-color: white;\n"
"	color: rgb(90, 90, 90);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(124, 132, 159);\n"
"}\n"
"/*QLineEdit*/\n"
"QLineEdit {\n"
"	border: 1px solid rgb(200, 200, 200);\n"
"	border-radius: 5px;\n"
"	background-color: white;\n"
"	color: rgb(90, 90, 90);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"}\n"
"QLineEdit:focus {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(124, 132, 159);\n"
"}\n"
"/*QPushButton*/\n"
"QPushButton {\n"
"	background-color: rgb(6, 35, 100);\n"
"	border-radius: 5px;\n"
"	font: 14pt \"Calibri\";\n"
"	color: rgb(255, 25"
                        "5, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(9, 53, 148);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(60, 69, 165);\n"
"}\n"
"/*QComboBox*/\n"
"QComboBox{\n"
"	color: rgb(90, 90, 90);\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
"	border: 1px solid rgb(200, 200, 200);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(124, 132, 159);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 30px; \n"
"	background-image: url(:/icons/bin/ui/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"/*QDoubleSpinBox*/\n"
"QDoubleSpinBox, QSpinBox {\n"
"	border: 1px solid rgb(200, 200, 200);\n"
"	border-radius: 5px;\n"
"	color: rgb(90, 90, 90);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-positio"
                        "n: left center;\n"
"}\n"
"QDoubleSpinBox:focus, QSpinBox:focus {\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(124, 132, 159);\n"
"}\n"
"QDoubleSpinBox::up-arrow, QSpinBox::up-arrow {\n"
"	image: url(:/icons/bin/ui/icons/cil-arrow-top.png);\n"
"}\n"
"QDoubleSpinBox::down-arrow, QSpinBox::down-arrow {\n"
"	image: url(:/icons/bin/ui/icons/cil-arrow-bottom.png);\n"
"}\n"
"QDoubleSpinBox::up-button, QDoubleSpinBox::down-button, QSpinBox::up-button, QSpinBox::down-button {\n"
"    background: transparent;\n"
"}\n"
"/*QDateEdit*/\n"
"QDateEdit, QDateTimeEdit{\n"
"	color: rgb(90, 90, 90);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(200, 200, 200);\n"
"	padding: 5px;\n"
"}\n"
"QDateEdit:hover, QDateTimeEdit:hover{\n"
"	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(124, 132, 159);\n"
"}\n"
"QDateEdit::up-arrow, QDateTimeEdit::up-arrow{\n"
"	image: url(:/icons/bin/ui/icons/cil-arrow-top.png);\n"
"}\n"
"QDateEdit::down-arrow, QDateTimeEdit::down-arrow{\n"
"	image: url(:/icons/bin/ui/icons/cil-arrow"
                        "-bottom.png);\n"
"}\n"
"QDateEdit::up-button, QDateEdit::down-button, QDateTimeEdit::up-button, QDateTimeEdit::down-button {\n"
"    background: transparent;\n"
"}\n"
"/*QToolBox*/\n"
"QToolBox QPushButton {\n"
"	background-color: transparent;\n"
"    color: rgb(220,220,220);\n"
"	font: 600 12pt \"Segoe UI\";\n"
"	text-align: left;\n"
"	padding-left: 20px;\n"
"}\n"
"QToolBox QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"}\n"
"QToolBox QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"}\n"
"QToolBox::tab {\n"
"	border-radius: none;\n"
"	font: 700 13pt \"Segoe UI\";\n"
"    color: rgb(137, 156, 176);\n"
"	padding-left: 10px;\n"
"	background-repeat: none;\n"
"\n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(48, 67, 106);\n"
"	border-left: 4px solid rgb(0, 249, 248);\n"
"}\n"
"\n"
"QToolBox::tab:hover {\n"
"	background-color: rgb(48, 67, 106);\n"
"}\n"
"/*QCheckBox*/\n"
"QCheck"
                        "Box, QRadioButton {font: 12pt \"Arial\";}\n"
"QCheckBox::indicator, QRadioButton::indicator {\n"
"    border: 2px solid rgb(103, 103, 103);\n"
"    background: rgb(6, 35, 100);\n"
"	width: 12px;\n"
"	height: 12px;\n"
"	border-radius: 4px;\n"
"	image: none;\n"
"}\n"
"QCheckBox::indicator:hover, QRadioButton::indicator:hover {\n"
"    border: 2px solid rgb(141, 141, 141);\n"
"}\n"
"QRadioButton::indicator {\n"
"	border-radius: 8px;\n"
"}\n"
"QRadioButton::indicator:checked, QCheckBox::indicator:checked {\n"
"    background: solid rgb(189, 255, 0);\n"
"}\n"
"/*QScrollArea*/\n"
"QScrollArea { background: transparent; }\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"QScrollArea > QWidget > QScrollBar { background: palette(base); }\n"
"/*QScrollBar*/\n"
"QScrollBar::handle:horizontal:hover, QScrollBar::handle:vertical:hover {background-color: rgb(9, 52, 147);}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: transparent;\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;"
                        "\n"
"	border-radius: 4px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(6, 35, 100);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	border: none;\n"
"    background: transparent;\n"
"	width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"	border: none;\n"
"    background: transparent;\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {background: none;}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {background: none;}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 4px;\n"
" }\n"
""
                        " QScrollBar::handle:vertical {	\n"
"    background: rgb(6, 35, 100);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: transparent;\n"
"     height: 10px;\n"
"    border-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"/*QTableView QHeaderView::section {padding-right: auto;}*/\n"
"QTableView {\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"QHeaderView {font: 400 15pt \"Segoe UI\";}\n"
"\n"
"QHeaderView::section:horizontal {\n"
"	background-color: rgb(248, 250, 255"
                        ");\n"
"	border: none;\n"
"	font: 400 11pt \"Segoe UI\";\n"
"}\n"
"QTableView::item {\n"
"	padding-left: 15px;\n"
"	border-bottom: 1px solid rgb(235, 235, 235);\n"
"}\n"
"QTableView::item:selected {\n"
"	background-color: rgba(248, 250, 255, 127);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout = QVBoxLayout(Form_FixExcelFiles)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainFrame = QFrame(Form_FixExcelFiles)
        self.mainFrame.setObjectName(u"mainFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setMinimumSize(QSize(0, 0))
        self.mainFrame.setMaximumSize(QSize(16777215, 16777215))
        self.mainFrame.setStyleSheet(u"#mainFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.mainFrame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 40))
        self.label.setMaximumSize(QSize(16777215, 40))
        self.label.setStyleSheet(u"font: 700 18pt \"Arial\";\n"
"")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnLoadFiles = QPushButton(self.mainFrame)
        self.btnLoadFiles.setObjectName(u"btnLoadFiles")
        self.btnLoadFiles.setMinimumSize(QSize(110, 35))
        self.btnLoadFiles.setMaximumSize(QSize(110, 35))
        self.btnLoadFiles.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btnLoadFiles, 0, 0, 1, 1)

        self.btnStart = QPushButton(self.mainFrame)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setMinimumSize(QSize(70, 35))
        self.btnStart.setMaximumSize(QSize(70, 35))
        self.btnStart.setStyleSheet(u"")

        self.gridLayout.addWidget(self.btnStart, 0, 1, 1, 1)

        self.chBoxInplace = QCheckBox(self.mainFrame)
        self.chBoxInplace.setObjectName(u"chBoxInplace")
        self.chBoxInplace.setCursor(QCursor(Qt.PointingHandCursor))
        self.chBoxInplace.setStyleSheet(u"")

        self.gridLayout.addWidget(self.chBoxInplace, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.progressBar = QProgressBar(self.mainFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setMinimumSize(QSize(0, 8))
        self.progressBar.setMaximumSize(QSize(16777215, 8))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"    text-align: right;\n"
"	font: 8pt \"Consolas\";\n"
"    background-color: #f2f2f2;\n"
"    height: 8px;\n"
"	color: rgb(6, 35, 100);\n"
"\n"
"	margin-right: 30px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #4285F4;\n"
"    border-radius: 4px;\n"
"}\n"
"QProgressBar::chunk:disabled {\n"
"    background-color: #c2c2c2;\n"
"}\n"
"\n"
"")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 4)

        self.terminal = QLabel(self.mainFrame)
        self.terminal.setObjectName(u"terminal")
        self.terminal.setMinimumSize(QSize(0, 0))
        self.terminal.setMaximumSize(QSize(16777215, 16777215))
        self.terminal.setStyleSheet(u"font: 10pt \"Consolas\";")
        self.terminal.setTextFormat(Qt.PlainText)
        self.terminal.setScaledContents(False)
        self.terminal.setWordWrap(True)
        self.terminal.setIndent(1)
        self.terminal.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.terminal, 2, 0, 1, 4)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalSpacer = QSpacerItem(20, 183, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.mainFrame)


        self.retranslateUi(Form_FixExcelFiles)

        QMetaObject.connectSlotsByName(Form_FixExcelFiles)
    # setupUi

    def retranslateUi(self, Form_FixExcelFiles):
        Form_FixExcelFiles.setWindowTitle(QCoreApplication.translate("Form_FixExcelFiles", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form_FixExcelFiles", u"<html><head/><body><p align=\"center\">Fix Excel Files</p></body></html>", None))
        self.btnLoadFiles.setText(QCoreApplication.translate("Form_FixExcelFiles", u"Load Files", None))
        self.btnStart.setText(QCoreApplication.translate("Form_FixExcelFiles", u"Start", None))
#if QT_CONFIG(tooltip)
        self.chBoxInplace.setToolTip(QCoreApplication.translate("Form_FixExcelFiles", u"<html><head/><body><p>Replace processed files with originals</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.chBoxInplace.setText(QCoreApplication.translate("Form_FixExcelFiles", u"Save inplace", None))
        self.terminal.setText("")
    # retranslateUi

