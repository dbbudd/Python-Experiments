#!/usr/bin/python
print "Content-type: text/html"
print

#import the libraries
import cgi
import cgitb; cgitb.enable()
import sqlite3
import sys

form = cgi.FieldStorage()
val_CarID = str(form.getvalue('car_id'))
val_Make = str(form.getvalue('car_make'))
val_Model = str(form.getvalue('car_model'))
val_Value = str(form.getvalue('car_value'))

my_data = (
    (val_CarID, val_Make, val_Model, val_Value)
)


#create a database connection
db = sqlite3.connect("cars.db")
db.row_factory = sqlite3.Row

#using the cursor class
cur = db.cursor()
cur.execute("INSERT INTO Cars(CarID, Make, Model, Value) VALUES (?, ?, ?, ?);", my_data)
print('<p>Your data has been successfully inserted into the database</p>')
print('<p>&nbsp;</p>')
print('<p>&nbsp;</p>')


print("<h1>All data currently in the Database</h1>")
my_data = db.execute("SELECT name FROM sqlite_master WHERE type='table'")
for tablerow in my_data.fetchall():
    table = tablerow[0]
    my_data = db.execute("SELECT * FROM {t}".format(t = table))
    print("<h3> TABLE NAME:")
    print(table)
    print("</h3>")
    print("<table border='1' cellspacing='0' cellpadding='10'>")
    print("""
          <tr style='font-weight:bold;'>
          <td>Column 1</td>
          <td>Column 1</td>
          <td>Column 1</td>
          <td>Column 1</td>
          </tr>
          """)
    for row in my_data:
        print("<tr>")
        for field in row.keys():
            print("<td>")
            print(row[field])
            print("</td>")
            print("</tr>")
            print("</table>")

db.commit()


