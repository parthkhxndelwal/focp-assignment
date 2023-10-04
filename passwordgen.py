# Password Generator
from random import *

non_caps = "abcdefghijklmnopqrstuvwxyz" # Non Uppercase Characters
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Uppercase Characters 
symbols = "!@#$%^&*()" # Symbols
numbers = "0123456789" # Numbers

char_non_caps = 4 # Non Uppercase Characters in the password 
char_caps = 2 # Uppercase Characters in the password
char_symbols = 3 # Symbols in the password
char_numbers = 3 # Numbers in the password

password = []

for i in range(char_non_caps):
    password.append(choice(non_caps))
for i in range(char_caps):
    password.append(choice(caps))
for i in range(char_symbols):
    password.append(choice(symbols))
for i in range(char_numbers):
    password.append(choice(numbers))
shuffle(password)

password = "".join(password)

print(f"Your password is: {password}")
