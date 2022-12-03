import random

#class allwoing to create players and store points
class Player:
  def __init__(self, name):
    self.name=name
    self.totalPoints=0
  def showPlayer(self):
    print("%s - %d" %(self.name, self.totalPoints))

#func to create players
def createPlayers():
  playersNum = int(input("How much players would you like to create?\n"))
  players = []
  for i in range(playersNum):
    name=input("Provide player name:\n")
    player = Player(name)
    players.append(player)
  return players

#take players array and show them
def showPlayers(players):
  for player in players:
    print('\n')
    print("----------")
    print("%s - %d" %(player.name, player.totalPoints))
    print("----------")
    print('\n')

#throw a dice
def dicesThrow(n):
  dice = [1, 2, 3, 4, 5, 6]
  throw = []
  for i in range(n):
    throw.append(random.choice(dice))
  throw.sort()
  return throw

#calculate points supportive func
def calculateStandard(throw):
  points=0
  for i in throw:
    if i == 1:
      points+=100
    elif i == 5:
      points+=50
  return points

#calculate points
def calculatePoints(throw):
  points=0
  #multiple occurancies of 1
  if throw.count(1) == 3:
    points+=1000
    points += calculateStandard(list(filter(lambda n: n!=1, throw)))
  elif throw.count(1) == 4:
    points+= 2000 
    points += calculateStandard(list(filter(lambda n: n!=1, throw)))
  elif throw.count(1) == 5:
    points+= 10000 
  
  #multiple occurancies of 2
  elif throw.count(2) == 3:
    points += 200
    points += calculateStandard(list(filter(lambda n: n!=2, throw)))
  elif throw.count(2) == 4:
    points+=400 
    points += calculateStandard(list(filter(lambda n: n!=2, throw)))
  elif throw.count(2) == 5:
    points+=800
  
  #multiple occurancies of 3
  elif throw.count(3) == 3:
    points+=300
    points += calculateStandard(list(filter(lambda n: n!=3, throw)))
  elif throw.count(3) == 4:
    points+=600 
    points += calculateStandard(list(filter(lambda n: n!=3, throw)))
  elif throw.count(3) == 5:
    points+=900
  
  #multiple occurancies of 4
  elif throw.count(4) == 3:
    points+=400
    points += calculateStandard(list(filter(lambda n: n!=4, throw)))
  elif throw.count(4) == 4:
    points+=800 
    points += calculateStandard(list(filter(lambda n: n!=4, throw)))
  elif throw.count(4) == 5:
    points+=1200
  
  #multiple occurancies of 5
  elif throw.count(5) == 3:
    points+=500
    points += calculateStandard(list(filter(lambda n: n!=5, throw)))
  elif throw.count(5) == 4:
    points+=1000
    points += calculateStandard(list(filter(lambda n: n!=5, throw)))
  elif throw.count(5) == 5:
    points+=1500

  #multiple occurancies of 6
  elif throw.count(6) == 3:
    points+=600
    points += calculateStandard(list(filter(lambda n: n!=6, throw)))
  elif throw.count(6) == 4:
    points+=1200 
    points += calculateStandard(list(filter(lambda n: n!=6, throw)))
  elif throw.count(6) == 5:
    points+=1800 

  else:
      points = calculateStandard(throw)
  
  return points

#player decides if he wants to reroll or save points 
def decide(player, turnPoints):
  print("You can reroll or save your current points.")
  while(True):
    print("1. Reroll.")
    print("2. Keep points.")
    choice = int(input())
    if (choice == 1):
      break
    elif (choice == 2 and player.totalPoints+turnPoints<=8000):
      player.totalPoints += turnPoints
      player.showPlayer()
      break
    elif (choice == 2 and player.totalPoints+turnPoints>8000):
      print("You can't save points anymore, you have to run for 10k now!")
    else:
      print("I don't get it!")
  return choice

#player decides which dices would he like to keep
def keepDices(throw):
  keptDices = []
  print("Which dices would you like to keep?")
  print("Type 'd' when done.")
  i=1
  for dice in throw:
    print("%d. %d" % (i, dice))
    i+=1
  while(True):
    keepDice = input()
    if keepDice == 'd':
      break
    else:
      if (throw[int(keepDice)-1] == 1 or throw[int(keepDice)-1] == 5):
        keptDices.append(throw[int(keepDice)-1])

      else:
        print("You can't keep %d. You can keep 1 or 5 only." % throw[int(keepDice)-1])

  return keptDices

#func to manage turns
def turn(players):

  for player in players:

    #show player stats
    print("---------")
    print("Player: %s" % player.name)
    print("Points: %d" % player.totalPoints)
    print("---------")

    #player throw
    turnPoints = 0
    keptDices = []

    while True:
      throw = dicesThrow(5-len(keptDices))
      throwPoints = calculatePoints(throw) + calculateStandard(keptDices)
      turnPoints += throwPoints #probably this line should be somewhere else or line above 
      

      if (len(keptDices) > 0):
        print(keptDices)
      if (len(keptDices) == 5):
        print("You can't keep dices anymore... Save points or reroll 5 dices!")
        keptDices = []
        if (player.totalPoints < 1250 and turnPoints < 1250):
          print("You have to reach 1250 points first, rerolling...")
          throw = dicesThrow(5)
        else:
          choice = decide(player, turnPoints)
          if (choice == 1):
            throw = dicesThrow(5)
          elif (choice == 2):
            break
          
      print(throw)
      print(turnPoints)

      if (calculatePoints(throw) == 0):
        print("Bad luck, bad roll!")
        break
      elif (throw.count(1) >= 3 or throw.count(2) >= 3 or throw.count(3) >= 3 or throw.count(4) >= 3
        or throw.count(5) >= 3 or throw.count(6) >= 3):
        if (player.totalPoints < 1250 and turnPoints < 1250):
          print("You have to reach 1250 points first, rerolling...")
          keptDices=[]
        else:
          choice = decide(player, turnPoints)
          if (choice == 1):
            keptDices = []
            print("Rerolling...")
          elif (choice == 2):
            break
      else:
        if (player.totalPoints < 1250 and turnPoints < 1250):
          print("You have to reach 1250 points first, rerolling...")
          for dice in keptDices:
            if dice == 1:
              turnPoints -= 100
            elif dice == 5:
              turnPoints -= 50
          for dice in keepDices(throw):
              keptDices.append(dice)
          for dice in throw:
            if dice == 1:
              turnPoints-=100
            elif dice == 5: 
              turnPoints-=50
          print("Rerolling...")
        else:
          choice = decide(player, turnPoints)
          if (choice == 1):
            for dice in keptDices:
              if dice == 1:
                turnPoints -= 100
              elif dice == 5:
                turnPoints -= 50
            for dice in keepDices(throw):
              keptDices.append(dice)
            for dice in throw:
              if dice == 1:
                turnPoints-=100
              elif dice == 5: 
                turnPoints-=50
            print("Rerolling...")
          elif (choice == 2):
            break
      
def checkWin(players):
  for player in players:
    if (player.totalPoints >= 10000):
      print("End of the game!")
      showPlayers(players)
      return False
    else:
      return True

