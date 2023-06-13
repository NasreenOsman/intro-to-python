# Session 2 Exercises

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. 
height =input("what is the height of rectangle: ")
width =input("what is the width of the rectangle: ")
area =int(height)*int(width)

# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.
print("Rectangle of width " + str(width)+ " and height " + str(height) + " has an area of " + str(area))



# 2. Write code that prints the length of the string, 'python'.
print(len("python"))


# 3. Print out the first and third letter of the word 'python'.
print("python"[0:4:2])



# 4. Ask the user to enter their name, and print out `Hello, <name>`.
name = input("What is your name: ")
print("Hello " + name)


# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.
age = input("What is your age: ")
age_in_15_years = int(age) + 15
print("In 15 years, you will be " + str(age_in_15_years) +" years old.")



# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. 
#   In 15 years time you will be <age_in_15_years_time>`.
print("Hello " + name + ", you are currently " + age + " years old. In 15 years, you will be " + str(age_in_15_years) +" years old.")



# 7. Ask the user to enter their hometown, print it out in uppercase letters.
hometown = input("What is your hometown? ")
print(hometown.upper())


# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.
colour = input("What is your favorite colour? ")
print(len(colour))



# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.
weather = input("What is the weather today? ")
month = input("What month is it? ")
print("It is " + month + " and it is "+ weather +" today.")



# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string: 
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.
temp1 = input("What was the temperature 2 days ago? ")
temp2 = input("What was the temperature yesterday? ")
temp3 = input("What is today's temperature? ")
temp4 = input("What is the forecast temperature for tomorrow? ")
temp5 = input("What is the forecast temperature for the day after tomorrow? ")
average = (float(temp1) + float(temp2) + float(temp3) + float(temp4) + float(temp5))/5

print("It is " + month + " and the average temperature is " + str(average) + " degrees celcius.")




# 11. Print out the above sentence but make the month upper case.
print("It is " + month.upper() + " and the average temperature is " + str(average) + " degrees celcius.")


# 12. Create a variable that holds your favourite animals and print it out. 
#    Make sure the animals are all on different lines and tabbed.
favourite_animals = "Dog\t\nCat\t\nfish"
print(favourite_animals)



# 13. Ask the user to enter their name as well as a number. 
#    Print out the uppercase character at that position in the string.
fname=input("What is your name? ")
fname_length=len(fname)
fnumber=int(input("Pick a number between 1 and "+ str(fname_length) +" ? "))
print(fname[fnumber].upper())




# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".
print("WelcometoPython"[1:-2:2])
