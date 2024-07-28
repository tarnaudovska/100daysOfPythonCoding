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
---'   ____)____
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


player_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if player_choise == 0:
    print(rock)
elif player_choise == 1:
    print(paper)
else:
    print(scissors)

import random

computer_choise = random.randint(0, 2)
if computer_choise == 0:
    print(rock)
elif computer_choise == 1:
    print(paper)
else:
    print(scissors)

if player_choise == 0 and computer_choise == 2:
    print("You win!")
elif player_choise == 1 and computer_choise == 0:
    print("You win!")
elif player_choise == 2 and computer_choise == 1:
    print("You win!")
elif player_choise == computer_choise:
    print("It's a draw!")
else:
    print("You lose!")