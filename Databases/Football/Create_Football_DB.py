#!/usr/bin/python
print 'Content-type: text/html\n\n'

import cgi
import cgitb; cgitb.enable()
import sqlite3

mydb = 'football.db'
conn = sqlite3.connect(mydb)
cursor = conn.cursor()

print 'Drop tables if they exist<br />'
cursor.execute('''DROP TABLE IF EXISTS Teams''')
cursor.execute('''DROP TABLE IF EXISTS Players''')
cursor.execute('''DROP TABLE IF EXISTS Games''')

print 'create Teams table<br />'
cursor.execute('''CREATE TABLE Teams (team_id INTEGER PRIMARY KEY,
					name varchar(20) NOT NULL,
					jersey varchar(10),
					shorts varchar(10),
					suburb varchar(20))''')

print 'create Players table<br />'
cursor.execute('''CREATE TABLE Players (	registration INTEGER PRIMARY KEY,
						first_name varchar(20) NOT NULL,
						last_name varchar(20) NOT NULL,
						address varchar(50),
						suburb varchar(20),
						DOB varchar(15),
						phone varchar(15))''')

print 'create Games table<br />'
cursor.execute('''CREATE TABLE Games (	games_id INTEGER PRIMARY KEY AUTOINCREMENT,
						team_id INTEGER NOT NULL,
						registration INTEGER NOT NULL,
						round INTEGER NOT NULL,
						position varchar(10),
						kicks INTEGER,
						handballs INTEGER,
						marks INTEGER,
						goals INTEGER,
						behinds INTEGER)''')

conn.commit()
cursor.close()
