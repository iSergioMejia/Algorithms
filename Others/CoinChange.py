'''
Coin Change Algorithm
Dynamic Programming
 Sergio A. Mejía - 2020
Python script for the solution of the problem 
"Given an amount and a set of coin values,
 What is the minimum amount of coins you can use to make that amount?"

Recursive, Memoized, Bottom Up (with Backtracking) variants
'''

import math

'''
Recursive Variant
  Recursively evaluate all posible changes using a coin/bill of each value only if this value 
  is less or equal than the giving change. Call the recursion with the substraction of this coin
  denomination and storage the minimum of the returned values
''' 
def CoinChange_Aux( P, C ):
  # Base case: The change value is 0
  if C == 0:
    return 0
  else:
    change = math.inf
    # Recursive case: Evaluate all posible changes using a coin/bill of each value only if this value is less or equal than the giving change
    for y in P:
      if y <= C:
        print(C, y)
        x = CoinChange_Aux(P, C - y) + 1
        if x < change:
          change = x
    #end for
    return change

'''
Memoized variant:
  Same as recursive, but the partial solutions are stored in M, so if this
  solution has been already calculated, the value of M is returned, instead of
  calculating it again.
'''
def CoinChange_Memo( P, C, M ):
  # As we want to minimize, the memo matrix starts with +inf
  if M[C] == math.inf:
    if C == 0:
      M[C] = 0
    else:
      change = math.inf
      for y in P:
        if y <= C:
          x = CoinChange_Memo(P, C - y, M) + 1
          if x < change:
            change = x
      #end for
      M[C] = change
  return M[C]

'''
Bottom Up (with Backtracking) Variant
  Calculate all of the possible partial solutions filling up the memoized vector.
  Each position of M is calculated with the previously calculated values.
  In addition, a T vector is defined saving which coin denomitation was used to give the change
  in each of the corresponding states.
'''
def CoinChange_BottomUp(P, C, M):
  # The BT matrix will save which value was used to give the change in the corresponding state
  T = [0 for i in range(C + 1)]
  M[0] = 0
  for i in range(1, C+1):
    change = math.inf
    for y in P:
      if y <= i:
        x = M[i - y] + 1
        if x < change:
          change = x
          T[i] = y
    #end for
    M[i] = change
  # end for
  # Declaration of a dict that will save the amount of coins/bills of each value to give the change
  B = {}
  for i in range(len(P)):
    # At the start, none coin or bill is given for the change
    B[P[i]] = 0
  x = C
  while x != 0:
    # 1 is added to the used value
    B[T[x]] += 1
    x = x - T[x]
  return [M[C], B]

'''
Interface function to call the other functions
'''
def CoinChange(P, C):
  M = [ math.inf for i in range(C+1)]
  n = CoinChange_BottomUp(P, C, M)
  return n

P = [1, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]
print(CoinChange(P, 23017))
