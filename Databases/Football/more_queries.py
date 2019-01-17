#!/usr/bin/python
print 'Content-type: text/html\n\n'

import cgi
import cgitb; cgitb.enable()
import sqlite3
from DB_Functions import *

mydb = 'football.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print '''
<html>
<head>
</head>
<body>
'''
print 'All the players from Yanchep:<br />'
cursor.execute('''SELECT * FROM Players
			    WHERE suburb = "Yanchep"''')
records = cursor.fetchall()
print_Records(records)

print '<hr />'
print 'The number of players from Yanchep:<br />'
cursor.execute('''SELECT suburb, COUNT(registration) FROM Players
			    WHERE suburb = "Yanchep"
			    GROUP BY suburb''')
records = cursor.fetchall()
fields = ["suburb", "count"]
print_Records(records, fields)

print '<hr />'
print 'The total number of goals that each player has kicked for the season:<br />'
cursor.execute('''SELECT Players.registration as rego, first_name, last_name, SUM(goals) as games
			    FROM Players, Games
			    WHERE Players.registration = Games.registration
			    GROUP BY rego
			    ORDER BY games DESC
			    LIMIT 10''')
records = cursor.fetchall()
fields = ["registration", "first_name", "last_name", "total goals"]
print_Records(records, fields)

print '<hr />'
print 'The total number of games that each player has played throughout the season:<br />'
cursor.execute('''SELECT Players.registration as rego, first_name, last_name, COUNT(goals) as games
			    FROM Players, Games
			    WHERE Players.registration = Games.registration
			    GROUP BY rego
			    ORDER BY games DESC
			    LIMIT 10''')
records = cursor.fetchall()
fields = ["registration", "first_name", "last_name", "total games"]
print_Records(records, fields)

print '''
</body>
</html>
'''
conn.commit()
cursor.close()
