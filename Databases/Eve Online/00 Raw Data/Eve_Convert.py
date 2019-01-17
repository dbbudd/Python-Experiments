#!/usr/bin/env python

import csv
import json

reader = open('Types.txt', 'rU')
writer = open('Types.csv', 'w')

for row in reader:
    row = row.replace("'", "").strip()
    writer.write(row)
    writer.write('\n')

print("output complete")