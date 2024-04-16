import random

class config:
     
    def __init__(self):
        self.__states__ = ['ca','az','nv','tx'] #defaults to ['ca','az','nv','tx']
        self.__defaultBackoff__ = 3 #may not work with values under 3. This is the minimum number of seconds the program waits between clicks on webpages.
        self.__variableBackoff__ = 2 #how random the interval between web page clicks are. "0" means it clicks every $defaultBackoff (default 3) seconds. "2" means it clicks between $defaultBackoff (default 3) seconds and $defaultBackoff (default 5) seconds.
        self.__sheetSaveName__ = "99 Cent Store Locations" #The Sheet Save Name
        self.__pathSaveName__ = "NinetyNineCentStoreData.xlsx" #The Save Path Name
        self.__numberedRows__ = False #Whether or not the first column is numbered

    def getStates(self):
        return self.__states__
    
    def getBackoff(self):
        return self.__defaultBackoff__

    def getVariableBackoff(self):
        return random.random()*self.__variableBackoff__
    
    def getSheetName(self):
        return self.__sheetSaveName__
    
    def getSavePath(self):
        return self.__pathSaveName__
    
    def isIndexed(self):
        return self.__numberedRows__