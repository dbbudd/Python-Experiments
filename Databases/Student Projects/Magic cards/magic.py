#!/usr/bin/env python

import csv
import sqlite3, sys, os
from os import system
import contextlib

#create a database connection
db = sqlite3.connect('MagicTheGathering.db')
db.row_factory = sqlite3.Row

result = open("DeckCard.csv",'wb')
writer = csv.writer(result, dialect = 'excel')



my_data = db.execute("""
                         SELECT * FROM DeckCard
                         """)

rows = my_data.fetchall()

for row in rows:
    data = tuple(row)
    writer.writerow(data)
    #print(data)