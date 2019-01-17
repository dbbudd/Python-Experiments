#!/usr/bin/env python

print "Content-type: text/html"
print

#import the libraries
import cgi
import cgitb; cgitb.enable()
import sqlite3
import sys


print("""
      <!doctype html>
      <html lang="en-US">
      """)

print("""
      <head>
      <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
      <title>Input Autocomplete Suggestions Demo</title>
      <link rel="stylesheet" type="text/css" media="all" href="style.css">
      <script type="text/javascript" src="js/jquery-1.9.1.min.js"></script>
      <script type="text/javascript" src="js/jquery.autocomplete.min.js"></script>
      <script type="text/javascript" src="js/currency-autocomplete.js"></script>
      </head>
      """)

print("""
      <body>
      <div id="topbar">POKEMON SEARCH</div>
      <div id="w">
      <div id="content">
      <h1>Pokemon DB Autocomplete Search</h1>
      <div id="searchfield">
      <form>
      <p>
      <label>Select Database Table:</label><br/>
      <select>
      <option value="volvo">Volvo</option>
      <option value="saab">Saab</option>
      <option value="mercedes">Mercedes</option>
      <option value="audi">Audi</option>
      </select>
      </p>
      """)

print("""
      <p>
      <label>Select the Attribute:</label>
      <input type="text" name="currency" class="biginput" id="autocomplete">
      </p>
      """)

print("""
      </form>
      </div>
      </div>
      </div>
      </body>
      """)

print("""
      </html>
      """)