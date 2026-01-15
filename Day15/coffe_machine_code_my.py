MENU  = {
    "espresso" : {
        "ingredients":{
        "water": 50,
        "coffee": 18,
        },
        "cost":1.5,
    },
    "latte" : {
        "ingredients":{
        "water": 200,
        "milk": 150,
        "coffee": 24,
        },
        "cost":2.5,
    },
     "cappuccino" : {
        "ingredients":{
        "water": 250,
        "milk": 100,
        "coffee": 24,
        },
        "cost":3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee":100,
    "money":0
}


total_amount = 0

def process_coins(qarters,dimes,nickles,pennies):
    """Count inserted coins"""
    amount = (qarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    global total_amount 
    total_amount += amount    

def sufficient_money_check(coffe_name):
    if MENU[coffe_name]["cost"] > total_amount:
        print("Sorry that's not enough money. Money refunded")
        return False
    else:
         change = round(total_amount - MENU[coffe_name]["cost"],2)
         if change > 0:
              print(f"Take you change: {change}")
         resources["money"] += MENU[coffe_name]["cost"]
         return True
    
def check_resource(drink):
     for key in MENU[drink]["ingredients"]:
          if MENU[drink]["ingredients"][key] > resources[key]:
           print(f"Sorry there is not enough {key}")
           return False
     return True

def final_coffee(drink_ingredients):
     for key in MENU[drink_ingredients]["ingredients"]:
         resources[key] -= MENU[drink_ingredients]["ingredients"][key] 
     print(f"Here is your {drink_ingredients} ☕. Enjoy!")
     
           
is_continue = True

while is_continue:

    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "off":
         is_continue = False

    elif user_input == "report":
        for key in resources:
            print(f"{key}: {resources[key]}")
        

    elif user_input in MENU:
                total_amount = 0
            
                if check_resource(user_input):
           
                    print("Please insert coins.")
                    quarters = int(input("How many quarters? "))
                    dimes = int(input("How many dimes? "))
                    nickles = int(input("How many nickles? "))
                    pennies = int(input("How many pennies? "))

                    process_coins(quarters,dimes,nickles,pennies)

                    if sufficient_money_check(user_input):

                      final_coffee(user_input)

    else:
         print("SOmething went wrong!")