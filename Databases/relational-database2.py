import sqlite3
import sys

#create a database connection
db = sqlite3.connect("cars.db")
db.row_factory = sqlite3.Row

#using the cursor class
cur = db.cursor()
cur.executescript("""
    DROP TABLE IF EXISTS Cars;
    CREATE TABLE Cars(CarID varchar(6) NOT NULL, Make TEXT, Model TEXT, Value INT CHECK (Value >= 100000), PRIMARY KEY(CarID));
    INSERT INTO Cars(CarID, Make, Model, Value) VALUES ('ABC123', 'Audi', 'R8', 300000);
    INSERT INTO Cars(CarID, Make, Model, Value) VALUES ('DEF444', 'Mercedes', 'SLS', 400000);
    INSERT INTO Cars(CarID, Make, Model, Value) VALUES ('XYZ000', 'Bentley', 'GT Continental', 600000);
    """)

cur.executescript("""
    DROP TABLE IF EXISTS Employees;
    CREATE TABLE Employees(EmployeeID varchar(4) NOT NULL, Employee TEXT NULL, DeptName varchar(10), CarID varchar(6) NOT NULL,
    PRIMARY KEY(EmployeeID),
    FOREIGN KEY (CarID) REFERENCES Cars(CarID) ON UPDATE CASCADE ON DELETE SET NULL);
    INSERT INTO Employees(EmployeeID, Employee, DeptName, CarID) VALUES ('E001', 'CLARKE', 'ACCOUNTING', 'ABC123');
    INSERT INTO Employees(EmployeeID, Employee, DeptName, CarID) VALUES ('E002', 'KENT', 'IT SUPPORT', 'DEF444');
    INSERT INTO Employees(EmployeeID, Employee, DeptName, CarID) VALUES ('E003', 'MANN', 'SALES', 'DEF444');
    INSERT INTO Employees(EmployeeID, Employee, DeptName, CarID) VALUES ('E004', 'LANE', 'IT SUPPORT', 'XYZ000');
    INSERT INTO Employees(EmployeeID, Employee, DeptName, CarID) VALUES ('E005', 'LOIS', 'SALES', 'XYZ000');
    INSERT INTO Employees(EmployeeID, Employee, DeptName, CarID) VALUES ('E006', 'OLSEN', 'ACCOUNTING', 'XYZ000');
    """)

db.commit()
    
my_length = cur.execute("SELECT MAX(LENGTH(DeptName)) FROM Employees")
for row in my_length:
    print (row)

# METHOD 1: Using the fetchall() method (output as tuple)
cur.execute("SELECT * FROM Cars ORDER by CarID")
my_data = cur.fetchall()
print(my_data)

# METHOD 2: Using the for-loop method (ouput in rows)
my_data = cur.execute('SELECT * FROM Employees ORDER by CarID')
for row in my_data:
    print(row)

# METHOD 3: Using row_factory
my_data = db.execute('SELECT * FROM Cars ORDER by CarID')
for row in my_data:
    print(dict(row))