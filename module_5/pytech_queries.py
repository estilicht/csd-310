import pymongo
from pymongo import MongoClient



url="mongodb+srv://estlichtenstein:Chana12!@cluster0.hypg9mr.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
students = db.students


docs = students.find({})
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")


for doc in docs:
    print("Student ID: " + str(doc["student_id"]))
    print("First Name: " + str(doc["first_name"]))
    print("Last Name: " + str(doc["last_name"]))
    print()

print()
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY -- ")

doc = students.find_one({"student_id": "1007"})
 
print("Student ID: " + str(doc["student_id"]))
print("First Name: " + str(doc["first_name"]))
print("Last Name: " + str(doc["last_name"]))
