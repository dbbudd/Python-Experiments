import csv, sqlite3

# set your database name here (remember the .db file extension)
my_database = "cars.db"

# set the name of your table here
my_table = "Cars"

# data file you are going to import
my_file = "data.txt"

def main():   
    
    db = sqlite3.connect(my_database)
    db.row_factory = sqlite3.Row
    db.execute("DROP TABLE IF EXISTS my_table")
    db.execute("CREATE TABLE my_table(Id INT, Name TEXT, Price INT);")
    
    # open CSV file
    reader = csv.reader(open(my_file, 'r'), delimiter='|')
    for row in reader:
        my_data = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8")]
        db.execute("INSERT INTO my_table (Id, Name, Price) VALUES (?, ?, ?);", my_data)
    db.commit()
    
    # create a selection statement
    cursor = db.execute('SELECT Id, Name, Price FROM my_table ORDER by Id')
    for row in cursor:
        print(dict(row))

if __name__ == "__main__": main()