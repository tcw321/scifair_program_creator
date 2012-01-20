import win32con
import winerror
import win32clipboard
import re
import decimal
import Tkinter
import sys

newdata = []
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)

data = ''.join(data)
redollar  = re.compile(r'[^0-9.]+')
data = redollar.sub(' ',data)

data2 = data.split()

sum = decimal.Decimal('0.0')
for item in data2:
  sum = sum + decimal.Decimal(item)

output = 'Sum = %6.2f' % sum

Tkinter.Label(text=output).pack()
Tkinter.Button(text='Exit', command=sys.exit).pack()
Tkinter.mainloop()


