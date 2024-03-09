import random

def card(drawncards):
  '''
  Generates a card not in drawncards list and returns it
  '''
  #drawncards starts as ["seedcard"] to allow this loop to be entered
  card = "seedcard"
  while card in drawncards:
    
    card = random.randint(1,13)
    suit = random.randint(1,4)

    if suit == 1:
      suit = " of Clubs"
    elif suit == 2:
      suit = " of Diamonds"
    elif suit == 3:
      suit = " of Hearts"
    else:
      suit = " of Spades"

    #only face cards start with letters, so logic required
    if card == 1:
      card = "Ace"
    elif card == 11:
      card = "Jack"
    elif card == 12:
      card = "Queen"
    elif card == 13:
      card = "King"
    else:
      card = str(card)

    card = card + suit
  return card


def card_value(card):
  '''
  Takes in card and returns numeric value
  '''
  val = card[0]
  #for all cards except for face cards and 10 card[0] = value, so this is used to determine the value of those 
  if val == "A":
    return 11
  elif val == "K" or val == "Q" or val == "1" or val == "J":
    return 10
  else:
    return int(val)


def card_sum(cardlist):
  '''
  Evaluates a cardlist to allow for aces. Follows classic blackjack logic by converting an existing ace to 1 if total is over 21

  Returns a list of each card's value after changing aces if necesssary
  '''
  total = 0
  total = sum(cardlist)
  
  #critical to the blackjack logic. If the combined value is over 21 and an ace is in the list, the ace value becomes 1.
  while total > 21 and 11 in cardlist:
    cardlist[cardlist.index(11)] = 1
    total = sum(cardlist)
  return cardlist

def value_list(cardlist, card):
  '''
  Adds a card (string) to the cardlist of numeric values by converting card to its numeric value

  Retuns cardlist with card concatenated
  '''
  card = card_value(card)
  return cardlist + [card]
