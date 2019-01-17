#!/usr/bin/python
import os
import sys

#entire folder and all subfolders
#os.system('chmod -R 755 PokeCGI')

#all files in current directory
#os.system('chmod 755 *')

filename = "test.py"

file = open(filename, 'a')

file.writelines("""
#!/usr/bin/python
print "Content-type: text/html"
print

#import the libraries
import cgi
import cgitb; cgitb.enable()
import sqlite3
import sys


print("<html>")
print("<head>")
print("<title>PokeCGI</title>")
print("<meta http-equiv='Content-Type' content='text/html;charset=utf-8'>")
print("</head>")
print("<body>")

print("#put your python code here")

print("</body>")
print("</html>")
""")
file.close()

os.system('chmod 755 test.py')