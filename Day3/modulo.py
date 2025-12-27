# Simple if-else
# num = int(input("Enter a number: "))
# if(num % 2 == 0):
#     print(f"{num} is even!")
# else:
#     print(f"{num} is odd!")

# Nested if else 
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age! "))
#     if age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry you have to grow taller before you can ride.")

# if elif else
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age! "))
#     if age <= 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry you have to grow taller before you can ride.")

# Multiple if
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age! "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo == 'y':
        # Add $3 to their bill
        bill += 3
    print(f"Your final bill is ${bill}")  

else:
    print("Sorry you have to grow taller before you can ride.") 