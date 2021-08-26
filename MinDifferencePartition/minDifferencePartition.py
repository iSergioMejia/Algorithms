'''
Minimum Difference Partition Algorithm
 Dynamic Programming
Sergio A. Mejía - 2020
Java class for the solution of the problem 
"Divide a set into two subsets such that the difference
of the subsets element sums is the minimum"

Recursive, Memoized and BottomUp (with Backtracking) variants
'''
import math

def PrintMatrix( M ):
  for i in range( len( M ) ):
    for j in range( len( M[i] ) ):
      if M[ i ][ j ] == math.inf:
        print( ".", end = "" )
      else:
        print( "x", end = "" )
    # end for
    print( "" )
  # end for
  print( "---------------------" )
# end def

def PrintBoolMatrix( M ):
  for i in range( len( M ) ):
    for j in range( len( M[i] ) ):
      if M[ i ][ j ]:
        print( ".", end = "" )
      else:
        print( "x", end = "" )
    # end for
    print( "" )
  # end for
  print( "---------------------" )
# end def

# For documentation, see the Java class xd
def minSubset_Aux(A, i, C_1, C_2):
  if i == 0:
    return abs(C_1 - C_2)
  else:
    return min(minSubset_Aux(A, i-1, C_1 + A[i - 1] , C_2),
               minSubset_Aux(A, i-1, C_1, C_2 + A[i - 1]))

# For documentation, see the Java class xd
def minSubset_Memo(A, i, C_1, C_2, M):
  key = abs(C_1 - C_2)
  if M[i][key] == math.inf:
    if i == 0:
      M[i][key] = abs(C_1 - C_2)
      # print(C_1, C_2)
      # PrintMatrix(M)
    else:
      M[i][key] = min(minSubset_Memo(A, i-1, C_1 + A[i - 1] , C_2, M),
                minSubset_Memo(A, i-1, C_1, C_2 + A[i - 1], M))
      # print(C_1, C_2)
      # PrintMatrix(M)
  return M[i][key]

# For documentation, see the Java class xd
def minSubset_BottomUp(A, n):
  suma = 0
  for val in A:
    suma += abs(val)

  M = [ [0 for j in range(suma*2+1)] for i in range(len(A)+1)]
  T = [ [False for j in range(suma*2+1)] for i in range(len(A)+1)]

  for j in range(2*suma + 1):
    M[0][j] = abs(j - suma)

  for i in range(1, n+1):
    for j in reversed(range(0, 2*suma+1)):
      n1 = math.inf
      n2 = math.inf
      right = j + A[i-1]
      left  = j - A[i-1]
      if 0 <= left <= 2*suma:
        n1 = M[i-1][left]
      if 0 <= right <= 2*suma:
        n2 = M[i-1][right]
      # print("i=%f, j1=%f, j2=%f n1=%f, n2=%f"%(i-1,right, left,n1,n2))
      if n1 < n2: #Left
        M[i][j] = n1
        T[i][j] = False
      else:       #Right
        M[i][j] = n2
        T[i][j] = True
      # PrintMatrix(M)

  C_1 = []
  C_2 = []

  # PrintBoolMatrix(T)

  j = suma
  for i in reversed(range(1, n+1)):
    if T[i][j]:
      C_1.append(A[i - 1])
      j = abs(j + A[i - 1])
    else:
      C_2.append(A[i - 1])
      j = abs(j - A[i - 1])
  return [M[n][suma], C_1, C_2]

def minSubset(A):
  suma = 0
  for val in A:
    suma += abs(val)
  M = [ [math.inf for j in range(suma+1)] for i in range(len(A)+1)]
  n = minSubset_Memo(A, len(A), 0, 0, M)
  n2 = minSubset_BottomUp(A, len(A))
  # print(M)
  return(n, n2)

S = [1,6,11]
print(minSubset(S))
S = [1,6,11,5]
print(minSubset(S))
S = [1,-5,11]
print(minSubset(S))
S = [1, 6, 11, -2]
print(minSubset(S))
S = [10,20,15,5,25]
print(minSubset(S))
S = [1,3,5,6]
print(minSubset(S))
S = []
print(minSubset(S))
