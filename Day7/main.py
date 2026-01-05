import random
import hangman_words
import hangman_art


print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
world_length = len(chosen_word)
for postion in range(world_length):
    placeholder +=  "_"
print("Word to guess: "+ placeholder)

# Another Logic
# for char in chosen_word:
#     char = placeholder
#     print(char,end="")

# user_guess = input("\nGuess a letter: ").lower()

# Another Logic
# for letter in chosen_word:
#     if letter == user_guess:
#        print(letter,end="")
#     else:
#         print(char,end="")
game_over = False
correct_letters = []
lives = 6

while not game_over:

    print(f"***************{lives}/6 LIVES LEFT***************")

    user_guess = input("\nGuess a letter: ").lower()

    if user_guess in  correct_letters:
            print(f"You've already guessed {user_guess}")
         
         
    display = ""

    for letter in chosen_word:
            if letter == user_guess:
                display += letter
                correct_letters.append(user_guess)

            elif letter in correct_letters:
                 display += letter

            else:
                display += "_"

    print("Word to guess:" + display)


    if user_guess not in chosen_word:
         lives -= 1
         print(f"You guessed {user_guess}, that's not in the word. You lose a life")
         if lives == 0:
              game_over = True
              print(f"**************** IT WAS {chosen_word}! YOU LOSE****************")

    if "_" not in display:
         game_over = True
         print("****************YOU WIN****************")
    
    print(hangman_art.stages[lives])
