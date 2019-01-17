#!/usr/bin/env python

import csv
import sqlite3, sys, os
from os import system
import contextlib

#create a database connection
db = sqlite3.connect('eve.db')
db.row_factory = sqlite3.Row

# Select the Type from Types table where the Type_ID is "2"
def Question_1():
    print("")
    print("###  QUESTION ONE ###")
    my_data = db.execute("...")
    rows = my_data.fetchall()
    
    for row in rows:
        data = dict(row)
        print(data)

Question_1()

# Select all records from the Regions Table
def Question_2():
    print("")
    print("###  QUESTION TWO ###")
    my_data = db.execute("...")
    rows = my_data.fetchall()
    
    for row in rows:
        data = dict(row)
        print(data)
Question_2()



# Select all records from the Regions Table with a Region_ID greater than "10000054"
def Question_3():
    print("")
    print("###  QUESTION THREE ###")
    my_data = db.execute("...")
    rows = my_data.fetchall()
    
    for row in rows:
        data = dict(row)
        print(data)
Question_3()


# Select the Region_ID from the Regions table where the Region is "Kador"
def Question_4():
    print("")
    print("###  QUESTION FOUR ###")
    my_data = db.execute("...")
    rows = my_data.fetchall()
    
    for row in rows:
        data = dict(row)
        print(data)
Question_4()

# Select the Region from the Regions table where the Region starts with 'F'
def Question_5():
    print("")
    print("###  QUESTION FIVE ###")
    my_data = db.execute("...")
    rows = my_data.fetchall()
    
    for row in rows:
        data = dict(row)
        print(data)
Question_5()



#SQL Statement: Retrieve the table names from "sqlite_master"
def Question_6():
    print("")
    print("###  QUESTION SIX ###")
    my_data = db.execute("...")
    rows = my_data.fetchall()
    
    for row in rows:
        data = dict(row)
        print(data)
Question_6()


#SQL Statement: Retrieve Type_ID and Type FROM Types where the Type_ID is greater than "365900".
# Also make sure that the results are ranked by Type_ID.
def Question_7():
    print("")
    print("###  QUESTION SEVEN ###")
    my_data = db.execute("...")
    rows = my_data.fetchall()
    
    for row in rows:
        data = dict(row)
        print(data)
Question_7()


# Select the Type_ID from the Types table where the Type_ID is greater
# then 36590 and order the results in decending order
def Question_8():
    print("")
    print("###  QUESTION EIGHT ###")
    my_data = db.execute("...")
    rows = my_data.fetchall()  
    for row in rows:
        data = dict(row)
        print(data)
Question_8()

# Select all records from the Transactions table but limit the output to 1 record.
def Question_9():
    print("")
    print("###  QUESTION NINE ###")
    my_data = db.execute("...")
    rows = my_data.fetchall()
    
    for row in rows:
        data = dict(row)
        print(data)
Question_9()

#SQL Statement: Select Type from Types, Type_ID and Duraction from Transactions where
# the Order_ID in the Transactions table is equal to "1936527645"
def Question_10():
    print("")
    print("###  QUESTION TEN ###")
    my_data = db.execute("...")
    rows = my_data.fetchmany()
    
    for row in rows:
        data = "Type: (" + str(row[1]) + ")" + str(row[0]) + " - " + str(row[2])
        print(data)
Question_10()

# What is the highest value in the Price column of the Transactions table
def Question_11():
    print("")
    print("###  QUESTION ELEVEN ###")
    
    my_data = db.execute("...")
    rows = my_data.fetchall()
    
    for row in rows:
        data = dict(row)
        print(data)
Question_11()

# Use a SQL query to find out how many records are in the Transaction table.
# Use "Type_ID" at the attribute which you retrieve from the Transaction table.
def Question_12():
    print("")
    print("###  QUESTION TWELVE ###")
    
    my_data = db.execute("...")
    rows = my_data.fetchall()
    
    for row in rows:
        data = dict(row)
        print(data)
Question_12()



# Write a SQL statement which will delete (DROP) a table called "Station" if it already exists
def Question_13():
    print("")
    print("###  QUESTION THIRTEEN ###")
    
    db.execute("...")
    
Question_13()

# Create a new table called "Station" with a Primary Key called Station_ID, which is an integer
# and a second attribute called Station with the data type "TEXT"
def Question_14():
    print("")
    print("###  QUESTION FOURTEEN ###")
    
    db.execute("...")
    
    
Question_14()

# Insert a new record into the Station table with the Station_ID value of "60014935"
# and the Station value = "Australia"
def Question_15():
    print("")
    print("###  QUESTION FIFTEEN ###")
    my_data = (60014935, 'Australia')
    db.execute("...", my_data)
    db.commit()
    
    
Question_15()