#!/usr/bin/python
print 'Content-type: text/html'
print

import cgi
import cgitb; cgitb.enable()
import sqlite3
from DB_Functions import *

mydb = 'football.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

form = cgi.FieldStorage()
suburb = form.getvalue('suburb')
values = { "suburb": suburb }

print '<h1>Players from ' + suburb + '</h1>'
cursor.execute('''SELECT suburb, COUNT(registration) FROM Players
			    WHERE suburb = :suburb
			    GROUP BY suburb''', values)

records = cursor.fetchall()
if len(records) == 0:
    print 'There are no players from ' + suburb
else:
    print 'There are ' + str(records[0][1]) + ' players from ' + records[0][0]
print '<br /><br />'
print 'The players from ' + suburb + ' are:<br />'

cursor.execute('''SELECT registration, last_name, first_name
		    FROM Players
		    WHERE suburb = :suburb''', values)
fields = ["Registration", "Last Name", "First Name"]
records = cursor.fetchall()
print_Records(records)

conn.commit()
cursor.close()
