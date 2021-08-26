import math

def printMatrix(M):
  for i in range(len(M)):
    for j in range(len(M[i])):
      if M[i][j] == math.inf:
        print(".", end="")
      else:
        print("x", end="")
    print("")

def w(P, Q, i, j):
  accum = 0
  for l in range(i, j+1):
    accum += P[l-1]
  for l in range(i-1, j+1):
    accum += Q[l]
  return accum

def defTreeOptimalStructure_Aux(P, Q, i, j):
  if j == i - 1:
    return Q[i - 1]
  else:
    mini = math.inf
    for r in range(i, j+1):
      val = defTreeOptimalStructure_Aux(P, Q, i, r-1) + defTreeOptimalStructure_Aux(P, Q, r+1, j) + w(P, Q, i, j)
      if val < mini:
        mini = val
    return mini

def defTreeOptimalStructure_Memo(P, Q, i, j, M):
  if M[i][j] == math.inf:
    if j == i - 1:
      M[i][j] = Q[i - 1]
    else:
      mini = math.inf
      for r in range(i, j+1):
        val = defTreeOptimalStructure_Memo(P, Q, i, r-1, M) + defTreeOptimalStructure_Memo(P, Q, r+1, j, M) + w(P, Q, i, j)
        if val < mini:
          mini = val
      M[i][j] = mini
  return M[i][j]

def defTreeOptimalStructure(P, Q):
  M = [ [math.inf for j in range(len(Q)+1)] for i in range(len(Q)+1)]
  n1 = defTreeOptimalStructure_Aux(P, Q, 1, len(P))
  n2 = defTreeOptimalStructure_Memo(P, Q, 1, len(P), M)
  printMatrix(M)
  return [n1, n2]

P = [ 0.15, 0.10, 0.05, 0.10, 0.20]
Q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
print(defTreeOptimalStructure(P,Q))
