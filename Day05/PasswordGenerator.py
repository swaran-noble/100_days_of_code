import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letters_n = int(input("How many letters would you like in your password?\n"))
symbols_n = int(input(f"How many symbols would you like?\n"))
numbers_n = int(input(f"How many numbers would you like?\n"))

password=""
for i in range(0,letters_n):
    password+=random.choice(letters)
for i in range(0,symbols_n):
    password+=random.choice(symbols)
for i in range(0,numbers_n):
    password+=random.choice(numbers)

print(f"Easy version: {password}")

#Hard version
#Hard version is to shuffle the string
hard_password = ''.join(random.sample(password,len(password)))
print(f"Hard version: {hard_password}")  
