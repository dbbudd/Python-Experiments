#!/usr/bin/python
print "Content-type: text/html"
print

#import the libraries
import cgi
import sqlite3
import sys
import template


template.my_header()

def add_form():
    print("<h1>ADD LOCATION</h1>")
    print("""
          <form id='add_location' action='insert_new_location.py' method='GET'>
          
          <p>
          <label>Region ID:</label><br/>
          <input type='text' name='Region_ID'>
          </p>
          <p>
          <label>Region:</label><br/>
          <input type='text' name='Region'>
          </p>
          <p>
          <label>Capital City:</label><br/>
          <input type='text' name='Capital'>
          </p>
          <p>
          <label>Biome:</label><br/>
          <select name='Biome'>
          <option>Desert</option>
          <option>Tundra</option>
          <option>Tiaga</option>
          <option>Savanna</option>
          <option>Grassland</option>
          <option>Tropical</option>
          </select>
          </p>
          
          <p>
          <input type='submit' value='Submit' />
          </p>
          
          </form>
          """)

add_form()

template.my_footer()