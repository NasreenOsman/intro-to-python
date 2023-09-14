# Session 7 Exercises

## Section A
# 1. Write a function that prints your name



# 2. Write a function that accepts a name as a parameter and prints "Hello, <name>".
#name2 = input("Please input your name: ")


# 3. Loop through the list ["Alice", "Bob", "Charlie"] and call the function you just wrote.
#list =["Alice", "Bob", "Charlie"]

#def Helloname():
    #print("Hello " + name)

#for name in list:
  #Helloname()
   


# 4. Write a function that prints the area of two passed in parameters.

#a = int(input("please input paramter 1: "))
#b = int(input("please input paramter 2: "))

#def area():
  #print("Area = " + str(a * b) + " meters squared ")

#area()


# 5. Write a function called 'print_list' that accepts a list as a parameter and then prints out each item of the list.

#def print_list(lists):
  #for item in lists: 
    #print(item)

#lists = ["Bag", "Books", "Shoes"]

#print_list(lists)


# 6. Put the following into a function that accepts age as a parameter:
#     1. If they are younger than 11, print "You're too young to go to this school".
#     2. If they are between 11 and 16, print "You can can come to this school".
#     3. If they are over 16, print 'You're too old for school".
#     4. If they are 0, print "You're not born yet!".

#age = int(input("please input your age: "))

#def agefunction():
  #if age == 0: 
    #print("you are not born yet. ")
  #elif age < 11: 
    #print("You're too young to go to this school.")
  #elif 11<age<16: 
    #print("You can can come to this school")
  #else: print("You are too old for this school. ")

#agefunction()


# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Write a function called is_odd that will return True or False if the integer passed as a parameter is odd (hint: x % 2 will return true for all odd numbers).


# 2. Write a function that accepts a word and returns it backwards, e.g. 'hello' -> 'olleh'.

#def printbackwards(word):
  #reverse = word[::-1]
  #print(reverse)

#printbackwards("story")



# 3. Write a recursive function that accepts a number and prints that number of stars, followed by ever decreasing stars on each line, E.g:
# ```
# *****
# ****
# ***
# **
# *
# ```
 

# 4. Create a padlock function. You need to be able to pass in a passcode and if its correct it should return "Unlock", else "Locked".

  


# 5. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
#   For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.


 
# 6. Write a function called is_prime() that accepts a number and return True or False if the number of prime or not.




# 7. Write a function that checks to see if a string is a pallindrome, if it is, it will return True and False if it is not.


# 8. Write a function that checks to see if a sentence is a pallindrome, if it is, it will return True and False if it is not. 
#   Tip - you may want to format your sentence so it is all lower case, and .replace() to get rid of white spaces.

def palindrome_sen(string):
  string2 = string.lower()
  if string2[::-1].replace(" ", "") == string2.replace(" ", ""):
    return True
  else: return False
 
print(palindrome_sen("Nun nun nun"))
print(palindrome_sen("Run nun run"))