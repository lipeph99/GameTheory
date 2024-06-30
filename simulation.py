import random

_MEET_COUNT = 100 #Number of generations
_GROUP_COUNT = 50 #Amout of groups
_PRISIONER_COUNT = 10 #Prisioners per group
_MUT_VALUE = 10 #Mutation range for agressivity
_FIGHT_ROUNDS = 10 #Numer of fights between each round of cooperation
_FIGHT_COUNT = 3 #Number of fights started by each prisioner
_PAYOFF = [[9,0], [10,1]] #Prisioners dilemma table k1, k2, P in the paper

#A group is created using a list of prisioners
class Group:
  def __init__(self, prisList):
    self.prisList = prisList
    cumChance = 0
    self.total = 0
    for pris in prisList:
      self.total += pris.points
      cumChance += pris.atkChance
    self.avg = cumChance / _PRISIONER_COUNT

#A prisioner is created using the attack chance of a previous prisioner
class Prisoner:
  def __init__(self, chance):
    newChance = random.randint(-_MUT_VALUE, _MUT_VALUE) + chance
    self.atkChance = min(max(newChance, 0), 100)
    self.points = 0
  def addPoints(self, points):
    self.points += points

#Cooperation mode - the group with the higher average wins
def groupFight(g1, g2):
  #print(g1.total, g2.total)
  if (g1.total > g2.total):
    return groupReproduce(g1)
  else:
    return groupReproduce(g2)

#Each member of the winner group reproduces exactly once, creating a new group without any member of the old group remaining alive
def groupReproduce(g):
  newList = []
  #printList(g.prisList)
  for pris in g.prisList:
    newList.append(Prisoner(pris.atkChance))
  return Group(newList)

#2 prisioners fight, both get their points accordingly
def fight(p1,p2):
  d1 = 1 if random.randint(0, 100) <= p1.atkChance else 0
  d2 = 1 if random.randint(0, 100) <= p2.atkChance else 0
  p1.addPoints(_PAYOFF[d1][d2])
  p2.addPoints(_PAYOFF[d2][d1])
  #print("fight: ", p1.atkChance, p2.atkChance, d1, d2, _PAYOFF[d1][d2], _PAYOFF[d2][d1])

#The prisioner with the most points reproduce, no member of the old group is kept alive
def reproduce(p1,p2):
  #print("rep: ", p1.atkChance, p1.points, p2.atkChance, p2.points,)
  if (p1.points > p2.points):
    return Prisoner(p1.atkChance)
  else:
    return Prisoner(p2.atkChance)

#Use this function to print all members of a given group
def printList(prisonList):
  total = 0
  for i in range(_PRISIONER_COUNT):
    total += prisonList[i].atkChance
    print(prisonList[i].atkChance, end=' ')
  total /= _PRISIONER_COUNT
  print(" -- ", total)

#Calculates the average agressivity of all the groups
def printAvg(groupList):
  total = 0
  for g in groupList:
    total += g.avg
  total /= _GROUP_COUNT
  print("%.2f" % total)

#Creating first generation of prisioners with average agressivity of 50
groupList = []
for _ in range(_GROUP_COUNT):
  prisonList = []
  for _ in range(_PRISIONER_COUNT):
    prisonList.append(Prisoner(50)) #Change this value to start with a different agressivity average
  groupList.append(Group(prisonList))
  
#for p in prisonList:
  #print(p.atkChance)

#printList()

#Prints the starting population, only used for tests 1 and 2 in the paper
#for group in groupList:
#  print(group.avg)

#print()

for meet in range(_MEET_COUNT):
  #Starts every prisioner points with 0 and run all theirs fights
  for idx, group in enumerate(groupList):
    #printList(group.prisList)
    prisonList = group.prisList
    for j in range(_FIGHT_ROUNDS):
      for pris in prisonList:
        pris.points = 0
      for pris in prisonList:
        for i in range(_FIGHT_COUNT):
          enemy = prisonList[random.randint(0, _PRISIONER_COUNT - 1)]
          while (pris == enemy):
            enemy = prisonList[random.randint(0, _PRISIONER_COUNT - 1)]
          fight(pris, enemy)
          #End of fights
      
      #print(prisonList[j].points)
      #A single fight without reproduction is needed in order to give points to the prisioners, as each new prisioner is always created with 0 points
      newList = []
      for pris in prisonList:
        enemy = prisonList[random.randint(0, _PRISIONER_COUNT - 1)]
        while (pris == enemy):
          enemy = prisonList[random.randint(0, _PRISIONER_COUNT - 1)]
        newList.append(reproduce(pris, enemy))
      group = Group(newList)
      groupList[idx] = group
      prisonList = newList
      #printList(group.prisList)
    #print(group.avg)
    #End of points fight

  #A single fight without reproduction is needed in order to give points to the prisioners, as each new prisioner is always created with 0 points
  newGroup = []
  for idx, group in enumerate(groupList):
    prisonList = group.prisList
    for j in range(_FIGHT_ROUNDS):
      for pris in prisonList:
        pris.points = 0
      for pris in prisonList:
        for i in range(_FIGHT_COUNT):
          enemy = prisonList[random.randint(0, _PRISIONER_COUNT - 1)]
          while (pris == enemy):
            enemy = prisonList[random.randint(0, _PRISIONER_COUNT - 1)]
          fight(pris, enemy)
  #End of points fight

  #Group reproduction
  for idx, group in enumerate(groupList):
    enemy = groupList[random.randint(0, _GROUP_COUNT - 1)]
    while (group == enemy):
      enemy = groupList[random.randint(0, _GROUP_COUNT - 1)]
    newGroup.append(groupFight(Group(group.prisList), Group(enemy.prisList)))
  groupList = newGroup

  printAvg(groupList)
  
#print()  

for group in groupList:
  print(group.avg)
