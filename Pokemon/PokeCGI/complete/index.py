#!/usr/bin/python
print "Content-type: text/html; charset=utf-8"
print

import cgi
import os
import template

template.my_header()

print("""
      <h1>Homepage</h1>
      <p>Welcome to the Pokedex</p>
      """)

#template.my_footer()

