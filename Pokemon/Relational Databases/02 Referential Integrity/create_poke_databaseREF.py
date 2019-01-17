import sqlite3
import sys

#create a databease connection
db = sqlite3.connect('pokemon.db')


db.execute("PRAGMA foreign_keys=ON;")

#using the cursor class
db.execute("DROP TABLE IF EXISTS Pokedex;")
db.execute("DROP TABLE IF EXISTS Trainers;")
db.execute("DROP TABLE IF EXISTS Locations;")
db.execute("DROP TABLE IF EXISTS Training;")
db.execute("DROP TABLE IF EXISTS Battles;")
db.execute("DROP TABLE IF EXISTS Encounters;")



#TABLES WITH PRIMARY KEYS
db.execute('''
           CREATE TABLE Locations(
           Region_ID VARCHAR(2),
           Region TEXT,
           Capital TEXT,
           Biome TEXT,
           PRIMARY KEY(Region_ID)
           );
           ''')

#TABLES WITH FORIEGN KEYS
db.execute('''
           CREATE TABLE Trainers(
           Trainer_ID VARCHAR(5),
           Name TEXT,
           Gym TEXT,
           Specialist_Type TEXT,
           Type_1 TEXT,
           Type_2 TEXT,
           Gender VARCHAR(6),
           Region_ID VARCHAR(2),
           Hometown TEXT,
           PRIMARY KEY(Trainer_ID),
           FOREIGN KEY(Region_ID) REFERENCES Locations(Region_ID)
           );
           ''')

db.execute('''
           CREATE TABLE Pokedex(
           Pokedex_ID INTEGER,
           Species TEXT,
           Type TEXT,
           Attack INTEGER,
           Defense INTEGER,
           Spec_Attack INTEGER,
           Spec_Defense INTEGER,
           XP INTEGER,
           Health INTEGER,
           Region_ID VARCHAR(2),
           Captured_By VARCHAR(5),
           PRIMARY KEY(Pokedex_ID),
           FOREIGN KEY(Region_ID) REFERENCES Locations(Region_ID),
           FOREIGN KEY(Captured_By) REFERENCES Trainers(Trainer_ID)
           );
           ''')

db.execute('''
           CREATE TABLE Battles(
           Battle_ID INTEGER,
           Timestamp DATETIME,
           Pokedex_ID INTEGER,
           Trainer_ID VARCHAR(5),
           Region_ID VARCHAR(2),
           Home_Adv TEXT,
           Result TEXT,
           PRIMARY KEY(Battle_ID),
           FOREIGN KEY(Pokedex_ID) REFERENCES Pokedex(Pokedex_ID),
           FOREIGN KEY(Trainer_ID) REFERENCES Trainers(Trainer_ID)
           );
           ''')

db.execute('''
           CREATE TABLE Encounters(
           Encounters_ID INTEGER,
           Timestamp DATETIME,
           Pokedex_ID INTEGER,
           Region_ID VARCHAR(2),
           Home_Adv TEXT,
           Result TEXT,
           PRIMARY KEY(Encounters_ID),
           FOREIGN KEY(Region_ID) REFERENCES Locations(Region_ID),
           FOREIGN KEY(Pokedex_ID) REFERENCES Pokedex(Pokedex_ID)
           );
           ''')

#TABLES WITH COMPOSITE KEYS
db.execute('''
           CREATE TABLE Training(
           Trainer_ID VARCHAR(5),
           Pokedex_ID VARCHAR(2),
           Count_Encounters INTEGER,
           Count_Battles INTEGER,
           Attack INTEGER,
           Defense INTEGER,
           Spec_Attack INTEGER,
           Spec_Defense INTEGER,
           XP INTEGER,
           Health INTEGER,
           FOREIGN KEY (Trainer_ID) REFERENCES Trainers(Trainer_ID),
           FOREIGN KEY (Pokedex_ID) REFERENCES Pokedex(Pokedex_ID),
           PRIMARY KEY (Trainer_ID, Pokedex_ID)
           );
           ''')

db.commit()