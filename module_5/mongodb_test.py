import pymongo
from pymongo import MongoClient

url="mongodb://estlichtenstein:Chana12!@ac-cgmlvgz-shard-00-00.hypg9mr.mongodb.net:27017,ac-cgmlvgz-shard-00-01.hypg9mr.mongodb.net:27017,ac-cgmlvgz-shard-00-02.hypg9mr.mongodb.net:27017/?ssl=true&replicaSet=atlas-etuuci-shard-0&authSource=admin&retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print (db.list_collection_names)  

input('Press ENTER to exit')
