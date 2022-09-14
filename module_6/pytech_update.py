import pymongo
from pymongo import MongoClient

url = "mongodb+srv://estlichtenstein:Chana12!@cluster0.hypg9mr.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
students = db.students
student_list = students.find({})

print("\n --DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print("Student ID: " + str(doc["student_id"]))
    print("First Name: " + str(doc["first_name"]))
    print("Last Name: " + str(doc["last_name"]))
    print()

for doc in student_list:
    print (" Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Jonas"}})

fred = students.find_one({"student_id": "1007"})
print("\n --DISPLAYING STUDENT DOCUMENT 1007 --")

print(" Student ID: " + fred["student_id"] + "\n First Name: " + fred["first_name"] + "\n Last Name: " + fred["last_name"] + "\n")


input("\n\n End of program, press any key to continue...")
