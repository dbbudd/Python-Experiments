#!/usr/bin/env python

#declare a dictionary
city = {
    "New York City":8175133,
    "Los Angeles": 3792621,
    "Washington":632323,
    "Chicago": 2695598
    }

#ACCESSING THE DICTIONARY

#get all keys
city.keys()

#get all values
city.values()

#Accessing
city["New York City"]

#Assigning a value
city["Perth"] = 2600000

if "New York City" in city:
    print("success")


  
#LOOPING TECHNIQUES
for key in city:
    print(key)
    
for value in city:
    print(key)
    
for key in city.iterkeys():
    print(key)
    
for val in city.itervalues():
    print(val)
    
for key in city:
    print(city[key])

for key, value in city.items():
    print(key, value)







#FUNCTIONS
len(city)
list(city)
sorted(city.values())
sorted(city, key=city.__getitem__, reverse=False)
max(city, key=city.get)
min(city, key=city.get)




#OTHER USEFUL TRICKS
# copy a complete dictionary
x = city.copy()
print(x)

#sorting keys and accessing their values in order
keys = city.keys()
keys.sort()
for key in keys:
    print(city[key])
