'''
 Minesweeper Algorithm
 Brute Force and Heuristic Algorithms
  Sergio A. Mejia - 2020
 Python script for the problem "Given a Minesweeper
 game, solve it programatically"
'''

import math, random, itertools

offset = [
  [-1, -1], [-1, 0], [-1, 1],
  [0,  -1],          [0,  1],
  [1,  -1], [1,  0], [1,  1]
]

def PrintMatrix( M ):
  for i in range( len( M ) ):
    for j in range( len( M[i] ) ):
      res = "{:.2f}".format(M[ i ][ j ] )
      print( "\t",res, end = "" )
    # end for
    print( "" )
  # end for
  print( "---------------------" )
# end def

def PrintBombs(M):
  for i in range( len( M ) ):
    for j in range( len( M[i] ) ):
      if M[ i ][ j ]["bomb"] != True:
        print( ".\t", end = "" )
      else:
        print( "x\t", end = "" )
    # end j for
    print( "" )
  # end i for
  print( "---------------------")
# end def

def getCertainCoordinate( P ):
  for i in range(len(P)):
    for j in range(len(P[i])):
      if P[i][j] == math.inf:
        return [i, j]
    #end j for
  #end i for
  return None

def getLeastProbableCoordinate( P, M ):
  minP = math.inf
  options = []
  for i in range(len(P)):
    for j in range(len(P[i])):
      if M[i][j]["hidden"] == True:
        if P[i][j] == minP:
          minP = P[i][j]
          options.append([i, j])
        elif P[i][j] < minP:
          minP = P[i][j]
          options = [[i, j]]
  idx = random.randint(0, len(options)-1)

  return options[idx]

def verifyWin( M ):
  for i in range(len(M)):
    for j in range(len(M[i])):
      if M[i][j]["bomb"] == True and M[i][j]["flagged"] != True:
        return False
  return True

def CalcProbabilities( M ):
  coveredCount = 0.0
  totalBombs = 0.0
  for i in range(len(M)):
    for j in range(len(M[i])):
      if M[i][j]["hidden"] == True and M[i][j]["flagged"] != True:
        coveredCount += 1 
      if M[i][j]["bomb"] == True and M[i][j]["flagged"] != True:
        totalBombs += 1  
    #end j for
  #end i for
  P = [ ]
  for i in range(len(M)):
    row = []
    for j in range(len(M[i])):
      if M[i][j]["hidden"] != True:
        row.append(0.0)
      else:
        row.append(totalBombs/coveredCount)
    #end j for
    P.append(row)
  #end i for
  Count = [ [ 0.0 for j in range(len(M[i]))] for i in range(len(M))]
  for i in range(len(M)):
    for j in range(len(M[i])):
      if M[i][j]["hidden"] != True:
        count = 0.0
        tot = 0.0
        for k in range(len(offset)):
          di = i + offset[k][0]
          dj = j + offset[k][1]
          if 0 <= di < len(M) and 0 <= dj < len(M[i]):
            if M[di][dj]["bomb"] == True and M[di][dj]["flagged"] != True:
              count += 1
            if M[di][dj]["hidden"] == True and M[di][dj]["flagged"] != True:
              tot += 1
        #end offset for
        percent = 0
        if tot != 0:
          percent = count/tot
        Count[i][j] = count
        for k in range(len(offset)):
          di = i + offset[k][0]
          dj = j + offset[k][1]
          if 0 <= di < len(M) and 0 <= dj < len(M[i]):
            if M[di][dj]["hidden"] == True and M[di][dj]["flagged"] != True:
              if count == tot:
                P[di][dj] = math.inf #If I'm certain that there is a bomb, probability is 100% (Marked as inf so that no other probability disturbs it)
              else:
                P[di][dj] *= percent
        #end offset for
    #end j for
  #end i for
  # PrintMatrix(P)
  # PrintMatrix(Count)
  return P

def initializeM(n, m, nbombs):
  M = []
  for _ in range(n):
    row = []
    for _ in range(m):
      tile = {"hidden":True, "flagged":False, "bomb":False}
      row.append(tile)
    #end for
    M.append(row)
  #end for
  
  for i in range(nbombs):
    x = random.randint(0,n-1)
    y = random.randint(0,m-1)
    while M[x][y]["bomb"] == True:
      x = random.randint(0,n-1)
      y = random.randint(0,m-1)
    M[x][y]["bomb"] = True
  
  return M

def Test_HeuristicMinesweeper(n, m, nbombs, tries):
  winCount = 0.0
  for i in range(tries):
    M = initializeM(n, m, nbombs)
    # if i % 20 == 0:
      # print("Testing... ", float(i)/tries*100, "%")
    while(True):
      P = CalcProbabilities(M)
      '''mark = input("> ")

      x = int(mark[0])
      y = int(mark[2])
      O = mark[4]'''
      certain = getCertainCoordinate(P)
      if certain != None:
        M[certain[0]][certain[1]]["flagged"] = True
        # print("I have covered", certain[0],certain[1])
        win = verifyWin( M )
        if win:
          # print("Win")
          winCount += 1
          break
      else:
        step = getLeastProbableCoordinate(P, M)
        M[step[0]][step[1]]["hidden"] = False
        # print("I have uncovered", step[0],step[1])
        if M[step[0]][step[1]]["bomb"] == True:
          # print("Lost")
          break
    #end while
  #end for
  return winCount / tries

'''
Solution is O(knm) where k is number of steps.
Victory percent (Gotten from Test function):
  8x8, 10 bombs: 16-30%
  16x16, 40 bombs: 12-21%
  30x16, 99 bombs: 0-1%
'''  
def Heuristic_Minesweeper(M):
  PrintBombs(M)
  continueGame = True
  win = False
  while(continueGame):
    P = CalcProbabilities(M)

    #Try to get a certain bomb
    certain = getCertainCoordinate(P)
    if certain != None:
      #Cover the certain bomb
      M[certain[0]][certain[1]]["flagged"] = True
      print("I have covered", certain[0],certain[1])
      #Verify if covering this bomb made me win
      win = verifyWin( M )
      if win:
        continueGame = False
        win = True
    #If not certain bomb was found, get least probable coord
    else:
      step = getLeastProbableCoordinate(P, M)
      M[step[0]][step[1]]["hidden"] = False
      print("I have uncovered", step[0],step[1])
      #After uncovering, check if I've hit a bomb
      if M[step[0]][step[1]]["bomb"] == True:
        continueGame = False
        win = False
  #end while
  return win

# Brute Force, solution is O( nm * C(nm, b) )
def BruteForce_Minesweeper(M):
  PrintBombs(M)
  size = n*m
  for p in itertools.combinations(range(size), nbombs):
    for i in range(len(M)):
      for j in range(len(M[i])):
        M[i][j]["flagged"] = False
    for bombP in p:
      x = bombP // n
      y = bombP % n
      M[x][y]["flagged"] = True
    win = verifyWin( M )
    if win:
      return p


n = 8
m = 8
nbombs = 10
M = initializeM(n, m, nbombs)
win = Heuristic_Minesweeper(M)
# sol = BruteForce_Minesweeper(M)
# print(Test_HeuristicMinesweeper(n, m, nbombs, 100))
if win:
  print("Win")
else:
  print("Lost")