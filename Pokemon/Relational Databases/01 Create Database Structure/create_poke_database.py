import sqlite3
import sys

#create a databease connection
db = sqlite3.connect('pokemon.db')

#using the cursor class
#DROP TABLES
db.execute("DROP TABLE IF EXISTS Pokedex;")
db.execute("DROP TABLE IF EXISTS Trainers;")
db.execute("DROP TABLE IF EXISTS Locations;")
db.execute("DROP TABLE IF EXISTS Training;")
db.execute("DROP TABLE IF EXISTS Battles;")
db.execute("DROP TABLE IF EXISTS Encounters;")

#CREATE TABLES
db.execute("CREATE TABLE Locations(Region_ID VARCHAR(2), Region TEXT, Capital TEXT, Biome TEXT);")
db.execute("CREATE TABLE Trainers(Trainer_ID VARCHAR(5), Name TEXT, Gym TEXT, Specialist_Type TEXT, Type_1 TEXT, Type_2 TEXT, Gender VARCHAR(6), Region_ID VARCHAR(2), Hometown TEXT);")
db.execute("CREATE TABLE Pokedex(Pokedex_ID INTEGER, Species TEXT, Type TEXT, Attack INTEGER, Defense INTEGER, Spec_Attack INTEGER, Spec_Defense INTEGER, XP INTEGER, Health INTEGER, Region_ID VARCHAR(2), Captured_By VARCHAR(5));")
db.execute("CREATE TABLE Battles(Battle_ID INTEGER,Timestamp DATETIME, Pokedex_ID INTEGER, Trainer_ID VARCHAR(5), Region_ID VARCHAR(2), Home_Adv TEXT, Result TEXT);")
db.execute("CREATE TABLE Encounters(Encounters_ID INTEGER, Timestamp DATETIME, Pokedex_ID INTEGER, Region_ID VARCHAR(2), Home_Adv TEXT, Result TEXT);")
db.execute("CREATE TABLE Training(Trainer_ID VARCHAR(5), Pokedex_ID VARCHAR(2), Count_Encounters INTEGER, Count_Battles INTEGER, Attack INTEGER, Defense INTEGER, Spec_Attack INTEGER, Spec_Defense INTEGER, XP INTEGER, Health INTEGER);")

db.commit()