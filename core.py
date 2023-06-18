from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from json import load as load_json

internalPaths = {
    'styles': 'styles.json',
    'CityData': 'bin\data\CityData.csv'
                 }

with open(internalPaths['styles'], 'r') as f:
    styles = load_json(f)

def showMsg(text: str, msgType: str, buttons: list=list()):
    msg = QMessageBox()
    for btn in buttons:
        msg.addButton(btn)
    msg.setWindowFlag(Qt.FramelessWindowHint)
    
    if msgType == 'error':
        style = styles['STYLE_ERROR_MSG']
    elif msgType == 'notice':
        style = styles['STYLE_NOTICE_MSG']
    elif msgType == 'succes':
        style = styles['STYLE_NOTICE_MSG']
    else:
        style = ''
    msg.setStyleSheet(style)
    msg.setText(text)

    return msg.exec()


def openDialogue(mode=None, nameFilter: str=None):
    fileDialog = QFileDialog()
    if mode is not None:
        fileDialog.setFileMode(mode)
    if nameFilter is not None:
        fileDialog.setNameFilter(nameFilter)
    if fileDialog.exec_() == QFileDialog.Accepted:
        return fileDialog.selectedFiles()
    