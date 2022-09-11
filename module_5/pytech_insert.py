import pymongo
from pymongo import MongoClient

url="mongodb+srv://estlichtenstein:Chana12!@cluster0.hypg9mr.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
pytech = db["PyTech"]

records = [
    {
        "student_id": "1007",
        "first_name": "Fred",
        "last_name": "Fuller"
    },
    {
        "student_id": "1008",
        "first_name": "Mary",
        "last_name": "Miller"
    },
    {
        "student_id": "1009",
        "first_name": "Sam",
        "last_name": "Bella"
    }
]

for record in records:
    new_student_Id = pytech.insert_one(record).inserted_id
    print(new_student_Id)

docs = pytech.find()

for doc in docs:
    print(doc)

print(pytech.find_one({"student_id": "1008"}))

input('Press ENTER to exit')
