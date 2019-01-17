#!/usr/bin/env python

print "Content-type: text/html"
print

#import the libraries
import cgi
import cgitb; cgitb.enable()
import sqlite3
import sys, os, contextlib

form = cgi.FieldStorage()
val_Region_ID = str(form.getvalue('Region_ID'))
val_Region = str(form.getvalue('Region'))
val_Capital = str(form.getvalue('Capital'))
val_Biome = str(form.getvalue('Biome'))

my_data = (
    (val_Region_ID, val_Region, val_Capital, val_Biome)
)

#create a database connection
db = sqlite3.connect('pokemon.db')
db.row_factory = sqlite3.Row

#using the cursor class
db.execute("INSERT INTO Locations(Region_ID, Region, Capital, Biome) VALUES(?, ?, ?, ?);", my_data)

#PRINT THE HTML PAGE
print("""
      <!doctype html>
      <html lang="en-US">
      
      <head>
      <title>PokeCGI</title>
      <meta http-equiv='Content-Type' content='text/html;charset=utf-8'>
      </head>
      
      <body>
      """)

print("""
      <h1>Add Location</h1>
      <p>Your record has been successfully inserted into the database</p>
      <p>&nbsp;</p>
      <h2>Below are the current records in the Locations Table</h2>
      """)

my_data = db.execute('SELECT * FROM Locations')

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



print("""
      </body>
      </html>
      """)