import pprint
import csv
import xml.dom.minidom
from xml.dom.minidom import Node

result = open("newfile.csv",'wb')
writer = csv.writer(result, dialect = 'excel')

doc = xml.dom.minidom.parse ("pokemon.xml")

for node in doc.getElementsByTagName("pokemon"):
    pokedex_number = node.getElementsByTagName("pokedex_number")[0]
    pokedexVal = pokedex_number.childNodes[0].data
    
    species = node.getElementsByTagName("species")[0]
    speciesVal = species.childNodes[0].data
    
    atk_stats = node.getElementsByTagName("atk")[0]
    attack = atk_stats.childNodes[0].data
    
    def_stats = node.getElementsByTagName("def")[0]
    defense = def_stats.childNodes[0].data
    
    satk_stats = node.getElementsByTagName("satk")[0]
    sattack = satk_stats.childNodes[0].data
    
    sdef_stats = node.getElementsByTagName("sdef")[0]
    sdefense = sdef_stats.childNodes[0].data
    
    speed_stats = node.getElementsByTagName("spd")[0]
    speed = speed_stats.childNodes[0].data
    
    types = node.getElementsByTagName("type")[0]
    types = types.childNodes[0].data
    health = "100"
    
    myTuple = (pokedexVal, speciesVal, types, attack, defense, sattack, sdefense, speed, health)
    print(myTuple)
    writer.writerow(myTuple)

result.close

