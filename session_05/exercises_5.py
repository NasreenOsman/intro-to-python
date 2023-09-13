# Session 5 Exercises

## Section A
# 1. Print 10 random numbers.

import random
for number in range(10): 
  print(random.randint(1,10))


# 2. Keep asking the user to enter a number until they enter the number 7, then print "Wow lucky number 7!".

guess = int(input("Please input a number: "))
while guess !=7:
  guess = int(input("please input a number: "))
  if guess == 7: 
    print("Wow, lucky number 7")
    break
    
#     - Rewrite so that the number being guessed is a random value from 1 to 10 instead of number 7 .

guess = int(input("Please input a number: "))
while guess < 0 or guess > 10:
  guess = int(input("please input a number: "))
  if guess > 0 and guess < 10: 
    print("Wow, lucky number ")
    break


# 3. The area of a rectangle is width multiplied by height. Ask the user to enter a width and height in cm, then print the area to the whole square metre. 
#   E.g. 240cm x 80cm = 19200cm2 = 2m2.

width = int(input("Please enter width of rectangle in cm: "))
height = int(input("Please enter height of rectangle in cm: "))
print("The area of the rectangle is " + str(width*height) + " cm squared ")


# 4. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure" and then ask them to enter it again. 
#   Only allow them to enter the password wrong 3 times before printing "System Locked!".

password =(input("please enter your password: "))
user_guess = 0
if password == "qwerty123":
  print("You have successfully logged on.")

while user_guess <2:
  if password == "qwerty123":
    print("You have successfully logged on.")
    break
  else: print("Password failed") 
  user_guess +=1
  password = input("Please enter your password: ")
    

if user_guess==2:
    print("System locked")




# 5. Add up all the numbers from 1 to 500 and print the answer.
total = 0
for my_number in range(0,501):
  total +=my_number
  print(total) 




# 6. Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list. 
#   Find the index at which the user entered the number 99.
list8=[]
n=0
while n<10:
  numbers = int(input("Please input 10 numbers, one of the numbers should be the number 99: "))
  list8.append(numbers)
  n= n+1

y = list8.index(99)
print("The number 99 appears at position " +str(y + 1))
  




# 7. Print a multiplication table for the number 18 up to 15. E.g.
#     1 x 18 = 18
#     2 x 18 = 36
for each_number in range(1,16):
  z = each_number*18
  print(str(each_number) +" x 18 = " + str(z))


# 8. Print the numbers 1 to 100 (including the number 100) using a while loop.
n=0
while n<101:
  print(n)
  n +=1


# 9. Rewrite question B8 from session 3 using a while loop
#     - A school has following rules for their grading system:
#         a.	Above 80 – A
#         b.	60 to 80 – B
#         c.	50 to 60 – C
#         d.	45 to 50 – D
#         e.	25 to 45 – E
#         f.	Below 25 - F
#     Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.
lesson = input("please input your lesson: ")
mark = int(input("Please input your mark "))

if mark < 25:
    print("You have obtained an F" )
elif mark <45:
        print("you have obtained an E")
elif mark <50:
        print("you have obtained an D")
elif mark <60:
        print("you have obtained an D")
elif mark <80:
        print("you have obtained an B")
elif mark <100:
        print("you have obtained an A")
else: print("please get your marks")



# 10. Ask the user to enter the names of people who entered a prize draw. Select a random winner and print their name
import random
list =[]
names = None 

for x in range(5): 
  names = input("please enter names of people who entered the draw:\n ")  
  list.append(names)

print(random.choice(names))



# 11. Create a rock, paper, scissors game which is run against computer. 
#    This is a game where you select either rock/paper/scissors and you compare it to your opponents choice. 
#    Rock beats scissors, paper beats rock, scissors beats paper. If both choose the same, then you play again.
#       + Expand this so that its best of 3 games

user_score = 0
computer_score = 0
import random

for x in range(3): 
  user_turn=(input("Please input either rock, paper or scissors: "))
  computer_turn = random.choice(["rock", "paper", "scissors"])
  print("The computer picked " + computer_turn)
  if user_turn == "rock":
    if computer_turn == "scissors":
      print("you win")
      user_score +=1
    elif computer_turn == "paper":
      print("you lose")
      computer_score +=1
    else: print("Its a draw")

  if user_turn == "scissors":
    if computer_turn == "paper":
      print("you win")
      user_score +=1
    elif computer_turn == "rock":
      print("you lose")
      computer_score +=1
    else: print("Its a draw")

  if user_turn == "paper":
    if computer_turn == "rock":
      print("you win")
      user_score +=1
    elif computer_turn == "scissors":
      print("you lose")
      computer_score +=1
    else: print("Its a draw")

print("The computer scored " + str(computer_score) + " and your score = " +str(user_score))
