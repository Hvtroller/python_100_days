# this is BlackJack game project

import random

print("""
+-+-+-+-+-+-+-+-+-+
|B|l|a|c|k|J|a|c|K|
+-+-+-+-+-+-+-+-+-+ 
 
""")

cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def get_card_value(card):
  if card in ["J", "Q", "K"]:
    return 10
  if card == "A":
    return 11
  return int(card)

def get_hand_value(hand):
  total = 0
  for card in hand:
    total += get_card_value(card)
  return total

def is_bust(hand):
  return get_hand_value(hand) > 21

def is_blackjack(hand):
  return get_hand_value(hand) == 21

def is_win(player_hand, dealer_hand):
  if is_bust(player_hand):
    return False
  if is_bust(dealer_hand):
    return True

  return get_hand_value(player_hand) > get_hand_value(dealer_hand)

def is_tie(player_hand, dealer_hand):
  return get_hand_value(player_hand) == get_hand_value(dealer_hand)

def is_valid_input(hand, card):
  return card in cards and card not in hand

def is_valid_action(action):
  return action in ["hit", "stand"]

def get_winner(player_hand, dealer_hand):
  if is_win(player_hand, dealer_hand):
    return f"Player wins! {'Blackjack!' if is_blackjack(player_hand) else ''}"
  if is_win(dealer_hand, player_hand):
    return f"Dealer wins! {'Blackjack!' if is_blackjack(dealer_hand) else ''}"
  return "It's a tie!"

def get_hand_string(hand):
  return ", ".join(hand)

def deal_card(hand):
  hand.append(random.choice(cards))

player_hand = []
dealer_hand = []

for _ in range(2):
  deal_card(player_hand)
  deal_card(dealer_hand)

print("Player hand:", get_hand_string(player_hand))
print("Dealer hand:", dealer_hand[0], ", ?")

while True:
  action = input("Do you want to hit or stand? ")
  if not is_valid_action(action):
    print("Invalid action")
    continue

  if action == "hit":
    deal_card(player_hand)
    print("Player hand:", get_hand_string(player_hand))
    if is_bust(player_hand):
      print("Player busts! Dealer wins.")
      break
  else:
    break

if not is_bust(player_hand):
  print("Dealer hand:", get_hand_string(dealer_hand))
  while get_hand_value(dealer_hand) < 17:
    deal_card(dealer_hand)
    print("Dealer hand:", get_hand_string(dealer_hand))
    if is_bust(dealer_hand):
      print("Dealer busts! Player wins.")
      break

if not is_bust(player_hand) and not is_bust(dealer_hand):
  print(get_winner(player_hand, dealer_hand))







