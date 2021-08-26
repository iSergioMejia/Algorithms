'''
Longest Common Subsquence Algorithm
Dynamic Programming
 Sergio A. Mejía - 2020
Python script for the solution of the problem 
"Given two sequences, find the largest subsequence (non continous) where it is
the same between the two sequences"

Recursive, Memoized, Bottom Up (with Backtracking) variants
'''
import math

def printMatrix(M):
  for i in range(len(M)):
    for j in range(len(M[i])):
      if M[i][j] == -math.inf:
        print(".", end="")
      else:
        print("x", end="")
    print("")

'''
Recursive Variant
  Recursively move in the two sequences. If the current items are the same, sum one to
  the result and call the recursion without both items. If they are not the same, try
  call the recursion without the first and without the other and choose the biggest result.
''' 
def LCS_Aux(A, B, i, j):
  if i == 0 or j == 0:
    return 0
  else:
    if A[ i - 1 ] == B[ j - 1 ]:
      return LCS_Aux(A, B, i - 1, j - 1) + 1
    else:
      left = LCS_Aux(A, B, i - 1, j)
      right = LCS_Aux(A, B, i, j - 1)
      return max(left, right)

'''
Memoized Variant
  Same as recursive, but the partial solutions are stored in M, so if this
  solution has been already calculated, the value of M is returned, instead of
  calculating it again.
'''
def LCS_Memo(A, B, i, j, M):
  if M[i][j] == -math.inf:
    if i == 0 or j == 0:
      M[i][j] = 0
    else:
      if A[ i - 1 ] == B[ j - 1 ]:
        M[i][j] = LCS_Memo(A, B, i - 1, j - 1, M) + 1
      else:
        left = LCS_Memo(A, B, i - 1, j, M)
        right = LCS_Memo(A, B, i, j - 1, M)
        M[i][j] = max(left, right)
  return M[i][j]

'''
Bottom Up (with Backtracking) Variant
  Calculate all of the partial solutions and saving in a S vector
  if the element is present in the solution.
'''
def LCS_BottomUp(A, B, i, j, M):
  S = [[ [0,0] for m in range(j+1)] for n in range(i+1)]
  for m in range(i):
    M[i][0] = 0
  for n in range(j):
    M[0][j] = 0
  for m in range(1, i+1):
    for n in range(1, j+1):
      if A[ m - 1 ] == B[ n - 1 ]:
        M[m][n] = M[ m - 1 ][ n - 1 ] + 1
        S[m][n] = [-1, -1]
      else:
        left = M[ m - 1 ][ n ]
        right = M[ m ][ n - 1 ]
        if left < right:
          M[m][n] = right
          S[m][n] = [0, -1]
        else:
          M[m][n] = left
          S[m][n] = [-1, 0]
  
  print(S)
  pos = [i,j]
  d = S[ pos[0] ][ pos[1] ]
  Sol = []
  
  while d[0] != 0 and d[1] != 0:
    pos[0] += d[0]
    pos[1] += d[1]
    if d[0] == -1 and d[1] == -1:
      Sol.append( A[pos[0] - 1] )
    d = S[ pos[0] ][ pos[1] ]
  
  return (M[i][j], Sol)


def LCS(A, B):
  M = [ [0 for i in range(len(B) + 1) ] for j in range(len(A) + 1)]

  # return(LCS_Memo(A, B, len(A), len(B), M))
  # return(LCS_Aux(A, B, len(A), len(B)))
  return(LCS_BottomUp(A, B, len(A), len(B), M))

A = "CASAGRE"
B = "COSAJAJE"
print(LCS(A, B))

'''[[[0, 0], [0, 0],   [0, 0], [0, 0], [0, 0]]
[[0, 0],  [-1, -1], [0, -1], [0, -1], [0, -1]]
[[0, 0],  [-1, 0],  [-1, 0], [-1, 0], [-1, -1]]
[[0, 0],  [-1, 0],  [-1, 0], [-1, -1], [-1, 0]]
[[0, 0],  [-1, 0],  [-1, 0], [-1, 0], [-1, -1]]]'''