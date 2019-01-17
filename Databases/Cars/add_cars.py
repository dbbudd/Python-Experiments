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
    print ("<h1>ADD NEW CAR</h1>")
    print ("<form id='add_car' action='insert_car_data.py' method='POST'>")
    print ("<ul style='list-style:none'>")
    print ("<li>")
    print ("<label for='car_id' style='padding-right:40px;'>Car ID:</label>")
    print ("<input name='car_id' type='text' />")
    print ("</li>")
    print ("<li>")
    print ("<label for='car_make' style='padding-right:40px;'>Make:</label>")
    print ("<input name='car_make' type='text' />")
    print ("</li>")
    print ("<li>")
    print ("<label for='car_model' style='padding-right:40px;'>Model:</label>")
    print ("<input name='car_model' type='text' />")
    print ("</li>")
    print ("<li>")
    print ("<label for='car_value' style='padding-right:40px;'>Value:</label>")
    print ("<input name='car_value' type='text' />")
    print ("</li>")
    print ("<li>")
    print ("<input type='submit' />")
    print ("</li>")
    print ("</form>")
    print ("</body></html>")

generate_form()