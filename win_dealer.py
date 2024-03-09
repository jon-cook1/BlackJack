import draw
import time

def dealer_logic(dealer1,dealer2,dealercards,drawncards,default):
  '''
  Draws cards for the dealer until the sum is greater than 16 and returns the sum of the dealer's cards
  '''
  total = sum(draw.card_sum(dealercards))
  print("Dealer Card #1:", dealer1)
  if default:
    time.sleep(1)
  print("Dealer Card #2:", dealer2)
  
  while total < 17:
    if default:
      time.sleep(1)
    #draw card, add value to value list, add to total cards drawn, print card, evaluate dealer cards' sum
    newdealer = draw.card(drawncards)
    dealercards = draw.value_list(dealercards,newdealer)
    drawncards.append(newdealer)
    print(f"Dealer Card #{len(dealercards)}: {newdealer}")
    total = sum(draw.card_sum(dealercards))
  if default:
    time.sleep(2)
  return total
  
  
def eval_win(playertotal,dealertotal,bet,bank):
  '''
  Takes in player total and dealer total to evaluate winner and print proper message. Takes in bet and bank to determine how much money the player has after w/l/d and returns the adjusted bank value. 
  '''
  #If player has over 21, auto loss as dealer cards have not been shown
  if playertotal > 21:
    print(f"You busted ({playertotal}), you lose!")
    bet = bet * -1
  else:
    if dealertotal > 21:
      print(f"The dealer busted ({dealertotal}), you win!")
    elif playertotal > dealertotal:
      print(f"You have {playertotal} and the dealer has {dealertotal}, you win!")
    elif dealertotal > playertotal:
      print(f"You have {playertotal} and the dealer has {dealertotal}, you lose!")
      bet = bet * -1
    else:
      print(f"Both you and the dealer have {playertotal}, you pushed!")
      bet = 0

  return bank + bet

    