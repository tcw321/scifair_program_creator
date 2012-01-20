import pymongo

from pymongo import Connection
connection = Connection()

db = connection.science_fair
entries = db.entries

list_of_other = []
for entry in entries.find({ "other": { "$exists" :True}}, {"other" : "1"}):
    if entry["other"] != '':
        list_of_other.append(entry["other"])
print list_of_other
