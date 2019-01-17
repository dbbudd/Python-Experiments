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
registration = form.getvalue('registration')
values = { "rego": registration }

cursor.execute('''SELECT registration,
			 first_name,
			 last_name
		    FROM Players
		    WHERE registration = :rego''', values)

records = cursor.fetchall()
if len(records) == 0:
    print '<h1>Player with registration number ' + registration + ' not found</h1>'
elif len(records) > 1:
    print '<h1>Error: More than one player with number ' + registration + ' found</h1>'
else:
    print '<h1>Season Statistics for ' + records[0][1] + ' ' + records[0][2] + '</h1>'
    print 'Registration number: ' + str(records[0][0])
    

cursor.execute('''SELECT COUNT(*)
		    FROM Players, Games
		    WHERE Players.registration = Games.registration
		      AND Players.registration = :rego''', values)
records = cursor.fetchall()
if len(records) == 0:
    print '<h3>No games played this year</h3>'
else:
    print '<h3>Total Games for Season = ' + str(records[0][0]) + '</h3>'

print '<h3>Games for Season</h3>'
cursor.execute('''SELECT round,
			 position,
			 kicks,
			 handballs,
			 marks,
			 goals,
			 behinds,
			 Teams.name as TeamName
		    FROM Players, Games, Teams
		    WHERE Players.registration = Games.registration
		      AND Games.team_id = Teams.team_id
		      AND Players.registration = :rego
		    ORDER BY round''', values)
fields = ["Round", "Position", "Kicks", "Handballs", "Marks", "Behinds", "Goals", "Team"]
records = cursor.fetchall()
print_Records(records, fields)

print '<h3>Totals for Season</h3>'
cursor.execute('''SELECT SUM(kicks),
			 SUM(handballs),
			 SUM(marks),
			 SUM(goals),
			 SUM(behinds)
		    FROM Players, Games
		    WHERE Players.registration = Games.registration
		      AND Players.registration = :rego
		    GROUP BY Players.registration''', values)
fields = ["Kicks", "Handballs", "Marks", "Behinds", "Goals"]
records = cursor.fetchall()
print_Records(records, fields)

print '<h3>Averages per game</h3>'
cursor.execute('''SELECT AVG(kicks),
			 AVG(handballs),
			 AVG(marks),
			 AVG(goals),
			 AVG(behinds)
		    FROM Players, Games, Teams
		    WHERE Players.registration = Games.registration
		      AND Games.team_id = Teams.team_id
		      AND Players.registration = :rego
		    GROUP BY Players.registration''', values)
fields = ["Kicks", "Handballs", "Marks", "Behinds", "Goals"]
records = cursor.fetchall()
print_Records(records, fields)

print '<h3>Points for the Season</h3>'
cursor.execute('''SELECT SUM(goals) as tot_goals,
			 SUM(behinds) as tot_behinds,
			 SUM(goals) * 6 + SUM(behinds) as points
		    FROM Players, Games, Teams
		    WHERE Players.registration = Games.registration
		      AND Games.team_id = Teams.team_id
		      AND Players.registration = :rego
		    GROUP BY Players.registration''', values)
fields = ["Goals", "Behinds", "Points"]
records = cursor.fetchall()
print_Records(records, fields)

print '<h3>Games for Season</h3>'
cursor.execute('''SELECT round,
			 position,
			 kicks,
			 handballs,
			 marks,
			 goals,
			 behinds,
			 CASE
			    WHEN goals = 0 THEN 'No Goals'
			    WHEN goals < 5 THEN 'Some Goals'
			    WHEN goals >= 5 THEN 'Lots of Goals'
			 END as SomeGoals,
			 Teams.name as TeamName
		    FROM Players, Games, Teams
		    WHERE Players.registration = Games.registration
		      AND Games.team_id = Teams.team_id
		      AND Players.registration = :rego
		    ORDER BY round''', values)
fields = ["Round", "Position", "Kicks", "Handballs", "Marks", "Behinds", "Goals", "Some Goals", "Team"]
records = cursor.fetchall()
print_Records(records, fields)

conn.commit()
cursor.close()
