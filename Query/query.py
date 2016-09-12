from elasticsearch import Elasticsearch

class search_engine:
    
    es =Elasticsearch()
    def __init__(self,query):
        self.query =query
        
    def search_query(self):
        res = self.es.search(index="supreme_court_index", body={"query": {"match": {"data":self.query}}})
        print(res['hits']['total'])
        return res 
        
    