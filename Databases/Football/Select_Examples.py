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

cursor.execute('''SELECT suburb FROM Players
			    GROUP BY suburb
			    ORDER BY suburb''')

records = cursor.fetchall()
#fields = ["Registration", "Last Name", "First Name"]
print_Records(records)

conn.commit()
cursor.close()
