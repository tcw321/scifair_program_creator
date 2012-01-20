import pymongo

from pymongo import Connection
connection = Connection()

db = connection.science_fair
entries = db.entries

list_of_teachers = []
for entry in entries.find({ "teacher": { "$exists" :True}}, {"teacher" : "1"}):
    if entry["teacher"] not in list_of_teachers:
        list_of_teachers.append(entry["teacher"])
print list_of_teachers
