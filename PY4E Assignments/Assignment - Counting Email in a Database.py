import sqlite3  # need to import the sqlite3 library

conn = sqlite3.connect('countorgs.sqlite')  # make a connection to the database
cur = conn.cursor()  # similar to a handle. SQL commands are sent through cur, responses come back through cur

cur.execute('DROP TABLE IF EXISTS Counts')  # drops the table if the file already exists

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')  # creates a table, similar to a dictionary

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'
fh = open(fname)
lst = []
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    dom = email.find('@')
    org = email[dom+1:len(email)]

    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))  # the one tuple with the domain will replace the ?
    row = cur.fetchone()  # row will hold the information from the database
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))  # inserts a new value into the table if it has not been seen, has count of 1
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))  # if the row exists, updates the count with count + 1
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()