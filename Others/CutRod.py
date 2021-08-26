'''
Activity Selection Algorithm
Dynamic Programming
 Leonardo Florez - 2020
Python script for the solution of the problem 
"Given a rod of a given length and a table of earnings for pieces of different lengths,
how you can cut the rod in order to earn the greatest amount?"

Recursive (Naive), Memoized, Bottom Up (with Backtracking) variants
'''

import math, random

'''
Naive variant
  Try to cut all of the possible lengths and recursively calculate the earning of
  the remaining piece. Return the minimum of all of these possibilites.
''' 
## -------------------------------------------------------------------------
def CutRod_Naive( P, n ):
  if n == 0:
    return 0
  else:
    q = -math.inf
    for k in range( 1, n + 1 ):
      v = P[ k - 1 ] + CutRod_Naive( P, n - k )
      if q < v:
        q = v
      # end if
    # end for
    return q
  # end if
# end def

'''
Memoized Variant
  Same as recursive, but the partial solutions are stored in M, so if this
  solution has been already calculated, the value of M is returned, instead of
  calculating it again.
'''
## -------------------------------------------------------------------------
def CutRod_Memoized_Aux( P, n, r ):
  if r[ n ] == -math.inf:
    if n == 0:
      r[ n ] = 0
    else:
      q = -math.inf
      for k in range( 1, n + 1 ):
        v = P[ k - 1 ] + CutRod_Memoized_Aux( P, n - k, r )
        if q < v:
          q = v
        # end if
      # end for
      r[ n ] = q
    # end if
  # end if
  return r[ n ]
# end def

'''
Interface function for the memoized function
'''
## -------------------------------------------------------------------------
def CutRod_Memoized( P, n ):
  r = [ -math.inf for i in range( n + 1 ) ]
  return CutRod_Memoized_Aux( P, n, r )
# end def

'''
Bottom Up version
  Calculate all of the possible partial solutions, filling up all the positions of M.
''' 
## -------------------------------------------------------------------------
def CutRod_BottomUp( P, n ):
  r = [ -math.inf for i in range( n + 1 ) ]
  r[ 0 ] = 0
  for i in range( 1, n + 1 ):
    for k in range( 1, i + 1 ):
      v = P[ k - 1 ] + r[ i - k ]
      if r[ i ] < v:
        r[ i ] = v
      # end if
    # end for
  # end for
  return r[ n ]
# end def

'''
Bottom Up (Backtracking) version
  For each possible solution that is calculated, in another vector we save the
  length for which the greatest earning is achieved. Then we make backtracking 
  using this vector, cutting the rod accordingly.
'''
## -------------------------------------------------------------------------
def CutRod_Backtracking( P, n ):
  r = [ -math.inf for i in range( n + 1 ) ]
  s = [ -1 for i in range( n + 1 ) ]
  r[ 0 ] = 0
  for i in range( 1, n + 1 ):
    for k in range( 1, i + 1 ):
      v = P[ k - 1 ] + r[ i - k ]
      if r[ i ] < v:
        r[ i ] = v
        s[ i ] = k
      # end if
    # end for
  # end for

  # Backtracking
  T = []
  m = n
  while m > 0:
    T.append( s[ m ] )
    m = m - s[ m ]
  # end while

  return [ r[ n ], T ]
# end def

## -------------------------------------------------------------------------

P = [ 1, 5, 8, 9 ]
# P = [ 1, 1, 8, 9, 10, 17, 1, 15, 11, 16 ]
# P = [ random.uniform( 1, 10 ) for i in range( 25 ) ]

r_Naive = CutRod_Naive( P, len( P ) )
print( "Naive       :", r_Naive )

r_Memoized = CutRod_Memoized( P, len( P ) )
print( "Memoized    :", r_Memoized )

r_BottomUp = CutRod_BottomUp( P, len( P ) )
print( "BottomUp    :", r_BottomUp )

r_Backtracking = CutRod_Backtracking( P, len( P ) )
print( "Backtracking:", r_Backtracking )

## eof - cutrod.py