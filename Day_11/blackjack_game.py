
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def add_cards(symbol, user, number_of_cards):
  game[user]["cards"].extend(random.sample(cards, number_of_cards))
  game[user]["score"] = sum(game[user]["cards"])
  print(f'{symbol}{user.title()} cards are: {game[user]["cards"]}, {user.lower()} score is: {game[user]["score"]}')
  
def user_score(user):
  return game[user]["score"]

start_game = input("♠️♥️♦️♣️ Do you want to play? (y/n)\n").lower()

while start_game == "y":
  game = {
    "player":{
      "cards":[],
      "score":0,
    },
    "computer":{
      "cards":[],
      "score":0,
    }
  }
  add_cards("🧑 ","player", 2)
  add_cards("💻 ","computer", 1)
    
  if user_score("player")<=21:
    draw_another = input("🃏 Draw another one? (y/n)\n").lower()
    
    while draw_another=="y":
      add_cards("🧑 ","player", 1)
      
      if game["player"]["score"]<=21:
        draw_another = input("🃏 Draw another one? (y/n)\n").lower()
      else:
        add_cards("💻 ","computer", 1)
        print(f'\nYOU LOSE!😞\n 💻 Computers cards are {game["computer"]["cards"]} and comp score is {user_score("computer")}.\n 🧑 Your score is {user_score("player")}.\n')
        start_game = input("Do you want to play (y or n)\n").lower()
        break

    while user_score("computer")<17:
      add_cards("💻 ","computer", 1)

      
    if user_score("computer") <= 21:
      if user_score("computer")>user_score("player"):
        print(f'\nYOU LOSE!😞\n 💻 Computers cards are {game["computer"]["cards"]} and comp score is {user_score("computer")}.\n 🧑 Your score is {user_score("player")}.\n')
      elif user_score("computer")==user_score("player"):
        print(f'IT IS A TIDE. \n 💻 Computers cards are {game["computer"]["cards"]} and comp score is {user_score("computer")}.\n 🧑 Your score is {user_score("player")}.\n')
      else:
        print(f'\n🏆YOU WIN!!!🏆\n 💻 Computers cards are {game["computer"]["cards"]} and comp score is {user_score("computer")}.\n 🧑 Your score is {user_score("player")}.\n')
    else:
      print(f'\n🏆YOU WIN!!!🏆\n 💻 Computers cards are {game["computer"]["cards"]} and comp score is {user_score("computer")}.\n 🧑 Your score is {user_score("player")}.\n')

  start_game = input("♠️♥️♦️♣️ Do you want to play? (y/n)\n").lower()
      