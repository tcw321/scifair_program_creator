import pymongo

from pymongo import Connection
connection = Connection()

db = connection.science_fair
entries = db.entries

more = raw_input("Input Another? Y/N")
if (more == "Y"):
    next = 1
else:
    next = 0


while (next == 1):
    entry = {}
    entry['first_name'] = raw_input("First Name:")
    entry['last_name'] = raw_input("Last Name:")
    count = 1
    while ('Y' == raw_input("More names?Y/N: ")):
        entry['first_name'+format(count)] = raw_input("First Name:")
        entry['last_name'+format(count)] = raw_input("Last Name:")
    entry['teacher'] = raw_input("Teacher:")
    entry['title'] = raw_input("Title:")
    entry['electrical'] = raw_input("Electrical Y/N:")
    entry['other'] = raw_input("Other:")
    
    entries.insert(entry)
    more = raw_input("Input Another? Y/N")
    if (more == "Y"):
        next = 1
    else:
        next = 0

key = raw_input("Find key:")
value = raw_input("Find value:")

projects = entries.find({ key: value})
projects.sort("last_name", pymongo.ASCENDING)

for entry in entries.find({ key: value}):
    print 'First Name:', entry["first_name"]
    print 'Last Name:', entry["last_name"]
    if "first_name1" in entry:
        print 'First Name1:', entry["first_name1"]
        print 'Last Name1:', entry["last_name1"]
    if "first_name2" in entry:
        print 'First Name2:', entry["first_name2"]
    if "last_name2" in entry:        
        print 'Last Name2:', entry["last_name2"]
    if "first_name3" in entry:
        print 'First Name3:', entry["first_name3"]
        print 'Last Name3:', entry["last_name3"]        
    print 'Teacher:', entry["teacher"]
    print 'Project:', entry["title"]
    print 'Electrical:', entry["electrical"]
    print 'Other:', entry["other"]
    more_edits = True
    while (more_edits):
        if raw_input("Edit? Y/N:") == 'Y':
            key = raw_input("Key: first_name, last_name, teacher, title, electrical, other: ")
            entry[key] = raw_input("New value: ")
            entries.save(entry)
        more_edits = False
        if raw_input("More edits?") == "Y":
            more_edits = True
        
#handle optional fields






