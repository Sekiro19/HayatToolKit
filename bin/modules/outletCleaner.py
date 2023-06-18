from pathlib import Path
import numpy as np
import openpyxl
import pandas as pd
from dateCleaner import FuzzTransformer
from openpyxl.utils.dataframe import dataframe_to_rows


FR_DAYS = {"Lundi": 0, "Mardi": 1, "Mercredi": 2, "Jeudi": 3, "Vendredi": 4, "Samedi": 5, "Dimanche": 6}
TYPE_NAME = {'SUPERETTE': 1, 'SUPERETTE MT': 2, 'ALIMENTATION GENERAL': 3, 'COSMETIQUE': 4, 'TABAC JOURNAUX/KIOSQUE': 5, 
             'ARTICLE DETERGENT': 6, 'ARTICLE BEBE': 7, 'DROGUERIE': 8, 'PHARMACIE': 9, 'HOTEL/CAFE/': 10, 'AUTRE': 11, 
             'MIXTE': 12, 'HYGIENE': 13, 'DETEREGNT': 14, 
             'AG': 3, 'AB': 7, 'AD': 6, 'SUPMT': 2}

class OutletCleaner:
    def __init__(self, fileLoc: str, formatLoc: str) -> None:
        self.fileLoc = fileLoc
        self.dfFormat = pd.read_csv(formatLoc)
        self.workbook = openpyxl.load_workbook(self.fileLoc)
        self.worksheet = self.workbook.active
        self.dfOutlet = pd.read_excel(self.fileLoc, sheet_name=self.worksheet.title)
        self.setWilaya()
        self.fuzzTransformer = FuzzTransformer(threshold=80)

    
    def setWilaya(self):
        self.dfOutlet['City'] = self.dfOutlet['City'].str.strip().replace('', np.nan).fillna(method='ffill')
        outletCities = self.dfOutlet['City'].dropna().str.strip().unique()
        validCities = self.dfFormat[['City', 'NumWilaya']].drop_duplicates().dropna()
        numWilaya = validCities[validCities['City'].isin(outletCities)]['NumWilaya'].tolist()
        self.dfFormat = self.dfFormat[self.dfFormat['NumWilaya'].isin(numWilaya)]

    def correctSpelling(self) -> pd.Series:
        seriesToClean = self.dfOutlet['Town'].str.strip().replace('', pd.NA).fillna(self.dfOutlet['City'].ffill())
        validChoices = self.dfFormat['Town'].to_list()
        self.dfOutlet['Town'] = self.fuzzTransformer.cleanFuzzySeries(seriesToClean, validChoices)

    def fuzzyMap(self):
        self.dfOutlet['jour de visite'] = self.fuzzTransformer.mapFuzzySeries(self.dfOutlet['jour de visite'], FR_DAYS)
        self.dfOutlet['Outlet Type'] = self.fuzzTransformer.mapFuzzySeries(self.dfOutlet['Outlet Type'], TYPE_NAME)
    
    def save(self, saveFolder: str=None):
        self.worksheet.delete_rows(2, self.worksheet.max_row)
        for row in dataframe_to_rows(self.dfOutlet, index=False, header=False):
            self.worksheet.append(row)
            
        if saveFolder is None:
            saveFolder = self.fileLoc
        else:
            fileLocPath = Path(self.fileLoc)
            saveFolder = Path(saveFolder) / f"{fileLocPath.stem}_output{fileLocPath.suffix}"
        
        self.workbook.save(saveFolder)