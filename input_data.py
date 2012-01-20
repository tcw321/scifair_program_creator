import pymongo

from pymongo import Connection
connection = Connection()

db = connection.science_fair
entries = db.entries

more = "Y"
while (more == "Y"):
    first_name = raw_input("Enter first name:")
    last_name = raw_input("Enter last name:")
    project = raw_input("Enter project:")
    teacher = raw_input("Enter teacher:")
    electrical = raw_input("Electrical Y/N:")
    other = raw_input("Other:")
    more = raw_input("Input Another? Y/N:")
    entry = {"first_name": first_name,
             "last_name": last_name,
             "title": project,
             "teacher": teacher,
             "electrical": electrical,
             "other": other}
    entries.insert(entry)

