class Pokemon(object):
    def __init__(self, number, name, species, HP, attack):
        self.number = number
        self.name = name
        self.species = species
        self.HP = int(HP)
        self.attack = int(attack)

'''
my_pika = Pokemon('1', 'Daniel', 'Earth', 200, 100)

print (my_pika.name)

print(my_pika.HP)
my_pika.HP = my_pika.HP + 10
print(my_pika.HP)
'''