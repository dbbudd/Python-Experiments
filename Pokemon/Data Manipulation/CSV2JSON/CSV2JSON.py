import csv
import json

csvfile = open('pokedex.csv', 'r')
jsonfile = open('data.js', 'w')

reader = csv.DictReader( csvfile, )
jsonfile.write("var data = [\n")
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write(',\n')
jsonfile.write('];\n')