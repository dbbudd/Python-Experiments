import csv, sqlite3
from random import randint
from os import system
from pokeObj import Pokemon



def generateNum():
    my_number = randint(0,6)
    return my_number

my_value = str(generateNum())

def spawnPokemon():
    my_database = "pokemon.db"
    db = sqlite3.connect(my_database)
    my_data = db.execute("SELECT * FROM Pokemon").fetchall()
    for rows in my_data:
        for i in rows:
            if i[0] == my_value:
                my_Pika = Pokemon(rows[0], rows[1], rows[2], rows[3], rows[4])
    print("")
    print("Pokemon: " + my_Pika.name)
    print("HP: " + str(my_Pika.HP))
    print("Attack: " + str(my_Pika.attack))
    print("Number: " + my_Pika.number)
    print("Species: " + my_Pika.species)

spawnPokemon()



