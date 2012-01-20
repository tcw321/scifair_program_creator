
import pymongo

from pymongo import Connection
connection = Connection()

db = connection.science_fair
entries = db.entries

print "Char Hanchak"
for entry in entries.find({"teacher":"Char"}):
    print entry["first_name"],  entry["last_name"]

print "\n"
print "Heidi Hargesheimer"
for entry in entries.find({"teacher":"Heidi"}):
    print entry["first_name"],  entry["last_name"]

print "\n"
print "Edie Linton"
for entry in entries.find({"teacher":"Edie"}):
    print entry["first_name"],  entry["last_name"]

print "\n"
print "Jamie Martin"
for entry in entries.find({"teacher":"Jamie"}):
    print entry["first_name"],  entry["last_name"]

print "\n"
print "Josh Tumolo"
for entry in entries.find({"teacher":"Josh"}):
    print entry["first_name"],  entry["last_name"]

print "\n"
print "Maggi Idzikowski"
for entry in entries.find({"teacher":"Maggi"}):
    print entry["first_name"],  entry["last_name"]

print "\n"
print "Tracey Metry"
for entry in entries.find({"teacher":"Tracey"}):
    print entry["first_name"],  entry["last_name"]

print "\n"
print "Tyra Johnston"
for entry in entries.find({"teacher":"Tyra"}):
    print entry["first_name"],  entry["last_name"]

print "\n"
print "Bette Gobeille Diem"
for entry in entries.find({"teacher":"Bette"}):
    print entry["first_name"],  entry["last_name"]

print "\n"
print "Carl Clark"
for entry in entries.find({"teacher":"Carl"}):
    print entry["first_name"],  entry["last_name"]

print "\n"
print "Chad Downs"
for entry in entries.find({"teacher":"Chad"}):
    print entry["first_name"],  entry["last_name"]

print "\n"
print "Denise Chacon Lontin"
for entry in entries.find({"teacher":"Denise"}):
    print entry["first_name"],  entry["last_name"]

print "\n"
print "Ko Shih"
for entry in entries.find({"teacher":"Ko"}):
    print entry["first_name"],  entry["last_name"]

print "\n"
print "Leslie Lawther"
for entry in entries.find({"teacher":"Leslie"}):
    print entry["first_name"],  entry["last_name"]

print "\n"
print "Mike Derhammer"
for entry in entries.find({"teacher":"Mike"}):
    print entry["first_name"],  entry["last_name"]

print "\n"
print "Rick Hall"
for entry in entries.find({"teacher":"Rick"}):
    print entry["first_name"],  entry["last_name"]

print "\n"
print "Adam Samples"
for entry in entries.find({"teacher":"Adam"}):
    print entry["first_name"],  entry["last_name"]

print "\n"
print "Aina Bernier"
for entry in entries.find({"teacher":"Aina"}):
    print entry["first_name"],  entry["last_name"]

print "\n"
print "Mary Wigton"
for entry in entries.find({"teacher":"Mary"}):
    print entry["first_name"],  entry["last_name"]

print "\n"
print "Peter Ways"
for entry in entries.find({"teacher":"Peter"}):
    print entry["first_name"],  entry["last_name"]

