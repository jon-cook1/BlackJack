import BlackJack

def main():
  '''
  Runs through BlackJack trainer. Stops if the user attempts to split three times on one hand (currently unsupported)
  '''
  try:
    #true parameter allows for mode selection in game
    BlackJack.main(True)
  except UnboundLocalError:
    print("*"*25)
    print("*"*25)
    print("Sorry, BlackJack trainer is currently unable to support triple splits.\nFortunately a triple split is the best move to make only once in every ~15000 hands")

#-----#
main()
#-----#


#-------------data modes, not gameplay-----------
def gambling_odds():
  '''
  Automatically plays best move until bank == 0, then repeats 99 more times and finds average # of hands to lose 100

  *takes around 10 minutes to run with an average of ~411*
  '''
  avg = 0
  onekhandcount = 0
  errorcount = 0
  for i in range(100):
    try:
      #false parameter allows for mode selection, bank and bet input, and move to be skipped
      #this allows for automatic hands to be played very quickly for data collection
      step = BlackJack.main(False)
      avg += step
      if step == 1000:
        onekhandcount += 1
    #stop if triple split attempted
    except UnboundLocalError:
      errorcount += 1

  avg = avg / (100 - errorcount)

  print("Average hands before losing $100:",avg)
  print("Games over 1000 hands:",onekhandcount)


def triple_split_calc():
  '''
  dev function used to find average amount of hands played before unsupported triple split

  *took around 30 minutes to run and found an average of 15,000 hands before a triple split is recommended* 
  '''
  tsplit = 0
  handnum = 0
  while tsplit < 10:
    try:
      step = BlackJack.main(False)
      handnum += step
    #only possible error, means ai best move recommended triple splt
    except UnboundLocalError:
      tsplit += 1
  handnum = handnum / 10
  print("\n\nFound 10 triple splits")
  print("Average number of hands before triple split:",handnum)

#-------------------#
#gambling_odds()
#triple_split_calc()
#-------------------#


