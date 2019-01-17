#!/usr/bin/python
print "Content-type: text/html"
print

#import the libraries
import cgi
import cgitb; cgitb.enable()
import sqlite3
import sys




#Define function to generate HTML form.
def generate_form():
    print ("<html></head>")
    print ("")
    print ("</head></body>")
    print ("<h1>DELETE EMPLOYEE</h1>")
    print ("<form id='delete_employee' action='delete_emp_data.py' method='POST'>")
    print ("<ul style='list-style:none'>")
    print ("<li>")
    print ("<p>Enter the Employee ID of the Employee you which to delete from the database.</p>")
    print ("</li>")
    print ("<li>")
    print ("<label for='employee_id' style='padding-right:40px;'>Employee ID:</label>")
    print ("<input name='employee_id' type='text' />")
    print ("</li>")
    print ("<li>")
    print ("<input type='submit' />")
    print ("</li>")
    print ("</form>")
    print ("</body></html>")

