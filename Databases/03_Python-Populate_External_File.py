import sqlite3, csv

my_database = "cars.db"
my_file = "data.txt"

db = sqlite3.connect(my_database)
db.row_factory = sqlite3.Row

db.execute("DROP TABLE IF EXISTS Cars")
db.execute("CREATE TABLE Cars(column_1 TEXT, column_2 TEXT, column_3 TEXT);")

#open CSV file
reader = csv.reader(open(my_file, 'r'), delimiter='|')
for row in reader:
    my_data = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8")]
    db.execute("INSERT INTO Cars(column_1, column_2, column_3) VALUES (?, ?, ?);", my_data)

db.commit()

# Create a selection statement
my_data = db.execute('SELECT * FROM Cars ORDER BY column_2')

for row in my_data:
    print(dict(row))
    