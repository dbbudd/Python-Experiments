#!/usr/bin/env python

import csv
import sqlite3, sys, os
from os import system
import contextlib

#create a database connection
db = sqlite3.connect('pokemon.db')

db.row_factory = sqlite3.Row


def simple_select():
    searchstr = "'%" + "C" + "%'"
    my_data = db.execute("""
                     SELECT * FROM Locations
                     WHERE ? LIKE {search}
                     OR ? LIKE {search}
                     OR ? LIKE {search}
                     OR ? LIKE {search}
                     ORDER BY ?
                     """.format(search = searchstr), ("Region_ID", "Region", "Capital", "Biome", "Region_ID"))
    '''
    my_data = db.execute("""
                         SELECT * FROM Pokedex
                         WHERE Pokedex_ID LIKE {search}
                         OR Species LIKE {search}
                         OR Type LIKE {search}
                         OR Attack LIKE {search}
                         OR Defense LIKE {search}
                         OR Spec_Attack LIKE {search}
                         OR Spec_Defense LIKE {search}
                         OR XP LIKE {search}
                         OR Health LIKE {search}
                         OR Region_ID LIKE {search}
                         OR Captured_By LIKE {search}
                         ORDER BY Pokedex_ID
                         """.format(search = searchstr))
    
    my_data = db.execute("""
                         SELECT * FROM Trainers
                         WHERE Trainer_ID LIKE {search}
                         OR Name LIKE {search}
                         OR Gym LIKE {search}
                         OR Specialist_Type LIKE {search}
                         OR Type_1 LIKE {search}
                         OR Type_2 LIKE {search}
                         OR Gender LIKE {search}
                         OR Region_ID LIKE {search}
                         OR Hometown LIKE {search}        
                         ORDER BY Trainer_ID
                         """.format(search = searchstr))
    
    my_data = db.execute("""SELECT * FROM Trainers
                         WHERE Trainer_ID LIKE {search}
                         OR Name LIKE {search}
                         OR Gym LIKE {search}
                         OR Specialist_Type LIKE {search}
                         OR Type_1 LIKE {search}
                         OR Type_2 LIKE {search}
                         OR Gender LIKE {search}
                         OR Region_ID LIKE {search}
                         OR Hometown LIKE {search}        
                         ORDER BY Trainer_ID
                         """.format(search = searchstr))
    '''
    rows = my_data.fetchall()
    
    for row in rows:
        data = dict(row)
        print(data)

simple_select()