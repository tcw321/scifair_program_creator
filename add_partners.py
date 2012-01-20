import pymongo

from pymongo import Connection
connection = Connection()

db = connection.science_fair
entries = db.entries


key = raw_input("Find key:")
value = raw_input("Find value:")

projects = entries.find({ key: value})
projects.sort("last_name", pymongo.ASCENDING)

list_of_entries = []
for entry in entries.find({ key: value}):
    list_of_entries.append(entry)
    print 'First Name:', entry["first_name"]
    print 'Last Name:', entry["last_name"]
    if "first_name1" in entry:
        print 'First Name1:', entry["first_name1"]
        print 'Last Name1:', entry["last_name1"]
    if "first_name2" in entry:
        print 'First Name2:', entry["first_name2"]
        print 'Last Name2:', entry["last_name2"]
    if "first_name3" in entry:
        print 'First Name3:', entry["first_name3"]
        print 'Last Name3:', entry["last_name3"]        
    print 'Teacher:', entry["teacher"]
    print 'Project:', entry["title"]
    print 'Electrical:', entry["electrical"]
    print 'Other:', entry["other"]

    if raw_input("New Partner? Y/N:") == 'Y':
        entry["first_name1"] = raw_input("first_name1: ")
        entry["last_name1"] = raw_input("last_name1: ")
        entries.save(entry)

    if raw_input("New Partner? Y/N:") == 'Y':
        entry["first_name2"] = raw_input("first_name2: ")
        entry["last_name2"] = raw_input("last_name2: ")
        entries.save(entry)

    if raw_input("New Partner? Y/N:") == 'Y':
        entry["first_name3"] = raw_input("first_name3: ")
        entry["last_name3"] = raw_input("last_name3: ")
        entries.save(entry)        

        
#handle optional fields






