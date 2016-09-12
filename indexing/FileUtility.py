import configparser

class FileUtility:
    #fileName = '.\\input\\settings.ini'
    fileName = '/users/rahulchandrawanshi/documents/workspace/Elastic search/indexing/settings.ini'
    
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.fileName)
    
    def getKeyForSectionInFile(self, filePath, section, key):
        self.config.read(filePath)
        sectionDetails = self.config[section]
        return sectionDetails[key]
     
    def readFileSettings(self):  
        fileSettings  = self.config['FILES']
        fileSettingsDictionary = {}
        fileSettingsDictionary['Directory'] = fileSettings['Directory']
        return fileSettingsDictionary
    