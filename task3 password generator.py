import random
import string

print("Simple Password Generator")
length = int(input("Enter password length:"))
characters = string.ascii_letters + string.digits

password = ""
for i in range(length):
    password += random.choice(characters)
print("Your Password is:", password)
