#!/usr/bin/python
print "Content-type: text/html; charset=utf-8"
print

import cgi
import os
import sqlite3
import sys, os, contextlib



form = cgi.FieldStorage()
val_Table = str(form.getvalue('Choose_Table'))
frm_Search = str(form.getvalue('Search_Query'))
val_Search = "'" + frm_Search + "'"

#create a database connection
db = sqlite3.connect('pokemon.db')
db.row_factory = sqlite3.Row

import template

template.my_header()

print("""
      <h1>Search Results</h1>
      """)
if val_Table == "Locations":
    my_data = db.execute("""
                         SELECT * FROM Locations
                         WHERE Region_ID LIKE {search}
                         OR Region LIKE {search}
                         OR Capital LIKE {search}
                         OR Biome LIKE {search}
                         ORDER BY Region_ID
                         """.format(search = val_Search))
    
elif val_Table == "Pokedex":
    my_data = db.execute("""
                         SELECT * FROM Pokedex
                         WHERE Pokedex_ID LIKE {search}
                         OR Species LIKE {search}
                         OR Type LIKE {search}
                         OR Attack LIKE {search}
                         OR Defense LIKE {search}
                         OR Spec_Attack LIKE {search}
                         OR Spec_Defense LIKE {search}
                         OR XP LIKE {search}
                         OR Health LIKE {search}
                         OR Region_ID LIKE {search}
                         OR Captured_By LIKE {search}
                         ORDER BY Pokedex_ID
                         """.format(search = val_Search))
else:
    my_data = db.execute("""
                         SELECT * FROM Trainers
                         WHERE Trainer_ID LIKE {search}
                         OR Name LIKE {search}
                         OR Gym LIKE {search}
                         OR Specialist_Type LIKE {search}
                         OR Type_1 LIKE {search}
                         OR Type_2 LIKE {search}
                         OR Gender LIKE {search}
                         OR Region_ID LIKE {search}
                         OR Hometown LIKE {search}
                         ORDER BY Trainer_ID
                         """.format(search = val_Search))

print("<table border='1' cellspacing='0' cellpadding='10'>")

for row in my_data:
    print('<tr>')
    for field in row.keys():
        print('<td>')
        print(row[field])
        print('</td>')
    print('</tr>')
print('</table>')

db.commit()

template.my_footer()
