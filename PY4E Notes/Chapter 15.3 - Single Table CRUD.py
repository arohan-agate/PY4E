# SQL Insert
# The Insert statement inserts a row into a table
# INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu')

# SQL Delete
# Deletes a row in a table based on a selection criteria
# DELETE FROM Users WHERE email='fred@umich.edu'

# SQL Update
# Allows the updating of a field with a WHERE clause
# UPDATE Users SET name='Charles' WHERE email='csev@umich.edu'

# Retrieving Records: Select
# The select statement retrieves a group of records - you can either retrieve all the records or a subset of the records
# with a WHERE clause SELECT * FROM Users - Selects all the rows and columns
# SELECT * FROM Users WHERE email='csev@umich.edu - Selects the rows and columns when the WHERE applies'

# Sorting with ORDER BY
# You can add an ORDER BY clause to SELECT statements to get the results sorted in ascending or descending order
# SELECT * FROM Users ORDER BY name

import sqlite3  # need to import the sqlite3 library

conn = sqlite3.connect('emaildb.sqlite')  # make a connection to the database
cur = conn.cursor()  # similar to a handle. SQL commands are sent through cur, responses come back through cur

cur.execute('DROP TABLE IF EXISTS Counts')  # drops the table if the file already exists

cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')  # creates a table, similar to a dictionary

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):  # finds the line that has the email
        continue
    pieces = line.split()
    email = pieces[1]  # grabs the email address. in the from line, the email address is the second part, index 1
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))  # the one tuple with the email will replace the ?
    row = cur.fetchone()  # row will hold the information from the database
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))  # inserts a new value into the table if it has not been seen, has count of 1
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))  # if the row exists, updates the count with count + 1
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()