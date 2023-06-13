# Session 3 Exercises

## Section A
# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".
name = input("What is your name? ")
if name == "Bob":
  print("Welcome Bob")


# 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".
name2 = input("What is your name? ")
if name2 != "Alice":
  print("You're not Alice")



# 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure".
password = input("Please enter your password: ")
if password == "qwerty123":
    print("You have successfully logged on")
else: print("Password failure")



# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".
number = int(input("Please enter a number: "))
if number % 2 == 0:
    print("You have entered an even number.")
else: print ("You have entered an odd number.")




# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a second number: "))
if num1 + num2 > 21:
  print("Bust")
else: print("Safe")



# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.
length = int(input("Please enter the length of the shape: "))
width = int(input("Please enter the width of the shape: "))
if length==width: 
  print("This shape is a square. ")
else: print("This shape is not a square.")



# 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. 
#   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
years = int(input("Please input years of service: "))
salary = int(input("Please input salary: "))
if years > 3: 
  print("Your salary is " +str(salary) + " and your bonus is " + str(salary*0.1))
else: print("You are not eligible for a bonus due to being employed for less than 3 years. ")



# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.
num4 = int(input("Please enter a whole number: "))
if num4 > 0: 
  print(str(num4**3))
else: print(str(num4/2))




# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", 
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".
name3 = input("Please enter your name: ")
if name3 == "Alice":
  print("Hello, Alice.")
elif name3 == "Bob": 
  print("You're not Bob, I'm Bob.")
else: print("You must be Charlie.")


# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"
age=int(input("How old are you? "))
if age == 0:
  print("You're not born yet.")
elif age < 11:
  print("You're too young to go to this school.")
elif 11<age< 16:
  print("You can come to this school.")
elif age> 16:
  print("You're too old for this school.")


# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".
month = input("Please provide the name of the month: ")
if month == "March" or month == "April" or month == "May" or month == "march" or month == "april" or month == "may":
  print(month +" is in Spring")
elif month == "June" or month == "July" or month == "August" or month == "june" or month == "july" or month == "august": 
  print(month +" is in Summer")
elif month == "September" or month == "October" or month == "November" or month == "september" or month == "october" or month == "november":
  print(month +" is in Autumn")
elif month == "December" or month == "January" or month == "February" or month == "december" or month == "january" or month == "february": 
  print(month +" is in Winter")
else: print("I don't know")


# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.
num5 = int(input("Please provide a number: "))
num6 = int(input("Please provide a number: "))
if (num5%2 == 0 and num6%2 == 0):
  print("Even")
elif (num5%2 != 0 and num6%2!= 0):
  print("Odd")
else: print(str(num5*num6))


# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.
num7 = int(input("Please input a number: "))
num8 = int(input("Please input another number: "))
if num7>num8:
  print(str(num7) + " has the highest value")
elif num8>num7:
  print(str(num8 )+ " has the highest value")
else: print("Both numbers are equal")

# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years, 
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years. 
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
salary = int(input("What is your salary? "))
service = int(input("How many years have you worked for us? "))

if 3<=service<=5:
  print("Your salary is £" + str(salary) + " and your bonus is £" + str(0.10*salary))
elif  5<service<7:
  print("Your salary is £" + str(salary) + " and your bonus is £" + str(0.15*salary))
elif service>=7:
  print("Your salary is £" + str(salary) + " and your bonus is £" + str(0.20*salary))
else: print("Your salary is £" + str(salary) + ". You are not entitled to receive a bonus.")


# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. 
#   If all three ages are the same, print that.

name1= input("Please input the name of Person 1: ")
age1 = int(input("Please input the age of Person 1: "))
name2 = input("Please input the name of Person 2: ")
age2 = int(input("Please input the age of Person 2: "))
name3 = input("Please input the name of Person 3: ")
age3 = int(input("Please input the age of Person 3: "))

#oldest
if age1 > age2 and age1 > age3:
  print(name1 + " is the oldest and is " + str(age1) + " years old")
elif age2 > age1 and age2> age3:
    print(name2 + " is the oldest and is " + str(age2) + " years old")
 
elif age3 > age1 and age3>age2:
    print(name3 + " is the oldest and is " + str(age3) + " years old")

#youngest
if age1<age2 and age1<age3:
  print(name1 + " is the youngest and is " + str(age1) + " years old")
  
elif age2<age3 and age2<age1:
    print(name2 + " is the youngest and is " + str(age2) + " years old")
 
elif age3<age1 and age3<age2:
    print(name3 + " is the youngest and is " + str(age3) + " years old")
else: print("You are all the same age.")
  


# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
#   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.
lesson1 = input("Please input the name of Lesson 1: ")
mark1 = int(input("Please input grade obtained for " + lesson1 +": "))
lesson2 = input("Please input the name of Lesson 2: ")
mark2 = int(input("Please input grade obtained for " + lesson2+": "))
lesson3 = input("Please input the name of Lesson 3: ")
mark3 = int(input("Please input grade obtained for " + lesson3+": "))

if mark1<25:
  print("You obtained an F for " + lesson1)
elif 25<=mark1<45:
  print("You obtained an E for " + lesson1)
elif 45<=mark1<50:
  print("You obtained a D for " + lesson1)
elif 50<=mark1<60:
  print("You obtained a C for " + lesson1)
elif 60<=mark1<80:
  print("You obtained a B for " + lesson1)
elif 80<=mark1<100:
  print("You obtained an A for " + lesson1)

if mark2<25:
  print("You obtained an F for " + lesson2)
elif 25<=mark2<45:
  print("You obtained an E for " + lesson2)
elif 45<=mark2<50:
  print("You obtained a D for " + lesson2)
elif 50<=mark2<60:
  print("You obtained a C for " + lesson2)
elif 60<=mark2<80:
  print("You obtained a B for " + lesson2)
elif 80<=mark2<100:
  print("You obtained an A for " + lesson2)
  
  
if mark3<25:
  print("You obtained an F for " + lesson3)
elif 25<=mark3<45:
  print("You obtained an E for " + lesson3)
elif 45<=mark3<50:
  print("You obtained a D for " + lesson3)
elif 50<=mark3<60:
  print("You obtained a C for " + lesson3)
elif 60<=mark3<80:
  print("You obtained a B for " + lesson3)
elif 80<=mark3<100:
  print("You obtained an A for " + lesson3)