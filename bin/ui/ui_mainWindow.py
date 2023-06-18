# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainWindowSRCdeB.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QToolBox, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(840, 490)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.styles = QFrame(self.centralwidget)
        self.styles.setObjectName(u"styles")
        self.styles.setLayoutDirection(Qt.LeftToRight)
        self.styles.setAutoFillBackground(False)
        self.styles.setStyleSheet(u"#styles.QFrame {background-color: rgb(6, 35, 100);}\n"
"#topFrame.QFrame {background-color: rgb(255, 255, 255);}\n"
"#midFrame.QFrame {background-color: rgb(248, 250, 255);}\n"
"#logo {image: url(:/icons/bin/ui/icons/logo.svg)}\n"
"/*_______________Fixed_Styles______________*/\n"
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
""
                        "	color: rgb(90, 90, 90);\n"
"	border: 1px solid rgb(124, 132, 159);\n"
"}\n"
"/*QPushButton*/\n"
"QPushButton {\n"
"	background-color: rgb(6, 35, 100);\n"
"	border-radius: 5px;\n"
"	font: 14pt \"Calibri\";\n"
"	color: rgb(255, 255, 255);\n"
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
""
                        "QDoubleSpinBox, QSpinBox {\n"
"	border: 1px solid rgb(200, 200, 200);\n"
"	border-radius: 5px;\n"
"	color: rgb(90, 90, 90);\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	background-repeat: none;\n"
"	background-position: left center;\n"
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
"	border: 1px solid rgb(124, 13"
                        "2, 159);\n"
"}\n"
"QDateEdit::up-arrow, QDateTimeEdit::up-arrow{\n"
"	image: url(:/icons/bin/ui/icons/cil-arrow-top.png);\n"
"}\n"
"QDateEdit::down-arrow, QDateTimeEdit::down-arrow{\n"
"	image: url(:/icons/bin/ui/icons/cil-arrow-bottom.png);\n"
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
""
                        "	color: rgb(255, 255, 255);\n"
"	background-color: rgb(48, 67, 106);\n"
"	border-left: 4px solid rgb(0, 249, 248);\n"
"}\n"
"\n"
"QToolBox::tab:hover {\n"
"	background-color: rgb(48, 67, 106);\n"
"}\n"
"/*QCheckBox*/\n"
"QCheckBox, QRadioButton {font: 12pt \"Arial\";}\n"
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
"QScrollBar::handl"
                        "e:horizontal:hover, QScrollBar::handle:vertical:hover {background-color: rgb(9, 52, 147);}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: transparent;\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
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
"QScrollBar::add-page:"
                        "horizontal, QScrollBar::sub-page:horizontal {background: none;}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: transparent;\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 4px;\n"
" }\n"
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
"/*QTableView"
                        " QHeaderView::section {padding-right: auto;}*/\n"
"QTableView {\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"QHeaderView {font: 400 15pt \"Segoe UI\";}\n"
"\n"
"QHeaderView::section:horizontal {\n"
"	background-color: rgb(248, 250, 255);\n"
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
        self.styles.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.styles)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sideFrame = QFrame(self.styles)
        self.sideFrame.setObjectName(u"sideFrame")
        self.sideFrame.setMinimumSize(QSize(230, 0))
        self.sideFrame.setMaximumSize(QSize(230, 16777215))
        self.sideFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.sideFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.sideBtnFrame = QFrame(self.sideFrame)
        self.sideBtnFrame.setObjectName(u"sideBtnFrame")
        self.sideBtnFrame.setStyleSheet(u"")
        self.sideBtnFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.sideBtnFrame)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.sideBtnFrame)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(0, 90))
        self.logo.setMaximumSize(QSize(16777215, 90))
        self.logo.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.logo)

        self.labelAppName = QLabel(self.sideBtnFrame)
        self.labelAppName.setObjectName(u"labelAppName")
        self.labelAppName.setMinimumSize(QSize(45, 40))
        self.labelAppName.setMaximumSize(QSize(16777215, 40))
        self.labelAppName.setStyleSheet(u"font: 700 16pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.labelAppName.setAlignment(Qt.AlignCenter)
        self.labelAppName.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.labelAppName)

        self.toolBox_2 = QToolBox(self.sideBtnFrame)
        self.toolBox_2.setObjectName(u"toolBox_2")
        self.toolBox_2.setMinimumSize(QSize(0, 150))
        self.toolBox_2.setMaximumSize(QSize(16777215, 300))
        self.tabConverter = QWidget()
        self.tabConverter.setObjectName(u"tabConverter")
        self.tabConverter.setGeometry(QRect(0, 0, 230, 141))
        self.verticalLayout_17 = QVBoxLayout(self.tabConverter)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.btnPageProdMap = QPushButton(self.tabConverter)
        self.btnPageProdMap.setObjectName(u"btnPageProdMap")
        self.btnPageProdMap.setMaximumSize(QSize(16777215, 25))
        self.btnPageProdMap.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/bin/ui/icons/icons8-hashtag-key-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPageProdMap.setIcon(icon)

        self.verticalLayout_17.addWidget(self.btnPageProdMap)

        self.btnPageFuzzPurge = QPushButton(self.tabConverter)
        self.btnPageFuzzPurge.setObjectName(u"btnPageFuzzPurge")
        self.btnPageFuzzPurge.setMaximumSize(QSize(16777215, 25))
        self.btnPageFuzzPurge.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnPageFuzzPurge.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/bin/ui/icons/icons8-broom-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPageFuzzPurge.setIcon(icon1)

        self.verticalLayout_17.addWidget(self.btnPageFuzzPurge)

        self.btnPageFixExcelFiles = QPushButton(self.tabConverter)
        self.btnPageFixExcelFiles.setObjectName(u"btnPageFixExcelFiles")
        self.btnPageFixExcelFiles.setMaximumSize(QSize(16777215, 25))
        self.btnPageFixExcelFiles.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnPageFixExcelFiles.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/bin/ui/icons/icons8-support-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPageFixExcelFiles.setIcon(icon2)

        self.verticalLayout_17.addWidget(self.btnPageFixExcelFiles)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_2)

        self.toolBox_2.addItem(self.tabConverter, u"Converter")

        self.verticalLayout_3.addWidget(self.toolBox_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addWidget(self.sideBtnFrame)


        self.horizontalLayout.addWidget(self.sideFrame)

        self.mainFrame = QFrame(self.styles)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 3, 6, 6)
        self.topFrame = QFrame(self.mainFrame)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setMinimumSize(QSize(0, 50))
        self.topFrame.setMaximumSize(QSize(16777215, 40))
        self.topFrame.setStyleSheet(u"")
        self.topFrame.setFrameShape(QFrame.NoFrame)
        self.topFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.topFrame)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 10, 0)

        self.verticalLayout_2.addWidget(self.topFrame)

        self.midFrame = QFrame(self.mainFrame)
        self.midFrame.setObjectName(u"midFrame")
        self.midFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.midFrame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.midFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageProductMapper = QWidget()
        self.pageProductMapper.setObjectName(u"pageProductMapper")
        self.horizontalLayout_2 = QHBoxLayout(self.pageProductMapper)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedWidget.addWidget(self.pageProductMapper)
        self.pageFuzzPurge = QWidget()
        self.pageFuzzPurge.setObjectName(u"pageFuzzPurge")
        self.verticalLayout_5 = QVBoxLayout(self.pageFuzzPurge)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget.addWidget(self.pageFuzzPurge)
        self.pageFixExcelFiles = QWidget()
        self.pageFixExcelFiles.setObjectName(u"pageFixExcelFiles")
        self.verticalLayout_4 = QVBoxLayout(self.pageFixExcelFiles)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget.addWidget(self.pageFixExcelFiles)

        self.verticalLayout_12.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.midFrame)

        self.midFrame.raise_()
        self.topFrame.raise_()

        self.horizontalLayout.addWidget(self.mainFrame)


        self.verticalLayout.addWidget(self.styles)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox_2.setCurrentIndex(0)
        self.toolBox_2.layout().setSpacing(6)
        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.labelAppName.setText(QCoreApplication.translate("MainWindow", u"Hayat Data ToolKit", None))
        self.btnPageProdMap.setText(QCoreApplication.translate("MainWindow", u"Products Mapper", None))
        self.btnPageFuzzPurge.setText(QCoreApplication.translate("MainWindow", u"Fuzz Purge", None))
        self.btnPageFixExcelFiles.setText(QCoreApplication.translate("MainWindow", u"Fix Excel Files", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.tabConverter), QCoreApplication.translate("MainWindow", u"Converter", None))
    # retranslateUi

