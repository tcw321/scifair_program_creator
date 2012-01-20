
import pymongo

from pymongo import Connection
connection = Connection()

db = connection.science_fair
entries = db.entries


key = raw_input("Find key:")

for entry in entries.find({ key: value}):
    print 'First Name:    ', entry["first_name"]
    print 'Last Name:     ', entry["last_name"]
    if "first_name1" in entry:
        print 'First Name1:   ', entry["first_name1"]
        print 'Last Name1:    ', entry["last_name1"]
    if "first_name2" in entry:
        print 'First Name2:   ', entry["first_name2"]
        print 'Last Name2:    ', entry["last_name2"]
    if "first_name3" in entry:
        print 'First Name3:   ', entry["first_name3"]
        print 'Last Name3:    ', entry["last_name3"]        
    print 'Teacher:       ', entry["teacher"]
    print 'Project:       ', entry["title"]
    print 'Electrical:    ', entry["electrical"]
    while raw_input("Edit? Y/N:") == 'Y':
        key = raw_input("Key:")
        entry[key] = raw_input("New value: ")
        entries.save(entry)
#handle optional fields






