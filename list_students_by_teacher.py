
import pymongo

from pymongo import Connection
connection = Connection()

db = connection.science_fair
entries = db.entries



for entry in entries.find():
    print entry["first_name"], " ", entry["last_name"]
    print entry["title"]
    print entry["teacher"]
