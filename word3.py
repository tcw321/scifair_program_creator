import win32com.client
import pymongo

from pymongo import Connection
connection = Connection()

db = connection.science_fair
entries = db.entries


wordapp = win32com.client.Dispatch("Word.Application") # Create new Word Object
wordapp.Visible = 1 # Word Application should`t be visible
worddoc = wordapp.Documents.Add() # Create new Document Object
worddoc.PageSetup.Orientation = 1 # Make some Setup to the Document:
worddoc.PageSetup.BookFoldPrinting = 1 # Make some Setup to the Document:
#worddoc.Content.Font.Size = 11
#worddoc.Content.Paragraphs.TabStops.Add (100)
#worddoc.Content.Text = "Hello, I am a text!"

key = raw_input("Find key:")
value = raw_input("Find value:")

while (key != ""):

    location = worddoc.Range()
    location.Paragraphs.Add()
    location.Collapse(0)
    projects = entries.find({ key: value});
    projects.sort("last_name", pymongo.ASCENDING)
    table = location.Tables.Add (location, projects.count()+1,2)
    table.ApplyStyleHeadingRows = 1
    table.AutoFormat(16)
    table.Cell(1,1).Range.InsertAfter(value)
    row = 1
    for entry in projects:
        row += 1
        name = entry["first_name"]+" "+entry["last_name"]
        table.Cell(row,1).Range.InsertAfter(name)
        table.Cell(row,2).Range.InsertAfter(entry["title"])

    key = raw_input("Find key:")
    value = raw_input("Find value:")

location1 = worddoc.Range()
location1.Paragraphs.Add()
location1.Collapse(0)
table = worddoc.Tables.Add (location1, 3, 4)
table.ApplyStyleHeadingRows = 1
table.AutoFormat(16)
table.Cell(1,1).Range.InsertAfter("Teacher1")

location1 = worddoc.Range()
location1.Paragraphs.Add()
location1.Collapse(0)
table = worddoc.Tables.Add (location1, 3, 4)
table.ApplyStyleHeadingRows = 1
table.AutoFormat(16)
table.Cell(1,1).Range.InsertAfter("Teacher2")

worddoc.Content.MoveEnd
worddoc.Close() # Close the Word Document (a save-Dialog pops up)
wordapp.Quit() # Close the Word Application
