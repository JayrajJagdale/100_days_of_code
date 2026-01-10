import random
import art

random_number = random.randint(1,100)
print(random_number)
 
def guess_check(num):
    if num > random_number:
        print("Too high.")
        print("Guess again.")
    elif num < random_number:
         print("Too low.")
         print("Guess again.")
    
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

is_game_over = False

if level == 'easy':
    easy_level = 10
    print(f"You have {easy_level} attempts remaining to guess the number.")
    while not is_game_over:
        guess = int(input("Make a guess: "))
        guess_check(guess)
        if guess == random_number:
            print(f"You got it! The answer was {random_number}")
            is_game_over = True
        else:
            easy_level -= 1
            if easy_level == 0:
                print(f"You Lose! The answer was {random_number}")
                is_game_over = True
            else:
                print(f"You have {easy_level} attempts remaining to guess the number.")

elif level == "hard":
    hard_level = 5
    print(f"You have {hard_level} attempts remaining to guess the number.")
    while not is_game_over:
        guess = int(input("Make a guess: "))
        guess_check(guess)
        if guess == random_number:
            print(f"You got it! The answer was {random_number}")
            is_game_over = True
        else:
            hard_level -= 1
            if hard_level == 0:
                print(f"You Lose! The answer was {random_number}")
                is_game_over = True
            else:
                print(f"You have {hard_level} attempts remaining to guess the number.")
else:
    print("Incorrect Choice..! Try Again")