import win32com.client
 
wordapp = win32com.client.Dispatch("Excel.Application") # Create new Word Object
wordapp.Visible = 1 # Word Application should`t be visible

name = raw_input("Enter : ")
