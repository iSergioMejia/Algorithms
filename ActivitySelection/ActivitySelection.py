'''
Activity Selection Algorithm
Dynamic Programming
 Sergio A. Mejía - 2020
Python script for the solution of the problem 
"Select the biggest amount of activites that can fit
 in a certain time span given their start and finish hours"

Recursive, Memoized, Bottom Up (with Backtracking) and Greedy variants
'''

import random, math, time, sys

def PrintMatrix( M ):
  for i in range( len( M ) ):
    for j in range( len( M[i] ) ):
      if M[ i ][ j ] == -1:
        print( ".", end = "" )
      else:
        print( "x", end = "" )
    # end for
    print( "" )
  # end for
  print( "---------------------" )
# end def

'''
Greedy variant:
  Take the first activity and traverse the sequence
  finding the next activity that will fit after the current activity.
  This activity will be now the current activity. The algorithm
  finishes when all activities have been considered.
'''
def ActivitySelection_Greedy(S):
  T = [S[0]]
  k = 0
  for i in range(1, len(S)):
    if S[i][0] >= S[k][1]:
      T.append(S[i])
      k = i
  return T

'''
Recursive variant:
  Starting from the back, find the next activity that fits before the last one and
  recursively find the best result between considering this activity or not considering
  it and moving just to the next one.
'''
def Activity_Selection_Aux(S, i):
    if i == 0:
        return 0
    j = i - 1
    while j > 0 and S[j - 1][1] > S[i - 1][0]:
        j -= 1
    return max(Activity_Selection_Aux(S, i - 1), Activity_Selection_Aux(S, j) + 1)

'''
Memoized variant:
  Same as recursive, but the partial solutions are stored in M, so if this
  solution has been already calculated, the value of M is returned, instead of
  calculating it again.
'''
def Activity_Selection_Memo(S, i, M):
    if M[i] == -math.inf:
        if i == 0:
            M[i] = 0
        else:
            j = i
            while j > 0 and S[j - 1][1] > S[i - 1][0]:
                j -= 1
            left = Activity_Selection_Memo(S, i - 1, M)
            right = Activity_Selection_Memo(S, j, M) + 1
            if left < right:
                M[i] = right
            else:
                M[i] = left
    return M[i]

'''
Bottom Up (with Backtracking) variant:
  Calculate all of the partial solutions and saving in a B vector
  the index of the chosen solution in order to backtrack the solution.
'''
def Activity_Selection_BottomUp(S, n, M):
    B = [ -1 for i in range(n + 1) ]
    M[0] = 0
    for i in range(1, n + 1):
        j = i
        while j > 0 and S[j - 1][1] > S[i - 1][0]:
            j -= 1
        left = M[i - 1]
        right = M[j] + 1
        if left < right:
            M[i] = right
            B[i] = j
        else:
            M[i] = left
            B[i] = -1
    
    T = []
    j = n
    while j > 0 and B[j] == -1:
        j -= 1
    b = B[ j ]
    T.append( S[j - 1] )
    while b != 0:
        while B[b] == -1:
            b -= 1
        T.append(S[b - 1])
        b = B[b]
        
    T.reverse()
    return [M[j], T]

'''
Interface function
'''
def Activity_Selection(S):
    M = [ -math.inf for i in range(len(S)+1)]

    n3 = Activity_Selection_BottomUp(S, len(S), M)
    return n3

'''
In order to test the Greedy vs. DP, a lot of cases have to be made.
'''
def makeCases(n, size, end):
  S = []
  for _ in range(n):
    H = []
    for j in range(size):
      h = random.randint(1,end)
      H.append(h)
    H.sort()
    T = []
    for j in range(size):
      m = random.randint(0,H[j]-1)
      T.append([m,H[j]])
    S.append(T)
  return S

'''
S1 = [[1,4],[0,4],[2,5],[3,5],[4,6],[5,7],[6,9],[5,10]]
S2 = [[0,1],[1,2],[0,3],[2,3]]
S3 = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 9], [5, 9], [6, 10], [8, 11], [8, 12], [2, 14], [12, 16]]
S = [S1, S2, S3]
'''

## Check arguments
if len( sys.argv ) != 3:
    print( "Usage: ", sys.argv[ 0 ], "maxSize nCases" )
    exit( 1 )
## end if

endHour = 16
nCases = int(sys.argv[ 1 ])
for i in range(1,nCases+1):
  if i % 5 == 0:
    endHour += 2
  # print("Building cases...")
  S = makeCases(int(sys.argv[ 2 ]),i,endHour)
  # print("Done building cases.")
  sameAns = 0
  total = 0.0
  totalGreedyTime = 0.0
  totalDPTime = 0.0
  for Si in S:
    sGT = time.process_time( )
    resGreedy = ActivitySelection_Greedy(Si)
    eGT = time.process_time( )
    totalGreedyTime += float( eGT - sGT )
    
    sDPT = time.process_time( )
    resDP = Activity_Selection(Si)
    eDPT = time.process_time( )
    totalDPTime += float(eDPT - sDPT)
    resDP = resDP[1]
    if len(resGreedy) == len(resDP):
      equals = True
      for j in range(len(resGreedy)):
        if not (resGreedy[j][0] == resDP[j][0] and resGreedy[j][1] == resDP[j][1]):
          equals = False
      if equals:
        sameAns += 1
    total += 1
  percSameAns = sameAns/total 
  avgGreedyTime = totalGreedyTime/total
  avgDPTime = totalDPTime/total
  print(i,total,percSameAns, avgGreedyTime, avgDPTime)