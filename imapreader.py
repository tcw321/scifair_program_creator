import getpass, imaplib

outfile = open('output_all.txt', mode='w')
M = imaplib.IMAP4('mail.tcw321.com')
user = 'kjgotts+tcw321.com'
pss = getpass.getpass()
print 'user', user
M.login(user, pss)
M.select()
typ, data = M.search(None, 'ALL')
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    temp = 'Number: ', num
    outfile.writelines( temp )
    outfile.writelines( data[0][1] )
#code, mailboxen = M.list()
#print mailboxen
#M.close()
#M.logout()
