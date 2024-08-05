import art
from os import system

print(art.logo)

bidders_list = {}
new_bidder = True

while new_bidder:
  bidder_name = input("What is your name?\n")
  bid_price = int(input("What is your bidding price?\n"))

  bidders_list[bidder_name] = bid_price
  
  new_bidder = input("Is there another bidder?\n Yes or No\n")
  if new_bidder == "Yes".lower():
    new_bidder = True
    system('cls')
  else:
    new_bidder = False

highest_bidder = ""
highest_bid = 0

for bidder in bidders_list:
  if highest_bid<bidders_list[bidder]:
    highest_bid = bidders_list[bidder]
    highest_bidder = bidder
    
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")