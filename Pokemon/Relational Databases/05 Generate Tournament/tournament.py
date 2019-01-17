import sqlite3
import sys

#create a databease connection
db = sqlite3.connect('pokemon.db')
db.execute("PRAGMA foreign_keys=ON;")

db.commit()