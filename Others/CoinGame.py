'''
Activity Selection Algorithm
Dynamic Programming
 Sergio A. Mejía - 2020
Python script for the solution of the problem 
"Given a sequence of values representing coins, take one coin from one of the edges
and let another player take the next coin from one of the edges. What is the greatest
amount of money you can earn?"

Recursive, Bottom Up and Greedy variants
'''

def printMatrix( E ):
  print( "-----------------" )
  for i in range( len( E[ 0 ] ) ):
    for j in range( len( E ) ):
      print( E[ i ][ j ], end = "\t" )
    print( "" )
  print( "-----------------" )

'''
Recursive Variant
  There are 4 cases in each step of the game.
  You take the leftmost coin and the other player takes the rightmost (1) 
    or the new leftmost coin (2)
  You take the rightmost coin and the other player take the leftmost (3)
    ot the new rightmost coin (4)
  Choose the best of the result of recursively calling these 4 cases. If there
  are no coins the earned amount is 0.
'''
def CoinGame_Aux(S, i, j):
  if i >= j:
    return 0
  else:
    op1 = S[i - 1] + CoinGame_Aux(S, i+1, j-1)
    op2 = S[i - 1] + CoinGame_Aux(S, i+2, j)
    op3 = S[j - 1] + CoinGame_Aux(S, i+1, j-1)
    op4 = S[j - 1] + CoinGame_Aux(S, i, j-2)
    return max(op1, op2, op3, op4)

'''
Bottom Up Variant
  Define a memoized matrix of size |S|+1. Find all the possible partial solutions
  represented as the positions of this matrix using the logic of the recursive
  solution. The matrix should be traversed through its diagonals starting
  from the upper-left position (0,2) and going down and right. (Showing below the order).
  The matrix diagonal must be full with 0s. 
     ----> 
    ..1.6.9
  | ...2.7.
  | ....3.8
  | .....4.
  | ......5
  v .......
    ....... 
'''
def CoinGame_BottomUp(S):
  M = [[0 for b in range(len(S)+1)] for a in range(len(S)+1)]
  i = 2
  n = len(S)
  while i <= n:
    a = 0
    b = i
    while b <= n:
      # print(a, b)
      op1 = M[a+1][b-1] + S[a]
      op2 = M[a+1][b-1] + S[b - 1]
      op3 = M[a+2][b] + S[a]
      op4 = M[a][b-2] + S[b - 1]
      M[a][b] = max(op1, op2, op3, op4)
      b += 1
      a += 1
    i += 2
  # printMatrix(M)
  return M[0][n]

'''
Greedy Variant
  Intuitive version of the solution, where in each step of the
  game you choose the greatest coin of the two available and
  then the other player choose the worst of the two new available.
'''
def CoinGame_Greedy(S):
  i = 0
  j = len(S)-1
  R = 0
  while i < j:
    # print(i,j)
    if S[i] < S[j]:
      R += S[j]
      if S[i] <= S[j - 1]:
        i += 1
        j -= 1
      else:
        j -= 2
    else:
      R += S[i]
      if S[i+1] <= S[j]:
        i += 2
      else:
        j -= 1
        i += 1
  return R

'''
Interface function for the other recursive function
'''
def CoinGame(S):
  return CoinGame_Aux(S, 1, len(S))

S = [6, 9, 1, 2, 16, 8]
# S = [8, 15, 3, 7 ]
S = [100, 500, 50, 1000, 100, 200, 50, 1000, 200, 50]
S = [20, 30, 2, 2, 2, 10]
S = [1, 6, 3, 4, 5, 2]
print(CoinGame(S))
print(CoinGame_BottomUp(S))
print(CoinGame_Greedy(S))