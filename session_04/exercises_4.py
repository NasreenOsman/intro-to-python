# Session 4 Exercises

## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.
list = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
print(list)


# 2. Add "Grapes" to the list and print the list.
list.append("Grapes")
print(list)


# 3. Change "Pears" to "Strawberries" and print the list.
list[2]="Strawberries"
print(list)


# 4. Remove "Apples" from the list and print the list.
del(list[0])
print(list)

# 5. Print out the current length of the list.
print(len(list))



# 6. Order the list alphabetically.
list.sort()
print(list)


# 7. Print out the list again.
print(list)



# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.
for item in list:
  print(item)


# 2. Print the numbers 1 to 100 (including the number 100).
for my_number in range(1, 101):
  print(my_number)


# 3. Print all odd numbers from 1 to 100.
for my_number in range(1, 100, 2):
  print(my_number)


# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).
year_not_held=[1916, 1940, 1944, 2020]
for olympic_year in range(1896, 2023, 4): 
  if olympic_year not in year_not_held:
    print(olympic_year)


# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.
list2=[5, 4, 6, 8, 93, 43, 54, 77, 92, 100]
even_count=0
odd_count=0 
for number in list2:
  if number%2==0: 
    even_count= even_count +1
  else: odd_count += 1

print("This list has " + str(even_count) + " even numbers and " + str(odd_count) + " odd numbers") 



# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.
list3=["Muhammad_Ali", "Michael_Schumi", "Lionel", "Tommy_Lee", "Neve_Campbell"]
for person in list3:
  print("Hello " + person)


# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".
word = "supercalifragilisticexpialidocious"
for each_letter in word:
  print(each_letter)
  


# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.
list4=[2,4,6,8,10]
list5=[]
for each_number in list4: 
  list5.append(each_number**2)
  print(list5)


# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.

list6=["Nasreen", "Tahir", "Nazrana", "Anisa", "Nishad"]
list7=[]
for each_name in list6:
  list7.append("Dr " + each_name)
  print(list7)

# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". 
#    For numbers which are multiples of both three and five, print "FizzBuzz".

#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```
for each_number in range(0, 101): 
  if each_number%3 ==0 and each_number%4==0:
    print("FizzBuzz")
  elif each_number%3==0:
    print("Fizz")
  elif each_number%5==0:
    print("Buzz")
  else: 
    print(each_number)