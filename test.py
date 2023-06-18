from pathlib import Path
import openpyxl

fileLocPath = Path('E:\\Hayat\\xlsToxlsx\\Bilan avril 2023.xlsx')
saveFolder = fileLocPath.parent / f"{fileLocPath.stem}_output{fileLocPath.suffix}"

workbook = openpyxl.load_workbook(fileLocPath)
workbook.save(saveFolder)