#Game for children between the ages of 3 - 5
#Children can enter either an alphabet (game 1) or a number (game 2) and the app will output results of whether the entered value is a consonant for vowel. If its a number, the app will output results of whether the number is odd or even. 
#I added game 3 since I did not use an import function in either game 1 or 2. 

#1 Alphabet game

print("Lets Start!")

vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

no_of_turns_alphabets = 0

alphabet = 0 

while no_of_turns_alphabets < 3:
  alphabet = input("Please enter an alphabet: ")
  consonants = open("consonants.txt", "r")
  content = consonants.read()
  if alphabet == "" and no_of_turns_alphabets <=1:
    print("Please try again: ")
  elif alphabet == "" and no_of_turns_alphabets ==2:
    print("Please try again in the next round: ")
  elif alphabet in vowels: 
    print("This is a vowel.")
  elif alphabet in content: 
    print("This is a consonant. ")      
  else: print ("This is not an aphabet. Please try again.  ")
  no_of_turns_alphabets +=1

consonants.close()


#2 Number game

print("Now lets play a number game!")

no_of_turns_numbers = 0

#define function
def is_odd(number):
  if number % 2 == 0:
    print(str(number) +" is an even number.")
  else: print(str(number) +" is an odd number")

  
while no_of_turns_numbers <3: 
  number = input("Please enter a number between 1 and 100: ")
  number_check = open("not_numeric.txt", "r")
  numbers = number_check.read()
  if number in numbers: 
    print("This is not a number, please try again.")
  elif int(number) == 0:
    print("Please enter another number.")
  else: is_odd(int(number))
  
  no_of_turns_numbers +=1

number_check.close()

#3 Rounding game

print("Now lets play a rounding game! ")

from math import floor, ceil

guess2 = float(input("Please enter any number with a decimal: "))

answer = input("Would you like to round up the number or down the number, write U for Up or D for Down? ")

if answer == "U": 
  print("Your rounded off number is " + str(ceil(guess2)))

elif answer == "D": 
  print("Your rounded off number is " + str(floor(guess2)) + ".")




 




