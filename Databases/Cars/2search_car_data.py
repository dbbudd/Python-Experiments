#!/usr/bin/python
print "Content-type: text/html"
print

#import the libraries
import cgi
import cgitb; cgitb.enable()
import sqlite3
import sys, os, contextlib



#create a database connection
db = sqlite3.connect("cars.db")
db.row_factory = sqlite3.Row

form = cgi.FieldStorage()
val_Search = form.getvalue("query_search")
val_Column = form.getvalue("query_column")
val_Table = form.getvalue("query_table")
val_Search = "%F"
val_Column = "Model"
val_Table = "Cars"

print("""
      <div style='float:left; display:block; width:100%; text-align:center;'>
      <h1>Search Results:</h1>
      <div style='float:left; display:inline; width:400px; height:100%; margin-left:20px;'>
      <h3> TABLE NAME: Cars </h3>
      <p>To search for a wildcard search use '%'.  For example 'F%' will return everything that starts with an 'F' and '%' on its own will return everything.</p>
      <table border='1' cellspacing='0' cellpadding='10' width='100%'>
      <tr style='font-weight:bold;'>
      <td>CAR ID</td>
      <td>MAKE</td>
      <td>MODEL</td>
      <td>VALUE</td>
      </tr>
    """)
my_data = db.execute("SELECT Model FROM Cars WHERE Model LIKE '%s'" % '%F')
for row in my_data:
    print("<tr>")
    for field in row.keys():
        print("<td>")
        print(row[field])
        print("</td>")
    print("</tr>")
print("</table></div>")
print("</div>")

db.commit()
