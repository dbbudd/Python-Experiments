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
val_Search = form.getvalue('query_search')
val_Column = form.getvalue('query_column')
val_Table = form.getvalue('query_table')


print("""
      <div style='float:left; display:block; width:100%; text-align:center;'>
      <h1>Search Results:</h1>   

      <div style='float:left; display:inline; width:400px; height:100%; margin-left:20px;'>
      """)
print("<h3> TABLE NAME: " + str(val_Table) + "</h3>")
print("<table border='1' cellspacing='0' cellpadding='10' width='100%'>")

my_data = db.execute("SELECT * FROM {table} WHERE {column} LIKE {search}".format(table = val_Table, column = val_Column, search = "'" + val_Search + "'"))
rows = my_data.fetchall()
for row in rows:
    print("</tr>")
    for field in row.keys():
        print("<td>")
        print(row[field])
        print("</td>")
    print("</tr>")
print("</table>")
    




print("""
      </div>
      </div>
      """)



db.commit()