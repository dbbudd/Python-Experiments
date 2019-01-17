class Pokemon(object):
    def __init__(self, number, name, species, HP, attack):
        self.number = number
        self.name = name
        self.species = species
        self.HP = int(HP)
        self.attack = int(attack)
    
    
def typeadvantage(poke1, poke2):
    if poke1.species=="Fire" and poke2.species=="Water" or poke1.species=="Earth" and poke2.species=="Fire" or poke1.species=="Water" and poke2.species=="Earth":
        print("Pokemon 1 has an elemental advantage over Pokemon 2")
    elif poke1.species=="Fire" and poke1.species=="Water" or poke2.species=="Earth" and poke2.species=="Fire" or poke2.species=="Water" and poke1.species=="Earth":
        print("Pokemon 2 has an elemental advantage over Pokemon 1")
    else:
        print("There are no elemental advantages in this battle.")

def typeadvantagebattle(poke1, poke2):
    if poke1.species=="Fire" and poke2.species=="Water" or poke1.species=="Earth" and poke2.species=="Fire" or poke1.species=="Water" and poke2.species=="Earth":
        return poke1.attack * 1.2
    elif poke2.species=="Fire" and poke1.species=="Water" or poke2.species=="Earth" and poke1.species=="Fire" or poke2.species=="Water" and poke1.species=="Earth":
        return poke1.attack * .8
    else:
        return poke1.attack
    
def battletime(poke1, poke2):
    beatmonster2hits = 0
    
    while poke2.HP > 0:
        beatmonster2hits +=1
        poke2.HP -= typeadvantagebattle(poke1, poke2)
    print ("It took", beatmonster2hits, "hits to beat Pokemon 2.")
    
    beatmonster1hits = 0
    
    while poke1.HP > 0:
        beatmonster1hits += 1
        poke1.HP -= typeadvantagebattle(poke2, poke1)
    print ("It took", beatmonster1hits, "hits to beat Pokemon 1.")
    
    if beatmonster1hits > beatmonster2hits:
        print("Pokemon 1 is stronger than Pokemon 2.")
    elif beatmonster1hits < beatmonster2hits:
        print("Pokemon 2 is stronger than Pokemon 1.")
    else:
        print("Monsters are of equal strength")

my_pokemon = Pokemon('1', 'Pikachu', 'Earth', 200, 100)
enemy = Pokemon('2', 'Squirtle', 'Water', 100, 100)
print("")
print(my_pokemon.name + "  VS. " + enemy.name)
print("")

typeadvantage(my_pokemon, enemy)
battletime(my_pokemon, enemy)
      
      
      
      
      
      
      
      