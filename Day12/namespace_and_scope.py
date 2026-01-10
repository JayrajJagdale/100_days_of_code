enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside funcion: {enemies}")

# Local Scope

# def drink_potion():
#     position_strength = 2
#     print(position_strength)

# drink_potion()
# print(poition_strength) # It can't be called becasue it is local variable

# Global Scope

player_health = 10

def drink_potion():
    position_strength = 2
    print(player_health)

drink_potion()
print(player_health)
