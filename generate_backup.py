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

teachers = [["Heidi", "Hargesheimer", "(K)", "Turquoise"],
            ["Edie", "Linton", "(1-2)", "Red"],
            ["Jamie", "Martin", "(1-2)", "Pink with Green Swirls"],
            ["Josh", "Tumolo", "(1-2)", ""],
            ["Maggi", "Idzikowski", "(1-2)", ""],
            ["Tyra", "Johnston", "(1-2)", "Orange"],
            ["Tracey", "Metry", "(1-2)", "Green"],
            ["Denise", "Chacon-Lontin", "(3-4)", "Green"],
            ["Chad", "Downs", "(3-4)", "Hot Pink"],
            ["Bette", "Diem", "(3-4)", "Brown"],
            ["Carl", "Clark", "(3-4)", "Navy Blue"],
            ["Rick", "Hall", "(5-6)", "Blue with Purple Dots"],
            ["Ko", "Shih", "(5-6)", "Yellow with Stripes"],
            ["Mike", "Derhammer", "(5-6)", "Tan with Blue Dots"],
            ["Leslie", "Lawther", "(5-6)", "Gold with Red Dots"],
            ["Adam", "Samples", "(7-8)", "Purple"],
            ["Aina", "Bernier", "(7-8)", "Purple"],
            ["Mary", "Wigton", "(7-8)", "Purple"]]

for teacher in teachers:
        location = worddoc.Range()
        location.Paragraphs.Add()
        location.Collapse(0)
        projects = entries.find({ "teacher": teacher[0]});
        projects.sort("last_name", pymongo.ASCENDING)
        table = location.Tables.Add (location, projects.count()+1,2)
        table.ApplyStyleHeadingRows = 1
        table.AutoFormat(16)
        title = ''.join(teacher)
        table.Rows(1).Cells.Merge
        table.Cell(1,1).Range.InsertAfter(title)
        row = 1
        for entry in projects:
            row += 1
            name = entry["first_name"]+" "+entry["last_name"] +"\n"
            if "first_name1" in entry:
                name += entry["first_name1"]+" "+entry["last_name1"] +"\n"
            if "first_name2" in entry:
                name += entry["first_name2"]+" "+entry["last_name2"] +"\n"
            if "first_name3" in entry:
                name += entry["first_name3"]+" "+entry["last_name3"] +"\n"            
            table.Cell(row,1).Range.InsertAfter(name)
            table.Cell(row,2).Range.InsertAfter(entry["title"])



worddoc.Content.MoveEnd
worddoc.Close() # Close the Word Document (a save-Dialog pops up)
wordapp.Quit() # Close the Word Applicati
