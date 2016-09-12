
from indexing.FileUtility import FileUtility
import os
from elasticsearch import Elasticsearch

class filedata:
    
    es = Elasticsearch()
    def __init__(self):
        fileUtility = FileUtility()
        fileSettings = fileUtility.readFileSettings()
        self.directory = fileSettings['Directory']
        self.fileCount = len(os.listdir(self.directory))
      
    

    
    def getFileContent(self, filename):
        file = open(filename, 'rb')
        fileContent = str(file.read()).replace('&quot;','"').replace('\\t','\t').replace('\\n','\n').replace('\\','')
        return fileContent
    


    def index(self):
        
        files = os.listdir(self.directory)
        no_of_files_added=0
        for file in files:
            if (file == '.DS_Store'):
                continue
            
            if(False == os.path.isdir(file)):
                data = self.getFileContent(self.directory + "/" + file)
                fileName = os.path.splitext(os.path.basename(file))[0]
                doc = { 'name':fileName,
                       'data':data}
                res = self.es.index(index="supreme_court_index", doc_type='law', body=doc)
                if(res['created']==True):
                    no_of_files_added+=1
                
                  
        return no_of_files_added
