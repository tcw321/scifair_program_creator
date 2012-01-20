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
worddoc.PageSetup.BottomMargin = 36
worddoc.PageSetup.LeftMargin = 36
worddoc.PageSetup.RightMargin = 40
worddoc.PageSetup.TopMargin = 40
worddoc.Content.Font.Size = 8
worddoc.Content.Font.Name = "Comic Sans MS"

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
        table.Rows(1).HeadingFormat = True
#        table.AutoFormat(16)
	table.Rows.AllowBreakAcrossPages = False
        title = ' '.join(teacher)
        table.Rows(1).Cells.Merge()
        table.Cell(1,1).Range.InsertAfter(title)
	table.Cell(1,1).Range.Font.Bold = True
	table.Cell(1,1).Range.Font.Size = 10
        row = 1
        for entry in projects:
            row += 1
	    table.Cell(row,1).LeftPadding = 16
            name = entry["first_name"]+" "+entry["last_name"]
            if "first_name1" in entry:
                name += "\n" + entry["first_name1"]+" "+entry["last_name1"]
            if "first_name2" in entry:
                name += "\n" + entry["first_name2"]+" "+entry["last_name2"]
            if "first_name3" in entry:
                name += "\n" + entry["first_name3"]+" "+entry["last_name3"]
            table.Cell(row,1).Range.InsertAfter(name)
	    table.Cell(row,1).Range.Paragraphs.SpaceAfter = 0
	    table.Cell(row,1).TopPadding = 2
	    table.Cell(row,1).BottomPadding = 2
            table.Cell(row,2).Range.InsertAfter(entry["title"])
	    table.Cell(row,2).Range.Paragraphs.SpaceAfter = 0

worddoc.Range.Paragraphs.WidowControl = True
worddoc.Content.MoveEnd
worddoc.Close() # Close the Word Document (a save-Dialog pops up)
wordapp.Quit() # Close the Word Applicati
