#
# script used for Science Fair 2011 using mongodb
#

import win32com.client
from read_tab_delimited_file import generateEntries

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
	    ["Edie", "Linton", "(K)", "  Pink"],
            ["Diane", "VanDorn", "(K)", "  Yellow with Stripes"],
            ["Tyra", "Johnston", "(1-2)", "  Orange"],
            ["Jennifer", "Thomas", "(1-2)", "  Red"],
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

spreadsheet = open("2015testform1.tsv", 'r')
entries = generateEntries(spreadsheet.readlines())

count = 0
for teacher in teachers:
        location = worddoc.Range()
        location.Paragraphs.Add()
        location.Collapse(0)
        projects = entries[teacher[0]]   ######
        if projects == {}:
            continue
        #if 'last_name' in projects[0]:
        #  projects = sorted(projects, key=lambda k: k['last_name'])  #*****
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
            #table.Cell(row,1).LeftPadding = 16
            table.Rows(row).Borders.OutsideLineStyle = True
            table.Rows(row).Borders.OutsideLineWidth = 8
            name = entry[1][0][0]+" "+entry[1][0][1]    #########
            if len(entry[1]) > 2 and entry[1][1][0] != "":
                name += "\n" + entry[1][1][0]+" "+entry[1][1][1]
            if len(entry[1]) > 3 and entry[1][2][0] != "":
                name += "\n" + entry[1][2][0]+" "+entry[1][2][1]
            if len(entry[1]) > 4 and entry[1][3][0] != "":
                name += "\n" + entry[1][3][0]+" "+entry[1][3][1]
            table.Cell(row,1).Range.InsertAfter(name)
            table.Cell(row,1).Range.Paragraphs.SpaceAfter = 0
            table.Cell(row,1).TopPadding = 2
            table.Cell(row,1).BottomPadding = 2
            table.Cell(row,2).Range.InsertAfter(entry[0])
            table.Cell(row,2).Range.Paragraphs.SpaceAfter = 0
            table.Cell(row,2).TopPadding = 2
            table.Cell(row,2).BottomPadding = 2


print("count ", count)
worddoc.Content.MoveEnd
worddoc.Close() # Close the Word Document (a save-Dialog pops up)
wordapp.Quit() # Close the Word Applicati
