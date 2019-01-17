#!/usr/bin/env python

import csv
import sqlite3, sys, os
from os import system
import contextlib

#create a database connection
db = sqlite3.connect('pokemon.db')

db.row_factory = sqlite3.Row


def simple_select():
    my_data = db.execute("SELECT Species FROM Pokedex WHERE Pokedex_ID = 1")
    rows = my_data.fetchall()
    
    for row in rows:
        data = dict(row)
        print(data)
        for field in row.keys():
            print(row[field])

#simple_select()
    
#query uses the wildcard '%' delimeter

def simple_wildecard():
    
    #value being parsed
    searchstr = "P%"
    my_data = db.execute("SELECT Species FROM Pokedex WHERE Species LIKE ?", (searchstr,))
    rows = my_data.fetchall()
    
    ##RETURN RESULTS
    #return all results
    
    print("""
      -- ALL RETURNED RESULTS --
      """)
    for row in rows:
        data = dict(row)
        print(data)

#simple_wildecard()


def select_join():
    my_data = db.execute("""
                         SELECT Species FROM Pokedex
                         LEFT OUTER JOIN Trainers
                         ON (Pokedex.Captured_By = Trainers.Trainer_ID)
                         WHERE (Pokedex.Captured_By = Trainers.Trainer_ID)
                         """)
    
    rows = my_data.fetchall()
    
    for row in rows:
        data = dict(row)
        print(data)

#select_join()

def multitable_select():
    my_data = db.execute("""
                         SELECT Trainers.Name, Pokedex.Species FROM Pokedex, Trainers
                         WHERE Pokedex.Captured_By = Trainers.Trainer_ID ORDER BY Trainers.Name
                         """)
    
    rows = my_data.fetchall()
    
    for row in rows:
        data = "Trainer " + str(row[0]) + " captured a " + str(row[1])
        print(data)

multitable_select()


def binding_variables():
    val_Selection = "Species"
    val_Search = "%p%"
    val_Column = "Species"
    val_Table = "Pokedex"
    
    my_data = db.execute("""
                         SELECT {selection} FROM {table}
                         WHERE {column}
                         LIKE {search}
                         """.format(selection = val_Selection, table = val_Table, column = val_Column, search = "'" + val_Search + "'"))
    rows = my_data.fetchall()
    for row in rows:
        for field in row.keys():
            print(row[field])

#binding_variables()



def select_table_names():
        my_data = db.execute("SELECT name FROM sqlite_master WHERE type='table'")
        print("List of Tables in your Database...")
        print(" ")
        rows = my_data.fetchall()
        for row in rows:
            print(row[0])
print("""
      ------
      My Tables
      ------
      """)

#select_table_names()


def select_column_names():
        print("All of the columns in your database")
        print(" ")
        cursor = db.execute("SELECT name FROM sqlite_master WHERE type='table'")
        for tablerow in cursor.fetchall():
            table = tablerow[0]
            cursor.execute("SELECT * FROM {t} LIMIT 1".format(t = table))
            for row in cursor:
                for field in row.keys():
                    print(table)
                    print(str(field))

print("""
      ------
      My Columns
      ------
      """)

#select_column_names()












db.commit()
db.close()