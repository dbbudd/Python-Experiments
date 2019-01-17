import sqlite3

# set your database name here (remember the .db file extension)
my_database = "cars.db"

# set the name of your table here
my_table = "Cars"

my_data = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)


def main():
    db = sqlite3.connect(my_database)
    db.row_factory = sqlite3.Row
    db.execute("DROP TABLE IF EXISTS my_table")
    db.execute("CREATE TABLE my_table(Id INT, Name TEXT, Price INT)")
    db.executemany("INSERT INTO my_table VALUES(?, ?, ?)", my_data)

    db.commit()
    
    # create a selection statement
    cursor = db.execute('SELECT Id, Name FROM my_table ORDER by Id')
    for row in cursor:
        print(dict(row))

if __name__ == "__main__": main()