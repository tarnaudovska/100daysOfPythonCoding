logo = """
  _   _                 _                  _____                     
 | \ | |               | |                / ____|                    
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __|
 | |\  | |_| | | | | | | | | |  __/ |    | |__| | |_| |  __/\__ \__ \\
 |_| \_|\__,_|_| |_| |_|_| |_|\___|_|     \_____|\__,_|\___||___/___/
                                                                      
"""

import random

levels = {
    "easy":15,
    "normal":10,
    "hard":5
}

def number_of_attempts(level):
    return levels[level]
  
start_game = input("Do you want to play new game? y or n\n").lower()
number_picked = random.randint(0, 25)

while start_game == "y":
    print(logo)
    choose_level = input("Choose level, easy, normal or hard\n").lower() 
    attempts = number_of_attempts(choose_level)
    print(f"You have {attempts} attempts to guess the number")

    won = False
    
    while attempts != 0:
        guessing_input = int(input("What is your guessed number? Pick between 0 and 25\n==> "))     
        attempts -= 1

        if guessing_input>number_picked:
            print(f"You are high. Left attempts {attempts}")
        elif guessing_input<number_picked:
            print(f"You are low. Left attempts {attempts}")
        else:
            won = True
            print("YOU WIN!!!")
            break

    if not won:
        print(f"You used all your attempts. The number was {number_picked}.\nGAME OVER")

    start_game = input("Do you want to play new game? y or n\n").lower()