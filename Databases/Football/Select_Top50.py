#!/usr/bin/python
print 'Content-type: text/html\n\n'

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'football.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

def print_Records(records):
# Print out all the records that have been found in an HTML table
    if len(records) > 0:
	print '<table style="border: 1px solid black; border-collapse: collapse;">'
	for record in records:
	    print '<tr>'
	    for field in record:
	        print'<td style="border: 1px solid black;">' + str(field) + '</td>'
	    print '</tr>'
	print '</table>'                         
    else:
	print 'No records found'

print '''
<html>
<head>
</head>
<body>
'''
print 'The teams are:<br />'
cursor.execute('''SELECT * FROM Teams''')
records = cursor.fetchall()
print_Records(records)
#for record in cursor.fetchall():
#    print record
#    print '<br />'

print '<br />++++++++++<br /><br />'
print 'The first 50 players are:<br />'
cursor.execute('''SELECT * FROM Players LIMIT 50''')
records = cursor.fetchall()
print_Records(records)
#for record in cursor.fetchall():
#    print record
#    print '<br />'

print '<br />++++++++++<br /><br />'
print 'The first 50 games are:<br />'
cursor.execute('''SELECT * FROM Games LIMIT 50''')
records = cursor.fetchall()
print_Records(records)
#for record in cursor.fetchall():
#    print record
#    print '<br />'

print '''
</body>
</html>
'''
conn.commit()
cursor.close()
