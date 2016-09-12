from indexing.Filedata import filedata
from elasticsearch import Elasticsearch
es = Elasticsearch()

print(filedata().index())

 


'''res = es.search(index="test-index", body={"query": {"match": {"data":"court"}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
   # print("%(name)s%(data)s"%hit['_source'] )
    print("%s" %hit['_score'] )
    '''