#!/usr/bin/python
print "Content-type: text/html"
print

#import the libraries
import cgi
import cgitb; cgitb.enable()
import sqlite3
import sys

def generate_search_form():
    #create a database connection
    db = sqlite3.connect("cars.db")
    db.row_factory = sqlite3.Row

    def select_table_names():
        my_data = db.execute("SELECT name FROM sqlite_master WHERE type='table'")
        print("<p>Which table do you wish to search in? </p>")
        print("<SELECT name='query_table'>")
        rows = my_data.fetchall()
        for row in rows:
            my_value = "value='" + str(row[0]) + "'"
            print("<option " + my_value + ">")
            print(row[0])
            print("</option>")
        print("</SELECT>")

    def select_column_names():
        print("<p>Which column do you wish to search in? </p>")
        print("<SELECT name='query_column'>")
        cursor = db.execute("SELECT name FROM sqlite_master WHERE type='table'")
        for tablerow in cursor.fetchall():
            table = tablerow[0]
            cursor.execute("SELECT * FROM {t} LIMIT 1".format(t = table))
            for row in cursor:
                for field in row.keys():
                    my_value = "value='" + str(field) + "'"
                    print("<option " + my_value + ">")
                    print(table)
                    print(": ")
                    print(str(field))
                    print("</option>")
        print("</SELECT>")
    
    #CREATING THE FORM STRUCTURE
    print("""
          <h1>QUERY SEARCH</h1>
          <p>To search for a wildcard search use '%'. For example 'F%' will return everything that starts with an 'F' and '%' on its own will return everything.</p>
          <form id='add_car' action='search_car_data.py' method='POST'>
          <p>Search: <input name='query_search' type='text'/></p>
        """)
    select_table_names()
    select_column_names()

    print("""
          <p><input type='submit' value='search' /></p>
          </form>
        """)

print("""
      <html>
      </head>
      <title>THE CARS DATABASE</title>
      </head>
      <body>
    """)


generate_search_form()



print("""
      </body>
      </html>
    """)
