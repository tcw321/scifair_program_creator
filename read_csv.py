import sys
#
# To Do - not working to add all the information to entries, only first entry, only entry with 14 tokens
#

def read_csv(names):
    csvfile = open(names, 'r')
    csvlines = csvfile.readlines()
    headers = csvlines[0].split(',')
    headers[-1] = headers[-1].rstrip()
    entries = {}
    for header in headers:
        entries[header] = []
    for nextline in csvlines[1:]:
        entry = nextline.split(',')
    if len(entry) > 1:
        for col in range(len(entry)):
            entries[headers[col]].append(entry[col])
        for col in range(len(entry), len(headers)):
            empty_string = ''
            entries[headers[col]].append(empty_string)
    return entries
    
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:  read_csv.py filename')
    else:
        t = read_csv(sys.argv[1])
        print(t['Teacher'])
