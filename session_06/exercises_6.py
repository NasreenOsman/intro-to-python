# Session 6 Exercises

## Section A
# 1. Create the following dictionary for an apple: Type = "Bramley", Price = 0.39, Colour = "Green".
apple = {
  "type": "Bramley",
  "price": 0.39,
  "colour": "green"
}
print(apple)


# 2. Add the best before date to the dictionary - print the dictionary.
apple["best before date"] = "08/09/23"
print(apple)


# 3. Change the price to 0.41 - print the dictionary.
apple["price"] = 0.41
print(apple)


# 4. Set the apple to be on offer using a Boolean - print the dictionary.
apple["offer"] = True
print(apple)


# 5. The offer has now expired, remove the key/value from the dictionary - print the dictionary.
del(apple["offer"])
print(apple)



# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask the user to enter a persons name, if they enter a name, ask for the persons age. Store this information in a dictionary inside a list. 
#   Continue to ask for names until no name is given. Then print out all of the names and ages collected.
name = 0
age = 0 
names = []
while name !="":
  name = input("Please enter your name: ")
  age = input("please enter your age: ")
  if name and age: 
    names.append(
    {
    "name": name,
    "age": age
    }
  )
  print(names)


# 2. Create a restaurants menu with 5 items. Store this information in a dictionary inside a list. 
#   Each item in the menu should have the name of the item, the price and if it's vegetarian friendly (make at least one vegetarian friendly dish). 
#   Print out the entire menu. Print out the name of the vegetarian option(s).

menu = [
  {"Fruit", "Price = £1", "Veg"},
  {"Curry", "Price = £3"},
  {"Fish", "Price =£4"},
  {"Chicken", "Price = £5"},
  {"Beef", "Price = £6"}
]
print(menu)

for item in menu: 
  if "Veg" in item: 
      print(item)

# 3. The beetle game is a dice game where depending on what you roll is how much of the beetle you can draw.
#   If you roll a 6, you can draw the body
#   If you roll a 5, you can draw the head
#   If you roll a 4, you can draw the legs (but remember, you cannot draw legs without a body)
#   If you roll a 3, you can draw the antenna (but remember, you cannot draw antenna without a head)
#   If you roll a 2, you can draw the eyes (but remember, you cannot draw eyes without a head)
#   If you roll a 1, you can draw the mouth (but remember, you cannot draw a mouth without a head)
#   You need 6 legs, 2 antenna, 2 eyes, 1 mouth.
#   The player to complete the beetle in the fewest rolls of the dice wins. Create the beetle game.

dice_roll = 0 
dice_turns = 0

while dice_turns < 10: 
  dice_roll = int(input("Please roll the dice and input your result here: "))
  if dice_roll == 6:
    print("You rolled a 6, you can draw the beetles body")
  elif dice_roll == 5:
    print("You rolled a 5, you can draw the beetles head")
  elif dice_roll == 4: 
    print("You rolled a 4, you can draw the beetles legs, but remember, you can't draw the legs without a body")
  elif dice_roll == 3: 
    print("You rolled a 3, you can draw the beetles antenna but remember, you can't draw the anetenna without a body")
  elif dice_roll == 2: 
    print("You rolled a 2, you can draw the beetles eyes, but remember, you can't draw the eyes without a body")
  elif dice_roll == 1: 
    print("You rolled a 1, you can draw the beetles mouth, but remember, you cand draw the mouth without a body")
  dice_turns += 1
  
beetle = input("Is your beetle complete (Y / N): ")
if beetle == "Y": 
  print("you took " + str(dice_turns) + " turns to complete the beetle. Next player, it's your turn now. ")
else: print("Game over, please play again.")

    
  