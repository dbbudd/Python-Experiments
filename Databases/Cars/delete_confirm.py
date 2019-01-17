#!/usr/bin/python
print "Content-type: text/html"
print

#import the libraries
import cgi
import cgitb; cgitb.enable()
import sqlite3
import sys, os, contextlib
import Tkinter
import tkMessageBox





#create a database connection
db = sqlite3.connect("cars.db")
db.row_factory = sqlite3.Row

form = cgi.FieldStorage()
val_Search = form.getvalue('employee_id')
val_Column = 'EmployeeID'
val_Table = 'Employees'


print("""
      <div style='float:left; display:block; width:100%; text-align:center;'>
      <h1>Search Results:</h1>   

      <div style='float:left; display:inline; width:400px; height:100%; margin-left:20px;'>
      """)
print("<h3> TABLE NAME: " + str(val_Table) + "</h3>")
print("<table border='1' cellspacing='0' cellpadding='10' width='100%'>")

#DELETE RECORDS
my_data = db.execute("SELECT * FROM {table} WHERE {column} = {search}".format(table = val_Table, column = val_Column, search = "'" + val_Search + "'"))
rows = my_data.fetchall()
for row in rows:
    print("</tr>")
    for field in row.keys():
        print("<td>")
        print(row[field])
        print("</td>")
    print("</tr>")
print("</table>")
    

#Define function which will delete the record
def delete_record():
    #db.execute("DELETE * FROM {table} WHERE {column} = {search}".format(table = val_Table, column = val_Column, search = "'" + val_Search + "'"))
    print("<p>Record of Employee: " + val_Search + " has been deleted</p>" )


to_delete = form.getvalue('delete')
if to_delete != 1:
    print("<p>Don't Delete</p>")
else:
    print("<p>Delete</p>")
    delete_record()
    
 ##### HERE    
print("</p>")
to_delete = form.getvalue('delete')
if to_delete != 1:
    print("<p>Don't Delete</p>")
else:
    generate_form()<form id='add_car' action='search_car_data.py' method='POST'>
    <p><input type='button' value='Delete Record' onClick='delete_record()'/></p>
    </form>
print("</div>")
print("</div>")
#      """)





top = Tkinter.Tk()
def hello():
    tkMessageBox.showinfo("Say Hellow", "Hello World")
    
b1 = Tkinter.Button(top, text = "Say Hello", command = hello)
b1.pack()

top.mainloop()







db.commit()