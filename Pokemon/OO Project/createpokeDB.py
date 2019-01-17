import csv, sqlite3
from random import randint
from os import system
from pokeObj import Pokemon

my_database = "pokemon.db"

def createDB():
    db = sqlite3.connect(my_database)
    db.row_factory = sqlite3.Row
    db.execute("DROP TABLE IF EXISTS Pokemon")
    db.execute("CREATE TABLE Pokemon(PokeID TEXT, Name TEXT, Species TEXT, HP TEXT, Attack TEXT);")
    db.commit()

def insertData():
    db = sqlite3.connect(my_database)
    db.row_factory = sqlite3.Row
    my_data = (
        ('1', 'Daniel', 'Earth', '200', '100')
    )
    db.execute("INSERT INTO Pokemon(PokeID, Name, Species, HP, Attack) VALUES(?,?,?,?,?);", my_data)
    db.commit()

createDB()
insertData()


