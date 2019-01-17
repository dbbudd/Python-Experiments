#import libraries
import csv, sqlite3, cgi, sys, os
import cgitb; cgitb.enable()
import contextlib
from os import system



#Database Connection
db = sqlite3.connect("pokemon.db")
db.row_factory = sqlite3.Row

#open CSV file
my_file = "pokedex.csv"
reader = csv.reader(open(my_file, 'r'), delimiter=',')
count = 0
for row in reader:
    my_data = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8"), unicode(row[3], "utf8"), unicode(row[4], "utf8"), unicode(row[5], "utf8"), unicode(row[6], "utf8"), unicode(row[7], "utf8"), unicode(row[8], "utf8")]
    db.execute("INSERT INTO Pokemon(pokedex_number, species, types, attack, defense, sattack, sdefense, speed, health) VALUES (?,?,?,?,?,?,?,?,?);", my_data)
    count = count + 1
db.commit()
output = " records have been entered into the database"
print("")
print str(count) + output