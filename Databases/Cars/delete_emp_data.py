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
#val_Search = form.getvalue('employee_id')
val_Search = 'employee_id'
val_Column = 'EmployeeID'
val_Table = 'Employees'


print("""
      <div style='float:left; display:block; width:100%; text-align:center;'>
      <h1>Search Results:</h1>
      <form id='delete_employee' action='delete_emp_data.py' method='GET'>
      <input type='hidden' name='check' value='1' />
      <input type='button' value='Delete Records' />
      </form>
      </div>
      """)

def delete_record():
    #db.execute("DELETE * FROM {table} WHERE {column} = {search}".format(table = val_Table, column = val_Column, search = "'" + val_Search + "'"))
    print("<p>Record of Employee: " + val_Search + " has been deleted</p>" )

form = cgi.FieldStorage()
to_delete = form.getvalue('check')
if to_delete != '1':
    print("<p>Don't Delete</p>")
else:
    print("<p>Delete</p>")
    delete_record()






db.commit()