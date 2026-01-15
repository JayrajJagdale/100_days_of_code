import random
import art
from data import info

def random_value():
 random_line = random.choice(info)
 return random_line

A = random_value()
B = random_value()

if A == B:
        B = random_value()

current_score = 0
is_game_over = False

while not is_game_over:

    print(art.logo1)
    print(f"Compare A: {A["name"]}, a {A["description"]}, from {A["country"]}" )
    print(art.logo2)
    print(f"Against B: {B["name"]}, a {B["description"]}, from {B["country"]}" )

    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_input == 'a':
        if A['follower_count'] > B['follower_count']:
            current_score += 1
            print(f"You're right! Current score: {current_score}")
            B = random_value()
            
        else:
            is_game_over = True
            print(f"Sorry, that's wrong. Final score: {current_score}")
          
    elif user_input == 'b':  
        if B['follower_count'] > A['follower_count']:
            current_score += 1
            print(f"You're right! Current score: {current_score}")
            A = random_value()

        else:
            is_game_over = True
            print(f"Sorry, that's wrong. Final score: {current_score}")
  
    else:
        print("Wrong Input !")