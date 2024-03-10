import draw
import helpers
import win_dealer
import time
import suggest

def logic(player1,player2,dealer1,dealer2,playercards,dealercards,bet,bank,handnum,drawncards,train,default):
  '''
  Takes all variables used in a blackjack hand to allow user to split. Splits base hand once then returns final bank after each split is played out
  '''
  p1 = [playercards[0]]
  p2 = [playercards[1]]
  
  #turned to true if player splits again
  splitagain1 = False
  splitagain2 = False
#------------------------------------------------------------
#hand sp-1
  #plays out same as a regular hand (in BlackJack file), but uses one of starter two cards and draws a new one
  bet2 = bet
  print(f"\nHand #{handnum}-1")
  print("Player Cards:")
  print(player1)
  newplayer = draw.card(drawncards)
  drawncards.append(newplayer)
  p1 = draw.value_list(p1,newplayer)
  print(newplayer)

  if sum(p1) == 21 or p1[0] == 11:
    choice = "s"
  else:
    if train:
      print("")
      choice = suggest.recommend_move(player1,newplayer,p1,dealer1)
    if default:
      choice = helpers.choice(player1,newplayer,bet,bank)

  if choice == "s":
    print("")

    total = sum(p1)
    print("You have",total)
  
  elif choice == "dd":
    bet = bet * 2 
    print("")
    if default:
      time.sleep(1)
    total = sum(draw.card_sum(helpers.hit(drawncards,p1)))
    print("")
    if total <= 21: 
      if default:
        time.sleep(1.5)
      print("You have",total)
    else:
      print(f"You busted ({total}), you lose!")


  elif choice == "h":
    total = sum(p1)
    notfirsth = False
    
    while total < 21:
      if default:
        time.sleep(1)
      if notfirsth:
        if train:
          print("")
          choice = suggest.recommend_move(player1,newplayer,p1,dealer1)
        if default:
          choice = input("Would you like to HIT or STAND? [h/s]\n> ")
          while choice not in ["h","s"]:
            print("Invalid choice. Please enter 'h' or 's'")
            choice = input("> ")
        if choice == "s":
          break
      print("")
      p1 = helpers.hit(drawncards,p1)
      print("")
      notfirsth = True
      total = sum(draw.card_sum(p1))
    print("")
    if total <= 21: 
      if default:
        time.sleep(1.5)
      print("You have",total)
    else:
      print(f"You busted ({total}), you lose!")
  else:
    splitnum = 1
    splitagain1 = True
    splitnum2 = 1
  
    #if user double splits, first hand of double split is played out
    split2first = secondsplit(player1,newplayer,p1,bet,bank,handnum,drawncards,splitnum,splitnum2,dealer1,train,default)
  
    #secondsplit returns list with player sum and drawncards, so those are isolated to allow for win calculations and no duplicate cards
    drawncards = split2first[1]
    sp2total1 = split2first[0]

    splitnum2 = 2
    split2second = secondsplit(player1,newplayer,p1,bet,bank,handnum,drawncards,splitnum,splitnum2,dealer1,train,default)

    drawncards = split2second[1]
    sp2total2 = split2second[0]

        
#------------------------------------------------------------
#hand sp-2
  #uses the second starter card and plays like regular hand
  print("-" * 10)
  print(f"\nHand #{handnum}-2")
  print("Player Cards:")
  print(player2)
  newplayer2 = draw.card(drawncards)
  drawncards.append(newplayer2)
  p2 = draw.value_list(p2,newplayer2)
  print(newplayer2)

  if sum(p1) == 21 or playercards[1] == 11:
    choice = "s"
  else:
    if train:
      print("")
      choice = suggest.recommend_move(player2,newplayer2,p2,dealer1)
    if default:
      choice = helpers.choice(player1,newplayer,bet,bank)

  if choice == "s":
    print("")
    total2 = sum(p2)
    print("You have",total2)
  
  elif choice == "dd":
    bet = bet * 2 
    print("")
    if default:
      time.sleep(1)
    total2 = sum(draw.card_sum(helpers.hit(drawncards,p2)))
    print("")
    if total2 <= 21: 
      if default:
        time.sleep(1.5)
      print("You have",total2)
    else:
      print(f"You busted ({total2}), you lose!")
      

  elif choice == "h":
    total2 = sum(p2)
    notfirsth = False
    
    while total2 < 21:
      if default:
        time.sleep(1)
      if notfirsth:
        if train:
          print("")
          choice = suggest.recommend_move(player2,newplayer2,p2,dealer1)
        if default:
          choice = input("Would you like to HIT or STAND? [h/s]\n> ")
          while choice not in ["h","s"]:
            print("Invalid choice. Please enter 'h' or 's'")
            choice = input("> ")
        if choice == "s":
          break
      print("")
      p2 = helpers.hit(drawncards,p2)
      print("")
      notfirsth = True
      total2 = sum(draw.card_sum(p2))
    print("")
    if total2 <= 21: 
      if default:
        time.sleep(1.5)
      print("You have",total2)
    else:
      print(f"You busted ({total2}), you lose!")
  else:
    splitnum = 2
    splitagain2 = True
    splitnum2 = 1
  
    split2first = secondsplit(player2,newplayer,p2,bet,bank,handnum,drawncards,splitnum,splitnum2,dealer1,train,default)
  
    drawncards = split2first[1]
    sp2total11 = split2first[0]

    splitnum2 = 2
    split2second = secondsplit(player2,newplayer,p2,bet,bank,handnum,drawncards,splitnum,splitnum2,dealer1,train,default)

    drawncards = split2second[1]
    sp2total22 = split2second[0]

    
#------------------------------------------------------------
#win calc
  
  print("-" * 10)
  print("")
  dealertotal = win_dealer.dealer_logic(dealer1,dealer2,dealercards,drawncards,default)
  #if first split splits again
  if splitagain1:
    print(f"\nHand #{handnum}-{splitnum}-1:")
    bank = win_dealer.eval_win(sp2total1,dealertotal,bet,bank)

    print(f"\nHand #{handnum}-{splitnum}-2:")
    bank = win_dealer.eval_win(sp2total2,dealertotal,bet,bank) 

  else:
    print(f"\nHand #{handnum}-1:")
    bank = win_dealer.eval_win(total,dealertotal,bet,bank)
  
  #if second split splits again
  if splitagain2:
    print(f"\nHand #{handnum}-{splitnum}-1:")
    bank = win_dealer.eval_win(sp2total11,dealertotal,bet,bank)

    print(f"\nHand #{handnum}-{splitnum}-2:")
    bank = win_dealer.eval_win(sp2total22,dealertotal,bet,bank) 
  else:
    print(f"\nHand #{handnum}-2:")
    bank = win_dealer.eval_win(total2,dealertotal,bet2,bank)

  return bank


#------------------------------------------------------------
# 2 and 3 split potential

def secondsplit(player1,newplayer,p1,bet,bank,handnum,drawncards,splitnum,splitnum2,dealer1,train,default):
  '''
  Takes all parameters as initial split function and allows the user to split a split. Called upon twice when double splitting and returns the sum of player cards and list of drawn cards.
  '''
  #function is same as split function above, but takes in splitnum2 to correctly print which split it is. 

  #triple splitting is currently not supported, so no split option is available in this program, however it could be implemented in the same way this one is, but the time it would take is not worth the 1 in ~15,000 hands that it occurs in.

  p1 = [draw.card_value(player1)]

  print(f"\nHand #{handnum}-{splitnum}-{splitnum2}")
  print("Player Cards:")
  print(player1)
  newplayer = draw.card(drawncards)
  drawncards.append(newplayer)
  p1 = draw.value_list(p1,newplayer)
  print(newplayer)

  
  if sum(p1) == 21:
    choice = "s"
  else:
    if train:
      print("")
      choice = suggest.recommend_move(player1,newplayer,p1,dealer1)
    if default:
      choice = helpers.choice(player1,newplayer,bet,bank)

  if choice == "s":
    print("")

    total = sum(p1)
    print("You have",total)
  
  elif choice == "dd":
    bet = bet * 2 
    print("")
    if default:
      time.sleep(1)
    total = sum(draw.card_sum(helpers.hit(drawncards,p1)))
    print("")
    if total <= 21: 
      if default:
        time.sleep(1.5)
      print("You have",total)
    else:
      print(f"You busted ({total}), you lose!")


  elif choice == "h":
    total = sum(p1)
    notfirsth = False
    
    while total < 21:
      if default:
        time.sleep(1)
      if notfirsth:
        if train:
          print("")
          choice = suggest.recommend_move(player1,newplayer,p1,dealer1)
        if default:
          choice = input("Would you like to HIT or STAND? [h/s]\n> ")
          while choice not in ["h","s"]:
            print("Invalid choice. Please enter 'h' or 's'")
            choice = input("> ")
        if choice == "s":
          break
      print("")
      p1 = helpers.hit(drawncards,p1)
      print("")
      notfirsth = True
      total = sum(draw.card_sum(p1))
    print("")
    if total <= 21: 
      if default:
        time.sleep(1.5)
      print("You have",total)
    else:
      print(f"You busted ({total}), you lose!")
  
  return [total,drawncards]
