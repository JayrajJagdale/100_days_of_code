# def greet():
#     print("Hii")
#     print("Hello")
#     print("Bye")

# greet()

# Functions that allows for inputs

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}? ")

# greet_with_name("Jayraj")

# Function with more than one input

def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_with("Jayraj","Kolhapur")
greet_with("Kolhapur","Jayraj") # Positional Argument
greet_with(location="Kolhapur",name="Jayraj") # Keyword Argument
