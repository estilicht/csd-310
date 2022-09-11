import pymongo
from pymongo import MongoClient

url="mongodb+srv://estlichtenstein:Chana12!@cluster0.hypg9mr.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
x="--Pytech Collection List--"
print(x)
print(db.list_collection_names()) 

input('Press ENTER to exit')

