'''
  PrintMatrix and MatrixMult_Aux made by Leonardo Florez
  BottomUp and Backtrack code made by Sergio A. Mejía
   for the Algorithmic Analysis class 20-30
  Python script for the solution of the problem 
  "Given some matrices dimensions, calculate the order of multiplication
  with the less amount of calculations"

  Recursive Memoized, Bottom Up (with Backtracking) and Greedy variants
'''

import math

def PrintMatrix( M ):
  for j in range( len( M ) ):
    for i in range( len( M ) ):
      if M[ i ][ j ] == math.inf:
        print( ".", end = "" )
      else:
        print( "x", end = "" )
    # end for
    print( "" )
  # end for
  print( "---------------------" )
# end def

def MatrixMult_Aux( D, i, j, M ):
  if M[ i ][ j ] == math.inf:
    if i == j:
      M[ i ][ j ] = 0
      # PrintMatrix( M )
    else:
      q = math.inf
      for k in range( i, j ):
        left = MatrixMult_Aux( D, i, k, M )
        right = MatrixMult_Aux( D, k + 1, j, M )
        m = left + right + ( D[ i - 1 ] * D[ k ] * D[ j ] )
        if m < q:
          q = m
        # end if
      # end for
      M[ i ][ j ] = q
      # PrintMatrix( M )
    # end if
  # end if
  return M[ i ][ j ]
# end def

def Backtrack(S, M, i, j):
  if i == j or S[i][j] == -1:
    return "A"+str(i)
  T = []
  T.append(Backtrack(S, M, i, S[i][j] ))
  T.append(Backtrack(S, M, S[i][j]+1, j))
  return T

def MatrixMult_BottomUp( D, M ):
  S = [ [ -1 for i in range( len( D ) ) ] for j in range( len( D ) )  ]
  for i in range(1, len(D)):
    M[i][i] = 0
  i = 0
  j = 0
  n = len(D)
  for i in reversed(range(1, n-1)):
    for j in range(i + 1, n ):
      q = math.inf
      for k in range( i, j ):
        left = M[i][k]
        right = M[k + 1][j]
        x = i
        m = left + right + ( D[ i - 1 ] * D[ k ] * D[ j ] )
        if m < q:
          q = m
          x = k
        # end if
      # end for
      M[ i ][ j ] = q
      S[ i ][ j ] = x
      # PrintMatrix( M )
  T = Backtrack(S, M, 1, len(D)-1)

  return (M[ i ][ j ], T)
# end def



def MatrixMult( D ):
  M = [ [ math.inf for i in range( len( D ) ) ] for j in range( len( D ) )  ]
  val =  MatrixMult_Aux( D, 1, len( D ) - 1, M )
  val2, bk = MatrixMult_BottomUp(D, M)
  print("Res from Memoization = ", val) 
  print("Res from Bottom Up = ", val2)
  eq = str(bk)
  eq = eq.replace("[","(")
  eq = eq.replace("]",")")
  eq = eq.replace("'","")
  eq = eq.replace(" ","")
  eq = eq.replace(",","*")
  print("Así debe multiplicar: "+eq)
  print("")
# end def

# D : [10x100],[100x5],[5x50]
D = [ 10, 100, 5, 50]
D1 = [ 10, 100, 5, 50, 3, 2, 10, 125, 35, 246 ]
D2 = [40, 20, 30, 20, 30]
D3 = [10, 20, 30, 40, 30]
MatrixMult( D )
MatrixMult( D1 )
MatrixMult( D2 )
MatrixMult( D3 )


