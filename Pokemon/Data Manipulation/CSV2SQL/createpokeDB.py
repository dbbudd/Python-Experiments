import csv, sqlite3
from random import randint
from os import system

my_database = "pokemon.db"

def createDB():
    db = sqlite3.connect(my_database)
    db.row_factory = sqlite3.Row
    db.execute("DROP TABLE IF EXISTS Pokemon")
    db.execute("CREATE TABLE Pokemon(pokedex_number TEXT, species TEXT, types TEXT, attack TEXT, defense TEXT, sattack TEXT, sdefense TEXT, speed TEXT, health TEXT);")
    db.commit()
    print("Database has been created")

createDB()


