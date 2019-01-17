#!/usr/bin/python
import os
import sys


formname = "test.html"
handlername = "test.py"

# This function will generate a HTML/Javascript form
def generate_html():
    file = open(formname, 'a')
    
    file.write("<!DOCTYPE html>")
    file.write("<html>")
    file.write("<head>")
    file.write("<title>" + formname + "</title>")
    file.write("</head>")
    file.write("<body>")
    
    #create the form
    file.write("<form id='search_database' action='")
    file.write(handlername)
    file.write("' method='GET'>")
    file.write("<label>Search:</label>")
    file.write("<input type='text' name='Search_Query'>")
    file.write("<input type='submit' value='Submit' />")
    file.write("</form>")
    
    file.write("</body>")
    file.write("</html>")

generate_html()





# This fuction will generate a template CGI page which will handle the form
def generate_handler():
    file = open(handlername, 'a')
    
    file.writelines("""
    #!/usr/bin/python
    print "Content-type: text/html"
    print
    
    #import the libraries
    import cgi
    import cgitb; cgitb.enable()
    import sqlite3
    import sys, os, contextlib
    
    form = cgi.FieldStorage()
    
    '''
            # Receive the variable from the other page and do something with it
                var1 = str(form.getvalue('Search_Query'))
                val_Search = "'" + frm_Search + "'"
            
            #create a database connection
                db = sqlite3.connect('pokemon.db')
                db.row_factory = sqlite3.Row
            
    '''
    
    
    
    print("<html>")
    print("<head>")
    print("<title>")
    print(filename)
    print("</title>")
    print("<meta http-equiv='Content-Type' content='text/html;charset=utf-8'>")
    print("</head>")
    print("<body>")
    
    print("<!--put your python code here-->")
    '''
        # SELECT Statement
            my_data = db.execute("SELECT * FROM Trainers WHERE Trainer_ID LIKE {search}".format(search = val_Search))
        
        # OUTPUT SELECTED DATA
            print("<table border='1' cellspacing='0' cellpadding='10'>")
            for row in my_data:
                print('<tr>')
                for field in row.keys():
                    print('<td>')
                    print(row[field])
                    print('</td')
                print('<tr>')
            print('</table>')
        
    '''
    
    print("</body>")
    print("</html>")
    """)
    file.close()
    
    # set the permissions of the file you have created
    os.system('chmod 755 %s' % handlername)
    
    
    

generate_handler()