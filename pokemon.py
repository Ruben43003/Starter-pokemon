#Starter_pokemon_dialogue
#Disclaimer: answers must be insrted after 1 space AND capitalize first letter
print("Hi my name is professor Oak! This is the start to your journey as a pokemon trainer. Please select one of the pokemon here at this lab.")
print("")
print("*Type knowldedge: There are many different pokemon types.")
print("The starters are either")
print("Fire")
print("Water")
print("Grass")
print("Electric")
print("")
print("Fire is Super Effective against Grass")
print("Water is Super Effective against Fire")
print("Grass is Super Effective against Water")
print("*Electric type is not enhanced against any of the listed types")
print("")

#Starter_pokemon_choices
starter_pokemon_list = [["Option 1.","Charmander", "Fire type"], ["Option 2.","Bulbasaur", "Grass type"], ["Option 3.","Squirtle", "Water type"]]
starter_pokemon_list.append(["Option 4","Pikachu", "Electric type", "Lv.1"])
print("Here I have ", str(len(starter_pokemon_list)), "Pokeballs, please select one and choose a Starter Pokemon.")

for starter_pokemon in starter_pokemon_list:
  print(starter_pokemon)
starter_pokemon = input("Choose a pokemon:")
if starter_pokemon == " Charmander":
  print("You chose Charmander! The Fire type pokemon.")
elif starter_pokemon == " Bulbasaur":
  print("You chose Bulbasaur! The Grass type pokemon.")
elif starter_pokemon == " Squirtle":
  print("You chose Squirtle! The Water type pokemon.")
elif starter_pokemon == " Pikachu":
  print("You chose Pikachu! The Electric type pokemon.")
else: 
  print("Please select a pokemon.")

#rival_chooses
print("")
print("")
print("Your rival Gary is about to choose...")
rival_1 = "Gary"

if starter_pokemon == " Charmander":
  rival_1_pokemon = "Squirtle"
  print(rival_1,"chose the Water type pokemon Squirtle.")
elif starter_pokemon == " Bulbasaur":
   rival_1_pokemon = "Charmander"
   print(rival_1, " chose the Fire type pokemon Charmander.")
elif starter_pokemon == " Squirtle":
   rival_1_pokemon = "Bulbasaur"
   print(rival_1, "chose the Grass type pokemon Bulbasaur.")
elif starter_pokemon == " Pikachu":
   rival_1_pokemon = "Charmander"
   print(rival_1, "chose the Fire type pokemon Charmander.")

#starter_pokemon_attack_list
charmander_attack_list = [["Fire punch"], ["Bite"]]
squirtle_attack_list = [["Bubble beam"], ["Tackle"]]
bulbasaur_attack_list = [["Leech seed"], ["Whip"]]
pikachu_attack_list = [["Electro ball"], ["Intimidate"]]

#Battle_commentary 
print("")
print("You and ", rival_1, "are about to batlle!")
print(rival_1, "sends out",rival_1_pokemon,".")

#Fight_sequence
print("")
print("What will you do?")
battle_options_list = [" Fight", "Run"]
print(battle_options_list)
battle_options = input("Select one :")
winning_statement_1 = "Congratulations you won your first pokemon battle!"
losing_statement_1 = "You lost."

if battle_options == " Fight":
  print("")
  print("Battle begins!")
  print("")
  print("Go",starter_pokemon, "!")
  if starter_pokemon == " Charmander":
    print(charmander_attack_list)
    attack = input("Choose an attack :")
    if attack == " Bite":
      print("")
      print("Woah that did alot of damage!", str(rival_1_pokemon), " has fainted.")
      print("")
      print(winning_statement_1)
    elif attack == " Fire punch":
      print("Ineffective!")
      print("Its ", rival_1, "'s turn...")
      print(rival_1_pokemon,"uses water beam!")
      print("Water beam was Super Effective!", starter_pokemon,"has fainted.")
      print("")
      print(losing_statement_1)
  
  if starter_pokemon == " Bulbasaur":
    print(bulbasaur_attack_list)
    attack = input("Choose an attack :")
    if attack == " Whip":
      print("")
      print("Woah that did alot of damage!", str(rival_1_pokemon), " has fainted.")
      print("")
      print(winning_statement_1)
    elif attack == " Leech seed":
      print("Ineffective!")
      print("Its ", rival_1, "'s turn...")
      print(rival_1_pokemon,"uses Fire puch!")
      print("Fire punch hurt alot!", starter_pokemon,"has fainted.")
      print("")
      print(losing_statement_1)
  if starter_pokemon == " Squirtle":
    print(squirtle_attack_list)
    attack = input("Choose an attack :")
    if attack == " Tackle":
      print("")
      print("Woah that did alot of damage!", str(rival_1_pokemon), " has fainted.")
      print("")
      print(winning_statement_1)
    elif attack == " Bubble beam":
      print("Ineffective!")
      print("Its ", rival_1, "'s turn...")
      print(rival_1_pokemon,"uses Leech seed!")
      print("Leech seed did some major damage!", starter_pokemon,"has fainted.")
      print("")
      print(losing_statement_1)
  if starter_pokemon == " Pikachu":
    print(pikachu_attack_list)
    attack = input("Choose an attack :")
    if attack == " Electro ball":
      print("")
      print("Woah that did alot of damage!", str(rival_1_pokemon), " has fainted.")
      print("")
      print(winning_statement_1)
    elif attack == " Intimidate":
      print("Ineffective!", rival_1_pokemon, "was not intimidated.")
      print("Its ", rival_1, "'s turn...")
      print(rival_1_pokemon,"uses Fire blast!")
      print("Stong hit!", starter_pokemon,"has fainted.")
      print("")
      print(losing_statement_1)
elif battle_options == " Run":
  print("You ran away.") 





