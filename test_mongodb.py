import pymongo

from pymongo import Connection
connection = Connection()

db = connection.test_database
print db.posts.find_one()



