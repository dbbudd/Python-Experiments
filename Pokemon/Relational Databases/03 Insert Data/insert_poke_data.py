import csv
import sqlite3, sys, os
from os import system
import contextlib

#create a database connection
db = sqlite3.connect('pokemon.db')

#import in order of data dependencies
#import Locations
#open CSV file
def import_locations():
    my_file = "location.csv"
    reader = csv.reader(open(my_file, 'rU'), delimiter=',')
    count = 0
    for row in reader:
        my_data = [row[0], row[1], row[2], row[3]]
        db.execute("INSERT INTO Locations(Region_ID, Region, Capital, Biome) VALUES (?, ?, ?, ?);", my_data)
        count = count + 1
        db.commit()
    output = " records have been entered into the database"
    print("")
    print str(count) + output


def import_trainers():
    my_file = "trainers.csv"
    reader = csv.reader(open(my_file, 'rU'), delimiter=',')
    count = 0
    for row in reader:
        my_data = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
        db.execute("INSERT INTO Trainers(Trainer_ID, Name, Gym, Specialist_Type, Type_1, Type_2, Gender, Region_ID, Hometown) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", my_data)
        count = count + 1
        db.commit()
    output = " records have been entered into the database"
    print("")
    print str(count) + output


def import_pokedex():
    my_file = "pokedex.csv"
    reader = csv.reader(open(my_file, 'rU'), delimiter=',')
    count = 0
    for row in reader:
        my_data = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]]
        db.execute("INSERT INTO Pokedex(Pokedex_ID, Species, Type, Attack, Defense, Spec_Attack, Spec_Defense, XP, Health, Region_ID, Captured_By) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", my_data)
        count = count + 1
        db.commit()
    output = " records have been entered into the database"
    print("")
    print str(count) + output



import_locations()
import_trainers()
import_pokedex()


db.commit()