import win_dealer
import draw
import time

def bank_input():
  '''
  Prompts user to enter bank value until a positive integer is entered, then returns that value
  '''
  bank = 0
  print("How much money are you playing with?")
  while bank <= 0:
    bank = input("$")
    try:
      bank = int(bank)
    #checks that input is not 0
      bank == 1 / bank
      if bank < 0:
        print("\nPlease enter a positive number")
    #exceptions allow different error messages depending on what is entered
    except ValueError:
      print("\nPlease enter a whole number")
      bank = 0
    except ZeroDivisionError:
      print("\nPlease enter a number greater than zero")
  return bank


def bet(bank,handnum,default):
  '''
  Prints hand number/ bank (parameters) and prompts user to enter a bet if automatic mode is off. Checks to make sure the bet is a positive integer then returns that value
  '''
  print("_"*56)
  print(" "*56)
  print(f"Hand #{handnum}\n")
  print("You have $" + str(bank))
  bet = 10
  notfirst = False
  
  if default:
    bet = 0
    print("Enter bet:")
    while bet < 1 or bet > bank:
      #allows no error message on first loop only
      if notfirst:
        print("\nInvalid Bet")
      bet = input("$")
      try:
        bet = int(bet)
      except ValueError:
        bet = 0
      notfirst = True
  else:
    #time.sleep(0.5)
    #uncomment for slower automatic mode
    if bank < 10:
      bet = bank
    print()
  return bet

def new_hand(player1,player2, dealer1):
  print("-"*29)
  print("Dealer Card #1:",dealer1)
  print("Dealer Card #2: ?\n")
  print("Player Cards:")
  print(player1)
  print(player2)
  print("-"*29)

def choice(player1, player2, bet, bank):
  '''
  Takes in player cards, bet, and bank to determine what actions the user is able to do. Returns the action that is chosen
  '''
  notfirst = False
  choice = ""
  
#if player can't afford to double bet, split and double down not available
  if bank < bet * 2:
    while choice not in ["h","s"]:
      if notfirst:
        print('Invalid input') 
      choice = input("Would you like to HIT or STAND? [h/s]\n> ")
      notfirst = True
  #double down available
  else:
      #if both cards are the same, split available
      if player1[0] == player2[0]:
        while choice not in ["h","s","dd","sp"]:
          if notfirst:
            print('Invalid input') 
          choice = input("Would you like to HIT, STAND, DOUBLE DOWN, or SPLIT? [h/s/dd/sp]\n> ")
          notfirst = True
      else:
        while choice not in ["h","s","dd"]:
          if notfirst:
            print('Invalid input') 
          choice = input("Would you like to HIT, STAND, or DOUBLE DOWN? [h/s/dd]\n> ")
          notfirst = True
  return choice

def first_blackjack(playercards, dealercards, bet, bank):
  '''
  Takes in player cards and dealer cards to evaluate if either have blackjack. Takes in bet and bank to return bank value if one or both have blackjack. Returns a string if neither have it
  '''
  print("")
  if sum(playercards) == 21 and sum(dealercards) == 21:
    print("Both you and the dealer have BLACKJACK, you pushed")
    return bank
  elif sum(playercards) == 21:
    print("***BLACKJACK***")
    return int(bank + bet * 1.5)
  elif sum(dealercards) == 21:
    print("The dealer has BLACKJACK, you lose")
    return bank - bet
  else:
    return "continue"


def stay(dealer1, dealer2, dealercards, drawncards, default):
  '''
  Takes in both dealer cards, list of dealer card values, and list of all cards drawn to calculate dealer's final total

  Returns sum of dealer's cards
  '''
  #draw cards until dealer busts or has to stay
  dealertotal = win_dealer.dealer_logic(dealer1,dealer2,dealercards,drawncards,default)
  print("-"*29)
  return dealertotal

def hit(drawncards,playercards):
  '''
  Draws new unique card and returns list of player card values with new card added
  '''
  newplayer = draw.card(drawncards)
  drawncards.append(newplayer)
  #add new card numeric value to list of player cards
  playercards = draw.value_list(playercards,newplayer)
  print(f"Player card #{len(playercards)}:",newplayer)
  return playercards

def mode_input():
  '''
  Prompts user for mode, checks for valid input, then returns
  '''
  mode = 1
  notfirst = False
  while mode not in ["d","t","a"]:
    #error message after first loop
    if notfirst:
      print("Invalid Input")
    mode = input("Would you like Default, Training, or Automatic mode? [d/t/a]\n> ")
    notfirst = True
  print("")
  
  return mode



