#!/usr/bin/python


#http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/
# Introduction to to Classes and Inheritance (in Python)

class Pokemon(object):
    def __init__(self, number, name, species, XP, Attack, Health):
        self.number = int(number)
        self.name = name
        self.species = species
        self.XP = int(XP)
        self.Attack = int(Attack)
        self.Health = int(Health)
        
    def getName(self):
        return self.name
    
    def getSpecies(self):
        return self.species
    
    def __str__(self):
        return ("%s is a %s Pokemon" % (self.name, self.species))

class spElec(Pokemon):
    def __init__(self, number, name, is_elec, XP, Attack, Health):
        Pokemon.__init__(self, 1, name, "Electric", XP, Attack, Health)
        self.is_elec = is_elec
        
    def is_elec(self):
        return self.is_elec

class spWater(Pokemon):
    def __init__(self, number, name, is_water, XP, Attack, Health):
        Pokemon.__init__(self, 1, name, "Water", XP, Attack, Health)
        self.is_water = is_water
        
    def is_water(self):
        return self.is_water

class spFire(Pokemon):
    def __init__(self, number, name, is_fire, XP, Attack, Health):
        Pokemon.__init__(self, 1, name, "Fire", XP, Attack, Health)
        self.is_fire = is_fire
        
    def is_fire(self):
        return self.is_fire
    
class spEarth(Pokemon):
    def __init__(self, number, name, is_earth, XP, Attack, Health):
        Pokemon.__init__(self, 1, name, "Earth", XP, Attack, Health)
        self.is_earth = is_earth
        
    def is_earth(self):
        return self.is_earth


#####
## USING THE CLASSES
#####
from pokeObj import spElec

my_Pikachu = spElec(1, "Pikachu", True, 10, 10, 100)
my_Squirtle = spWater(2, "Squirtle", True, 10, 10, 100)
my_Charmander = spFire(3, "Charmander", True, 10, 10, 100)
my_Jiggly = spEarth(4, "Jiggly Puff", True, 10, 10, 100)

print(my_Jiggly)
print(my_Jiggly.Health)
print(my_Jiggly.getSpecies)

my_Jiggly.Health = my_Jiggly.Health - 10
print(my_Jiggly.Health)