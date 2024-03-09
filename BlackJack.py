import helpers
import draw
import time
import win_dealer
import split
import suggest

def main(odds_mode):
  '''
  Runs through BlackJack hands until the player chooses not to play again or the bank is empty

  odds_mode (bool) - if false automatic mode is default

  returns handnum (int) - number of hands played
  '''
  #skip mode selection if data mode on
  if odds_mode:
    print("Welcome to BlackJack Simulator v2.6\n")
    default = True
    train = helpers.mode_input()
  else:
    train = "a"
  
  #initiate mode so bet and bank input can be skipped for automatic and data modes
  if train == "a":
    default = False
    train = True
  elif train == "t":
    train = True
  else:
    train = False

  if default:
    bank = helpers.bank_input()
  else:
    bank = 100
    bet = 10
    
  handnum = 0
  playagain = "y"
  startbank = bank
  while bank > 0 and playagain == "y":
    handnum += 1
    
    bet = helpers.bet(bank,handnum,default)

    #seedcard is sentinel for card selection loop to be entered
    drawncards = ["seedcard"]
    playercards = []
    dealercards = []

    #add card to drawn cards to allow checking for duplicates
    player1 = draw.card(drawncards)
    drawncards.append(player1)
    player2 = draw.card(drawncards)
    drawncards.append(player2)
    dealer1 = draw.card(drawncards)
    drawncards.append(dealer1)
    dealer2 = draw.card(drawncards)
    drawncards.append(dealer2)

    #create list of numerical card values for calculations
    playercards = draw.value_list(playercards,player1)
    playercards = draw.value_list(playercards,player2)
    dealercards = draw.value_list(dealercards,dealer1)
    dealercards = draw.value_list(dealercards,dealer2)

    helpers.new_hand(player1,player2,dealer1)
    
    #check to see if player or dealer has blackjack, no insurance option in program
    bj1 = helpers.first_blackjack(playercards, dealercards,bet,bank)
    if type(bj1) == int:
      bank = bj1
    else:
      #if train == true best move recommended
      if train:
        choice = suggest.recommend_move(player1,player2,playercards,dealer1)
      #if default == false move option is not prompted and best move auto implemented
      if default:
        choice = helpers.choice(player1,player2,bet,bank)

      if choice == "s":
        print("")
        dealertotal = helpers.stay(dealer1,dealer2,dealercards,drawncards,default)
        print("")

        playertotal = sum(playercards)
        bank = win_dealer.eval_win(playertotal,dealertotal,bet,bank)
      
      elif choice == "dd":
        bet = bet * 2 
        print("")
        if default:
          time.sleep(1)
        total = sum(draw.card_sum(helpers.hit(drawncards,playercards)))
        print("")
        #if additional card makes sum <=21, evaluate win vs dealer cards, otherwise its a bust/automatic loss
        if total <= 21: 
          if default:
            time.sleep(1.5)
          dealertotal = helpers.stay(dealer1,dealer2,dealercards,drawncards,default)
          bank = win_dealer.eval_win(total,dealertotal,bet,bank)
        else:
          print(f"You busted ({total}), you lose!")
          bank = bank + bet * -1

      elif choice == "h":
        total = sum(playercards)
        notfirsth = False
        
        #allow for hit or stay until total >= 21
        while total < 21:
          if default:
            time.sleep(1)
          if notfirsth:
            if train:
              choice = suggest.recommend_move(player1,player2,playercards,dealer1)
            if default:
              choice = input("Would you like to HIT or STAND? [h/s]\n> ")
              while choice not in ["h","s"]:
                print("Invalid choice. Please enter 'h' or 's'")
                choice = input("> ")
            if choice == "s":
              break
          print("")
          playercards = helpers.hit(drawncards,playercards)
          print("")
          notfirsth = True
          total = sum(draw.card_sum(playercards))
        print("")
    
        if total <= 21: 
          if default:
            time.sleep(1.5)
          dealertotal = helpers.stay(dealer1,dealer2,dealercards,drawncards,default)
          bank = win_dealer.eval_win(total,dealertotal,bet,bank)
        else:
          print(f"You busted ({total}), you lose!")
          bank = bank + bet * -1
      else:
        bank = split.logic(player1,player2,dealer1,dealer2,playercards,dealercards,bet,bank,handnum,drawncards,train,default)
    
    #every 10 hands ask to continue play, skipped if data mode is on
    if default:
      if handnum % 10 == 0:
        playagain = input("Would you like to continue playing? [y/n]\n> ")
        while playagain not in ["y","n"]:
          playagain = input("Invalid Input")
        print("")
    if handnum % 1000 == 0:
      break
  print("\nThanks for playing!")
  #data on gains/losses with respect to number of played hands
  print(f"You played {handnum} hands and finished with ${bank}")
  if bank == startbank:
    print("You broke even")
  elif bank < startbank:
    percent = ((startbank - bank)/startbank) * 100
    print(f"You lost ${startbank - bank}, that's a {percent}% loss")
  else:
    percent = int(((bank - startbank)/bank) * 100)
    print(f"You earned ${bank - startbank}, that's a {percent}% return")
  return handnum
