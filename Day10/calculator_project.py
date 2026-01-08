import art
def add(n1,n2):
    return n1 + n2

# my_favourite_operation = add
# print(my_favourite_operation(2,3))

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator():
    print(art.logo)
    
    still_calculate = True

    n1 = float(input("What's the first number?: "))

    while True: 
        for symbol in operations:
            print(symbol)
        choice = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))

        answer = operations[choice](n1,n2)
        print(f"{n1} {choice} {n2} = {answer}")

    
        should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if should_continue == 'y':
            n1 = answer
        
        elif should_continue == 'n':
            still_calculate = False
            print("\n" * 20)
            calculator()

calculator()
        

