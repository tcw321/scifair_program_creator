import pymongo

from pymongo import Connection
connection = Connection()

db = connection.science_fair
entries = db.entries

print entries.find_one()
