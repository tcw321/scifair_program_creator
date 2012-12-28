#
# script used for Science Fair 2011 using mongodb
#

import win32com.client
from projects import Entries
from read_csv import read_csv

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
worddoc.Content.Paragraphs.WidowControl = True

teachers = [["Heidi", "Hargesheimer", "(K)", "  Pink with Green Swirls"],
	    ["Char", "Hanchak", "(K)", "  Pink"],
            ["Maggi", "Idzikowski", "(K)", "  Yellow with Stripes"],
            ["Tyra", "Johnston", "(1-2)", "  Orange"],
            ["Edie", "Linton", "(1-2)", "  Red"],
            ["Jamie", "Martin", "(1-2)", "  Turquoise"],
            ["Tracey", "Metry", "(1-2)", "  Green"],
            ["Josh", "Tumolo", "(2-3)", "  Yellow"],
            ["Denise", "Chacon-Lontin", "(3-4)", "  Red with Orange Stars"],
            ["Carl", "Clark", "(3-4)", "  Green"],
            ["Bette", "Gobeille-Diem", "(3-4)", "  Brown"],
            ["Chad", "Downs", "(3-4)", "  Hot Pink"],
            ["Mike", "Derhammer", "(5-6)", "  Tan with Blue Dots"],
            ["Rick", "Hall", "(5-6)", "  Blue with Purple Dots"],
            ["Leslie", "Lawther", "(5-6)", "  Gold with Red Dots"],
            ["Ko", "Shih", "(5-6)", "  Blue with Pink Dots"],
            ["Aina", "Bernier", "(7-8)", "  Purple"],
            ["Adam", "Samples", "(7-8)", "  Purple"],
            ["Peter", "Ways", "(7-8)", "  Purple"],
            ["Mary", "Wigton", "(7-8)", "  Purple"]]

entries = Entries()
entries.values = read_csv("Ann Arbor Open Science Fair Entry Form - Sheet1 (5).csv")

count = 0
for teacher in teachers:
        location = worddoc.Range()
	    location.Paragraphs.Add()
        location.Collapse(0)
        projects = entries.find({ "Teacher": teacher[0]})   ######
	    if 'last_name' in projects[0]:
          projects = sorted(projects, key=lambda k: k['last_name'])  #*****
        table = location.Tables.Add (location, len(projects)+1,2)
        table.Rows(1).HeadingFormat = True
#        table.AutoFormat(16)
	    table.Rows.AllowBreakAcrossPages = False
        title = ' '.join(teacher)
        table.Rows(1).Cells.Merge()
        table.Cell(1,1).Range.InsertAfter(title)
	    table.Cell(1,1).Range.Font.Bold = True
	    table.Cell(1,1).Range.Font.Size = 10
        row = 1
        for entry in projects:  ##########
            count += 1
            row += 1
	        table.Cell(row,1).LeftPadding = 16
	        if row%2 == 0:
	          table.Rows(row).Shading.BackgroundPatternColorIndex = 16
              name = entry["first_name"]+" "+entry["last_name"]    #########
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


print "count ", count
worddoc.Content.MoveEnd
worddoc.Close() # Close the Word Document (a save-Dialog pops up)
wordapp.Quit() # Close the Word Applicati
