
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letter = random.randint(1,11)
nr_symbol = random.randint(1,6)
nr_number = random.randint(1,6)

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