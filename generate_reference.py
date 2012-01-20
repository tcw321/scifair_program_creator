import win32com.client
import pymongo

from pymongo import Connection
connection = Connection()

db = connection.science_fair
entries = db.entries


wordapp = win32com.client.Dispatch("Word.Application") # Create new Word Object
wordapp.Visible = 1 # Word Application should`t be visible
worddoc = wordapp.Documents.Add() # Create new Document Object
#worddoc.PageSetup.Orientation = 1 # Make some Setup to the Document:
#worddoc.PageSetup.BookFoldPrinting = 1 # Make some Setup to the Document:
#worddoc.PageSetup.BottomMargin = 36
#worddoc.PageSetup.LeftMargin = 36
#worddoc.PageSetup.RightMargin = 40
#worddoc.PageSetup.TopMargin = 40
worddoc.Content.Font.Size = 8
worddoc.Content.Font.Name = "Comic Sans MS"
worddoc.Content.Paragraphs.WidowControl = True

teachers = [["Heidi", "Hargesheimer", "(K)", "  Turquoise"],
            ["Maggi", "Idzikowski", "(1-2)", "  Blue with Pink Dots"],
            ["Tyra", "Johnston", "(1-2)", "  Orange"],
            ["Edie", "Linton", "(1-2)", "  Red"],
            ["Jamie", "Martin", "(1-2)", "  Pink with Green Swirls"],
            ["Tracey", "Metry", "(1-2)", "  Green"],
            ["Josh", "Tumolo", "(1-2)", "  Yellow"],
            ["Denise", "Chacon-Lontin", "(3-4)", "  Red with Orange Stars"],
            ["Carl", "Clark", "(3-4)", "  Navy Blue"],
            ["Bette", "Diem", "(3-4)", "  Brown"],
            ["Chad", "Downs", "(3-4)", "  Hot Pink"],
            ["Mike", "Derhammer", "(5-6)", "  Tan with Blue Dots"],
            ["Rick", "Hall", "(5-6)", "  Blue with Purple Dots"],
            ["Leslie", "Lawther", "(5-6)", "  Gold with Red Dots"],
            ["Ko", "Shih", "(5-6)", "  Yellow with Stripes"],
            ["Aina", "Bernier", "(7-8)", "  Purple"],
            ["Adam", "Samples", "(7-8)", "  Purple"],
            ["Peter", "Ways", "(7-8)", "  Purple"],
            ["Mary", "Wigton", "(7-8)", "  Purple"]]


for teacher in teachers:
        location = worddoc.Range()
	location.Paragraphs.Add()
        location.Collapse(0)
        projects = entries.find({ "teacher": teacher[0]});
        projects.sort("last_name", pymongo.ASCENDING)
        table = location.Tables.Add (location, projects.count()+1,4)
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
	    if row%2 == 0:
	        table.Rows(row).Shading.BackgroundPatternColorIndex = 16    
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
	    table.Cell(row,3).Range.InsertAfter(entry["other"])
	    table.Cell(row,4).Range.InsertAfter(entry["electrical"])


worddoc.Content.MoveEnd
worddoc.Close() # Close the Word Document (a save-Dialog pops up)
wordapp.Quit() # Close the Word Applicati
