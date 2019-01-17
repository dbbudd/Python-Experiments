import csv, sqlite3

# set your database name here (remember the .db file extension)
my_database = "cars.db"

# CONNECT TO DATABASE
db = sqlite3.connect(my_database)
db.row_factory = sqlite3.Row

###############################################################################################
##############################   CREATE EMPLOYEE CARS   #######################################
###############################################################################################

# DROP TABLES
db.execute("DROP TABLE IF EXISTS Cars")
db.execute("CREATE TABLE Cars(CarID INT, Make TEXT, Model TEXT);")
    
# OPEN cars.txt AND READ IT!
reader = csv.reader(open('cars.txt', 'r'), delimiter='|')
for row in reader:
    my_data = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8")]
    db.execute("INSERT INTO Cars(CarID, Make, Model) VALUES (?, ?, ?);", my_data)
db.commit()


###############################################################################################
##############################   CREATE EMPLOYEE TABLE   ######################################
###############################################################################################

# DROP TABLES
db.execute("DROP TABLE IF EXISTS Employees")
db.execute("CREATE TABLE Employees(EmployeeID TEXT, Employee TEXT, DeptName TEXT, Car INT);")
    
# OPEN employees.txt AND READ IT!
reader = csv.reader(open('employees.txt', 'r'), delimiter='|')
for row in reader:
    my_data = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8"), unicode(row[3], "utf8")]
    db.execute("INSERT INTO Employees(EmployeeID, Employee, DeptName, Car) VALUES (?, ?, ?, ?);", my_data)
db.commit()

###############################################################################################
################################   SELECTION STATEMENTS   #####################################
###############################################################################################

# create a selection statement to print Employees table  
cursor1 = db.execute('SELECT EmployeeID, Employee, DeptName, Car FROM Employees ORDER by Car')
for row in cursor1:
    #print(dict(row))
    my_employees = dict(row)

# create a selection statement to print Cars Table
cursor2 = db.execute('SELECT CarID, Make, Model FROM Cars ORDER by CarID')
for row in cursor2:
    #print(dict(row))
    my_cars = dict(row)
    
cursor3 = db.execute('SELECT * FROM Employees WHERE DeptName = "Accounting"')
for row in cursor3:
    my_query = dict(row)

###############################################################################################
####################################   PRINT OUTPUTS  #########################################
###############################################################################################

print("#### EMPLOYEE TABLE ####")
print(str(my_employees))
print("")
print("#### CARS TABLE ####")
print(str(my_cars))