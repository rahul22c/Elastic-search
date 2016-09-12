from Query.query import search_engine
from flask import Flask, render_template, request, url_for


 
result={}

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('mypage.html')

@app.route("/search",methods=['POST'])
def search():
    print(request.form['searchkey'])
    query = str(request.form['searchkey'])
    global result
    result= search_engine(query).search_query()
    for hit in result['hits']['hits']: 
        print (hit['_source']['name'])
    return render_template('result.html',name=result)
@app.route("/files/<name>" )
def files(name):
    value=1
    a='\n'
    global result
    for hit in result['hits']['hits']: 
        if hit['_source']['name']==name:
            nm= hit['_source']['data']
            name= str(nm)
            name= name.replace('\n','<br>').replace('\t','')
           
    return render_template('filedata.html', n=name)

if __name__ == "__main__":
    app.run()
    
