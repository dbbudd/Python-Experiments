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
starts_with = form.getvalue('starts_with')
values = { "starts_with": starts_with + '%' }

print "<h1>Players who's surname starts with " + starts_with + '</h1>'

cursor.execute('''SELECT COUNT(last_name) FROM Players
			    WHERE last_name LIKE :starts_with''', values)

records = cursor.fetchall()

if len(records) == 0:
    print 'There are no players with a last name starting with ' + starts_with
else:
    print 'There are ' + str(records[0][0]) + ' players with a name starting with ' + starts_with
print '<br /><br />'


print 'The players are:<br />'

cursor.execute('''SELECT registration, last_name, first_name
		    FROM Players
		    WHERE last_name LIKE :starts_with''', values)
fields = ["Registration", "Last Name", "First Name"]
records = cursor.fetchall()
print_Records(records, fields)

print '<hr>'
print 'This next query is hard coded'
print "<h1>Players who's surname end with 'on'</h1>"

cursor.execute('''SELECT COUNT(last_name) FROM Players
			    WHERE last_name LIKE "%on"''')

records = cursor.fetchall()

if len(records) == 0:
    print "There are no players with a last name ending with 'on'"
else:
    print 'There are ' + str(records[0][0]) + " players with a name ending with 'on'"
print '<br /><br />'

print 'The players are:<br />'

cursor.execute('''SELECT registration, last_name, first_name
		    FROM Players
		    WHERE last_name LIKE "%on"''')
fields = ["Registration", "Last Name", "First Name"]
records = cursor.fetchall()
print_Records(records, fields)


conn.commit()
cursor.close()
