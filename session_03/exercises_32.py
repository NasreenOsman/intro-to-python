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
  
  