import random
rock = '''
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
choice_list = [rock,paper,scissors]
random_index = random.randint(0,2)
computer_choice = random_index

if  your_choice < 0 or your_choice > 1:
    print("Invalid Input")

else:
    print(your_choice)
    print(choice_list[your_choice])

    print(computer_choice)
    print(choice_list[computer_choice])

    if your_choice == computer_choice:
        print("Its a Tie!")

    elif your_choice == 0 and computer_choice == 2:   
        print('You Win')

    elif your_choice == 1 and computer_choice == 0:
        print("You Win!")

    elif your_choice == 2 and computer_choice == 1:
        print("You Win!")

    else:
        print("You Lose!")


