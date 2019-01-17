import sqlite3
import sys
import csv

#create a databease connection
db = sqlite3.connect('eve.db')
db.text_factory = str


#DROP TABLES
db.execute("DROP TABLE IF EXISTS Regions;")
db.execute("DROP TABLE IF EXISTS Types;")
db.execute("DROP TABLE IF EXISTS Transactions;")

#CREATE TABLES
db.execute("CREATE TABLE Regions(Region_ID INTEGER, Region TEXT);")
db.execute("CREATE TABLE Types(Type_ID INTEGER, Type TEXT);")
db.execute("CREATE TABLE Transactions(Order_ID INTEGER, Region_ID INTEGER, System_ID INTEGER, Station_ID INTEGER, Type_ID INTEGER, Bid INTEGER, Price REAL, Min_Volume REAL, Vol_Remaining REAL, Vol_Entered REAL, Issued TEXT, Duration TEXT, Range INTEGER, Reported_By TEXT, Reported_Time TEXT);")

db.commit()

print("tables have been created")

def import_regions():
    my_file = "Regions.csv"
    reader = csv.reader(open(my_file, 'rU'), delimiter=',')
    count = 0
    for row in reader:
        my_data = [row[0], row[1]]
        db.execute("INSERT INTO Regions(Region_ID, Region) VALUES (?, ?);", my_data)
        count = count + 1
        db.commit()
    output = " records have been entered into the Regions table"
    print("")
    print str(count) + output

import_regions()

def import_types():
    my_file = "Types.csv"
    reader = csv.reader(open(my_file, 'rU'), delimiter=',')
    count = 0
    for row in reader:
        my_data = [row[0], row[1]]
        db.execute("INSERT INTO Types(Type_ID, Type) VALUES (?, ?);", my_data)
        count = count + 1
        db.commit()
    output = " records have been entered into the Type table"
    print("")
    print str(count) + output
    
import_types()

def import_transactions():
    my_file = "Transactions.csv"
    reader = csv.reader(open(my_file, 'rU'), delimiter=',')
    count = 0
    for row in reader:
        my_data = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14]]
        db.execute("""
                   INSERT INTO Transactions(Order_ID, Region_ID, System_ID, Station_ID, Type_ID, Bid, Price, Min_Volume, Vol_Remaining, Vol_Entered, Issued, Duration, Range, Reported_By, Reported_Time)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                   """, my_data)
        count = count + 1
        db.commit()
    output = " Records have been entered into the Type table"
    print("")
    print str(count) + output
    
    
    

import_transactions()