import draw

def recommend_move(player1,player2,playercards,dealer1):
  '''
  Evaluates face up dealer card and player card sum to print and return the best move to make
  '''
  #get integer value of cards for comparisons
  dealer1 = draw.card_value(dealer1)
  total = sum(playercards)
  suggest = ""

  #split only available if both cards are the same and player has not hit
  if player1[0][0] == player2[0][0] and len(playercards) == 2:
    if playercards[0] == 11 or playercards[0] == 8:
      suggest = "Split"
    elif playercards[0] == 9 and dealer1 != 7:
      suggest = "Split"
    elif playercards[0] == 7 and dealer1 <= 7:
      suggest = "Split"
    elif playercards[0] == 6 and dealer1 <= 6:
      suggest = "Split"
    elif playercards[0] == 4 and dealer1 in [5,6]:
      suggest = "Split"
    elif playercards[0] == 3 and dealer1 <= 7:
      suggest = "Split"
    elif playercards[0] == 2 and dealer1 <= 7:
      suggest = "Split"
  
  #if split not recommended
  if suggest == "":
    #different suggestion if player has soft hand (ace == 11)
    if 11 in playercards:
      if total in [13,14,15,16]:
        if dealer1 in [4,5,6]:
          suggest = "Double Down or Hit"
        else:
          suggest = "Hit"
      elif total == 17:
        if dealer1 in [2,3,4,5,6]:
          suggest = "Double Down or Hit"
        else:
          suggest = "Hit"
      elif total == 18:
        if dealer1 in [3,4,5,6]:
          suggest = "Double Down or Stand"
        elif dealer1 in [9,10]:
          suggest = "Hit"
      elif total == 19 and dealer1 == 6:
        suggest = "Double Down or Stand"
 
    else:
      #hard hands (no ace == 11)
      if total in [5,6,7]:
        suggest = "Hit"
      elif total == 8:
        if dealer1 in [5,6]:
          suggest = "Double Down"
        else:
          suggest = "Hit"
      elif total == 9:
        if dealer1 <= 6:
          suggest = "Double Down"
        else:
          suggest = "Hit"
      elif total == 10:
        if dealer1 in [10,11]:
          suggest = "Hit"
        else:
          suggest = "Double Down"
      elif total == 11:
        suggest = "Double Down"
      elif total == 12:
        if dealer1 not in [4,5,6]:
          suggest = "Hit"
      elif total in [13,14,15,16]:
        if dealer1 >= 7:
          suggest = "Hit"

  #dd not available when player has already hit
  if suggest == "Double Down" or suggest == "Double Down or Hit":
    if len(playercards) > 2:
      suggest = "Hit"
    else:
      suggest = "Double Down"
  
  elif suggest == "Double Down or Stand":
    if len(playercards) > 2:
      suggest = "Stand"
    else:
      suggest = "Double Down"
  
  if suggest == "":
    suggest = "Stand"
  
  print("Recommendation:",suggest)
  print("")
  return auto_choice(suggest)

def auto_choice(suggestion):
  '''
  Converts suggested best move (suggestion) to one letter so it can be automatically used by if statements. 
  '''
  choice = "h"
  
  #allows for suggestion to be automatically inputted
  if suggestion == "Double Down":
    choice = "dd"
  elif suggestion == "Split":
    choice = "sp"
  elif suggestion == "Stand":
    choice = "s"
  return choice
    