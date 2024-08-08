logo = """  _   _                 _                                           _                                          
 | \ | |               | |                                         (_)                                         
 |  \| |_   _ _ __ ___ | |__   ___ _ __    __ _ _   _  ___  ___ ___ _ _ __   __ _    __ _  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|  / _` | | | |/ _ \/ __/ __| | '_ \ / _` |  / _` |/ _` | '_ ` _ \ / _ \
 | |\  | |_| | | | | | | |_) |  __/ |    | (_| | |_| |  __/\__ \__ \ | | | | (_| | | (_| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \__, |\__,_|\___||___/___/_|_| |_|\__, |  \__, |\__,_|_| |_| |_|\___|
                                           __/ |                             __/ |   __/ |                     
                                          |___/                             |___/   |___/                      """

import random

levels = {
    "easy":15,
    "normal":10,
    "hard":5
}

number_picked = random.randint(0, 25)

def number_of_attempts(level):
    return levels[level]
  
start_game = input("Do you want to play new game? y or n\n")

while start_game == "y":
    print(logo)
    choose_level = input("Choose level, easy, normal or hard\n")   
    attempts = number_of_attempts(choose_level)
    print(attempts)

    while attempts != 0:
        guessing_input = int(input("What is your guessed number? Pick between 0 and 25\n==> "))     
        attempts -= 1

        if guessing_input != number_picked:
            
            if guessing_input>number_picked:
                print(f"You are high. Left attempts {attempts}")
            else:
                print(f"You are low. Left attempts {attempts}")
        else:
            print("You win")

    start_game = input("Do you want to play new game? y or n")   