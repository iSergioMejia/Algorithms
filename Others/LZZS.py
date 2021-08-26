'''
Largest Increasing Subsquence Algorithm
Dynamic Programming
 Sergio A. Mejía - 2020
Python script for the solution of the problem 
"Given a sequence, find the largest homogeneous zigzag subsequence, this is, that
  a_0 < a_1 > a_2 < ... > a_i or
  a_0 > a_1 < a_2 > ... < a_i  

Recursive, Memoized, Bottom Up (with Backtracking) variants
'''
import math

def LZZS_Aux(S, i, w):
  if i == 0:
    return 0
  else:
    j = i - 1
    if w == 0:
      while j > 0 and S[j - 1] >= S[i - 1]:
          j -= 1
      return max(LZZS_Aux(S, i - 1, 0), LZZS_Aux(S, j, 1) + 1)
    elif w == 1:
      while j > 0 and S[j - 1] <= S[i - 1]:
        j -= 1
      return max(LZZS_Aux(S, i - 1, 1), LZZS_Aux(S, j, 0) + 1)

def LZZS_Memo(S, i, w, M):
  if M[i][w] == -math.inf:
    if i == 0:
      M[i][w] = 0
    else:
      j = i - 1
      if w == 0:
        while j > 0 and S[j - 1] >= S[i - 1]:
            j -= 1
        M[i][w] = max(LZZS_Memo(S, i - 1, 0, M), LZZS_Memo(S, j, 1, M) + 1)
      elif w == 1:
        while j > 0 and S[j - 1] <= S[i - 1]:
          j -= 1
        M[i][w] = max(LZZS_Memo(S, i - 1, 1, M), LZZS_Memo(S, j, 0, M) + 1)
  return M[i][w]

def LZZS_BottomUp(S):
  n = len(S)
  M = [ [-math.inf for j in range(2)] for i in range(len(S) + 1)]
  B = [ [[-1, -1] for j in range(2)] for i in range(len(S) + 1)]
  
  M[0][0] = M[0][1] = 0
  
  for i in range(1, n+1):
    for w in range(2):
      j = i - 1
      if w == 0:
        while j > 0 and S[j - 1] >= S[i - 1]:
            j -= 1
        left = M[i - 1][0] 
        right = M[j][1] + 1
        if left > right:
          M[i][w] = left
          B[i][w] = [i-1, 0]
        else:
          M[i][w] = right
          B[i][w] = [j, 1]
      elif w == 1:
        while j > 0 and S[j - 1] <= S[i - 1]:
          j -= 1
        left = M[i - 1][1]
        right = M[j][0] + 1
        if left > right:
          M[i][w] = left
          B[i][w] = [i-1, 1]
        else:
          M[i][w] = right
          B[i][w] = [j, 0]

  # FALTA EL BACKTRACKING
  BT = [[B[j][i] for j in range(len(B))] for i in range(len(B[0]))]
  print(BT)
  
  return max(M[n][0], M[n][1])


def LZZS(S):
  nA1 = LZZS_Aux(S, len(S), 0)
  nA2 = LZZS_Aux(S, len(S), 1)

  M = [ [-math.inf for j in range(2)] for i in range(len(S) + 1)]
  nM1 = LZZS_Memo(S, len(S), 0, M)
  M = [ [-math.inf for j in range(2)] for i in range(len(S) + 1)]
  nM2 = LZZS_Memo(S, len(S), 1, M)

  nB = LZZS_BottomUp(S)
  return [max(nA1, nA2), max(nM1, nM2), nB]

S = [1, 2, 1, 3, 3, 4, 1]
print(LZZS(S))
