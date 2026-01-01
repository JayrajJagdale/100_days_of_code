import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letter = int(input("How many letters would you like in your password?\n"))
nr_symbol = int(input("How many symbols would you like?\n"))
nr_number = int(input("How many numbers would you like?\n"))

# Easy level
# password = ""

# for char in range(0,nr_letter):
#     password += random.choice(letters)

# for char in range(0,nr_symbol):
#     password += random.choice(symbols)

# for char in range(0,nr_number):
#     password += random.choice(numbers)

# print(password)

# Hard Level
password = []

for char in range(0,nr_letter):
    password.append(random.choice(letters))

for char in range(0,nr_symbol):
    password.append(random.choice(symbols))

for char in range(0,nr_number):
    password.append(random.choice(numbers))

print(password)

random.shuffle(password)

print(password)

print(f"Your Password: {"".join(password)}")


final_password = ""
for char in password:
    final_password += char

print(final_password)