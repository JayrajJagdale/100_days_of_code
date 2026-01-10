# Modify the global scope

# enemies = 1

# def increase_enemies():
#     global enemies
#     enemies += 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


# Another Way

enemies = 1

def increase_enemies(enemies):
    print(f"enemies inside function: {enemies}")
    return enemies + 1
    

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")