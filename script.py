# make sure ES is up and running
import requests
def check( ):
   res = requests.get('http://localhost:9200')
   print (res.content)
   return;

#connect to our cluster
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': '52.38.86.62', 'port': 9200}])

import json
def indexes(): 
# get all indexes
   r1 = requests.get('http://52.38.86.62:9200/_cat/indices?v')
   print(r1.content)
   return;
# get all of the content
def content():
   r = requests.get('http://52.38.86.62:9200/_search?pretty=true')
   print(r.content)
   return; 

#Get cluster health
def health():
   health = requests.get('http://52.38.86.62:9200/_cluster/health')
   print(health.content)
   return;
# search query
def search():
   search = requests.get('http://52.38.86.62:9200/_search?q=11943&size=5')
   print(r.search)
   return;
content()

