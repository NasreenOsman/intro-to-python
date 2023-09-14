
# 3. 'secret.txt' contains a secret message. Each number represents the letter of the alphabet where 1 = A, 2 = B ... Z = 26. 
#    Work out what the secret message says.
dictionary ={
  1:"A",
  2:"B",
  3:"C",
  4:"D",
  5:"E",
  6:"F",
  7:"G",
  8:"H",
  9:"I", 
  10:"J",
  11:"K",
  12:"L",
  13:"M", 
  14:"N",
  15:"O", 
  16:"P", 
  17:"Q", 
  18:"R", 
  19:"S", 
  20:"T", 
  21:"U", 
  22:"V", 
  23:"W", 
  24:"X", 
  25:"Y", 
  26:"Z"
}
secret = ""
for x in open("text_files/secret.txt", "r"):
    x = int(x)
    secret = secret + dictionary[x]
print(secret)

# 4. Benford’s law states that the leading digits in a collection of data are probably going to be small. 
#   For example, most numbers in a set (about 30%) will have a leading digit of 1, when the expected probability is 11.1% (i.e. one out of nine digits). 
#   Fake data is usually evenly distributed, where as real data The files 'accounts_1.txt', 'accounts_2.txt' and 'accounts_3.txt' contain financial transaction data. 
#   Work out which of the files contains fake data.
