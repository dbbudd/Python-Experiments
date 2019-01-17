#!/bin/python


## Todo #################################################
# choice for attacks									#
# each pokemon has a diffrent attack set				#
# more battles, maybe a tournament system				#
# more choices for items, instead of just a potion		#
#########################################################

## Modules
from random import uniform
from random import randint
from sys import exit
import readline

## Declarations
pokemons = ["Pickachu", "Rattata", "Abra", "MewTwo", "Zubat", "Richard Stallman", "Mew"]
my_pokemons = ["Charizard", "Bulbusaur", "Blastoise", "Zubat"]

attacks = ["Claw", "Cut", "Vine", "Tailswipe", "Weed", "Hurt"]
genders = ['boy', 'girl', 'shemale']

potion_count = 10
enemy_potion_count = 10

my_hp = 100
enemy_hp = 100


## Functions
def answer():
	global ans
	ans = raw_input(">> ").lower()
	if ans == "quit":
		print "you entered %s, exiting now" % ans
		exit(0)
	return ans

def start_battle():
	global enemy
	global battle_on
	battle_on = True
	count = len(pokemons) - 1
	enemy = pokemons[randint(0,count)]
	print "A wild %s appeared!" % enemy
	return enemy

def menu(section):
	if section == "general":
		print "Attack, Potion, Flee"
	elif section == "items":
		for i in items:
			print i
	else:
		print "unexpected argument for function menu(): %s"  % where
		exit(0)

def attack(user, target):
	global damage
	attack = attacks[int(uniform(0,5))]
	print "%s used %s on %s" %(user, attack, target)
	effect = uniform(0,1000)

	if  0 < effect < 100:
		print "No effect!"
		damage = 0
	elif 100 < effect < 500:
		print "Its Effective!"
		damage = 10
	elif 500 < effect < 800:
		print "Critical Strike!"
		damage = 15
	elif  800 < effect < 1000:
		print "ITS SUPER EFFECTIVE, OUCH!"
		damage = 20
	else:
		print "Error at function attack(), exiting"
		exit(0)
	return damage

def calc_hp(pokemon, action):
	global enemy_hp
	global my_hp
	if pokemon == enemy:
		if action == "attack":
			enemy_hp -= damage
		elif action == "heal":
			enemy_hp += 10
		if enemy_hp <= 0:
			win("victory")
		elif enemy_hp > 100:
			enemy_hp = 100
	elif pokemon == my_pokemon:
		if action == "attack":
			my_hp -= damage
		elif action == "heal":
			my_hp += 10
		if my_hp <= 0:
			win("loss")
		elif my_hp > 100:
			my_hp = 100
	else:
		print "unexpected argument for calc_hp function, exiting..."
		exit(0)
	return


def classic():
	global name
	global gender
	global rival
	print """Hi im Professor Anon and we live in a magical world filled with pokemons
Whats your name?"""
	name = answer()
	print """Nice to meet you %s
Are you a Boy or a Girl?""" % name
	looping = True
	while looping:
		gender = answer()
		if gender in genders:
			print "I see, so your a %s!" % gender
			looping = False
		else:
			print "lol thats not a gender you idiot!"

	print """This is my grandson, i forgot his name lol
Can you remind me of his name?"""
	rival = answer()
	print "Ah, now i remember, his name is %s!" % rival

def pokemon_choice():
	global my_pokemon
	print "What kind of pokemons do you like?"
	print "Fire, Water or Grass?"
	loop = True
	while loop:
		choice = answer()
		if choice == "fire":
			my_pokemon = my_pokemons[0]
			loop = False
		elif choice == "water":
			my_pokemon = my_pokemons[1]
			loop = False
		elif choice == "grass":
			my_pokemon = my_pokemons[2]
			loop = False
		else:
			print "Im not sure what you mean, lets try again"

	print "%s it is, your new pokemon is %s!" %(choice, my_pokemon)

def enemy_action():
	global enemy_hp
	global enemy_potion_count
	
	if enemy_potion_count > 0:
		act = int(uniform(0,11))
	else:
		act = 1

	if act < 7:
		attack(enemy, my_pokemon)
		calc_hp(my_pokemon, "attack")
		show_hp(my_pokemon)
	else:
		use_potion(enemy)
def win(reason):
	if reason == "victory":
		print "%s has fainted!" % enemy
		print "You win!"
		exit(0)
	elif reason == "loss":
		print "%s has fainted!" % my_pokemon
		print "You Lose!"
		exit(0)
	elif reason == "flee":
		print "%s has left the building!" % my_pokemon
		exit(0)
	else:
		print "unexpected argument for the win function, exiting now..."
		exit(0)

def use_potion(target):
	global my_hp
	global enemy_hp
	global potion_count
	global enemy_potion_count
	if potion_count <= 0:
		print "You dont have any more potions!"
		return
	if target != my_pokemon and target != enemy:
		print "Wrong Argument for the use potion function, exiting!"
		exit(0)
	
	print "%s used a Potion!" % target
	if target == my_pokemon:
		calc_hp(my_pokemon, "heal")
		potion_count -= 1
		print "You have %d potions left!" % potion_count
	elif target == enemy:
		calc_hp(enemy, "heal")
		enemy_potion_count -= 1
		print "%s has %d potions left!" %(enemy, enemy_potion_count)
	show_hp(target)

def show_hp(who):
	if who != my_pokemon and who != enemy:
		print "Wrong argument for the show hp function, exiting now!"
		exit(0)
	if who == my_pokemon:
		hp = my_hp
	elif who == enemy:
		hp = enemy_hp
	print "%s's HP is %d" %(who, hp)

def user_action():
	### This is the function that takes and executes the users choices
	"""No arguments, it just interactes directly with the user"""
	while battle_on:
		choosing = True
		while choosing:
			menu("general")
			answer()
			if ans == "attack":
				attack(my_pokemon, enemy)
				calc_hp(enemy, "attack")
				show_hp(enemy)
				print " "
				return
			elif ans == "flee":
				chance = uniform(0, 100)
				if chance > 90:
					win("flee")
				else:
					print "You failed to escape!"
					return
			elif ans == "potion":
				use_potion(my_pokemon)
				return
			else:
				print "i dont know what you mean :)"
				print "lets try again!"
				choosing = True
					


def not_implemented():
	print "This function is not yet implemented, be patient!"
	return

## Program starts Here
if __name__ == "__main__":
	classic()
	pokemon_choice()
	print "Now lets send you out to the wild and see what you can do"
	start_battle()
	while True:
		user_action()
		print "Enemy Turn!"
		raw_input('...')
		enemy_action()
		print "\n---------------------------------------------"
		print "Current HP is: [Enemy %s: %d; You %s: %d]" %(enemy, enemy_hp, my_pokemon, my_hp)
		print "---------------------------------------------\n" # i know it wont match
