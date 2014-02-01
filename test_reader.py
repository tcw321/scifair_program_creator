__author__ = 'Timothy'

spreadsheet = open("sat2014b.csv", 'r')
data = spreadsheet.readlines()[1:]

results = []
for line in data:
    elements = line.split(',')
    name = elements[2].strip() + ',' + elements[1]
    results.append(name)

results.sort();
for line in results:
    print line

results = []
print "*************************************************"
for line in data:
   elements = line.split(',')
   name = elements[4].strip() + ',' + elements[3]+','+elements[17]
   results.append(name)

for line in results:
    print line








