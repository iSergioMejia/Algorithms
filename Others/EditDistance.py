'''
Edit Distance Algorithm
Dynamic Programming
 Sergio A. Mejía - 2020
Python script for the solution of the problem 
"Given two words, what is the minimum Edit Distance (this is, amount of
additions, substractions and changes of letters) to go from one word to the other?"

Recursive, Memoized, Bottom Up (with Backtracking) variants
'''

import math

def printMatrix(M):
  for i in range(len(M)):
    for j in range(len(M[i])):
      if M[i][j] == math.inf:
        print("\t X", end='')
      else:
        print("\t",M[i][j], end='')
    print("")

'''
Recursive Variant
  Recursively try the three operations in the current letter positions and stick
  with the solution which gives the minimum moves. When one of the words has a length
  of 0 the minimum needed changes is the length of the other word. 
'''
def ED_Aux(A, B, i, j):
  if i == 0 and j == 0:
    return 0
  if i == 0 and j != 0:
    return j
  if i != 0 and j == 0:
    return i
  if A[ i - 1 ] == B[ j - 1 ]:
    return ED_Aux(A, B, i - 1, j - 1)
  else:
    insert = ED_Aux(A, B, i, j-1) + 1
    erase  = ED_Aux(A, B, i-1, j) + 1
    change = ED_Aux(A, B, i-1, j-1) + 1
    return min(insert, erase, change)

'''
Memoized Variant
  Same as recursive, but the partial solutions are stored in M, so if this
  solution has been already calculated, the value of M is returned, instead of
  calculating it again. The M matrix is |A|+1 x |B|+1 sized. 
'''
def ED_Memo(A, B, i, j, M):
  if M[i][j] == math.inf: 
    if i == 0 and j == 0:
      M[i][j] = 0
    elif i == 0 and j != 0:
      M[i][j] = j
    elif i != 0 and j == 0:
      M[i][j] = i
    else:
      if A[ i - 1 ] == B[ j - 1 ]:
        M[i][j] = ED_Memo(A, B, i - 1, j - 1, M)
      else:
        insert  = ED_Memo(A, B, i, j-1, M)   + 1
        erase   = ED_Memo(A, B, i-1, j, M)   + 1
        change  = ED_Memo(A, B, i-1, j-1, M) + 1
        M[i][j] = min(insert, erase, change)

  return M[i][j]

'''
Bottom Up (with Backtracking) Variant
  Calculate all of the possible partial solutions filling up the memoized matrix.
  Each position of M is calculated with the previously calculated values.
  A Backtrack S matrix is also initialized which consist in the instruction used to make
  the solution in the corresponding state. It will save the offset in the same matrix (dx, dy)
  and the involved letters (A[i-1], B[j-1])
'''
def ED_BottomUp(A, B, m, n, M):
  # Initialize Backtracking (BT) Matrix [dx, dy, A_i, B_j]
  S = [ [ [0, 0, None, None] for i in range(len(B) + 1)] for j in range(len(A)+1)]
  # Initalize base cases for first column for Memo matrix and BT matrix. In BT it refers to erase A_i in position 0 
  for i in range(m + 1):
    M[i][0] = i 
    S[i][0] = [-1, 0, A[i - 1], None]
  # Initalize base cases for first row for Memo matrix and BT matrix. In BT it refers to add B_j in position 0 
  for j in range(n + 1):
    M[0][j] = j
    S[0][j] = [0, -1, None, B[j - 1]]
  # Base case for [0,0], where the backtracking must end
  S[0][0] = [0, 0, None, None]
  
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      # If letters in A_i and B_j are the same, the cost will be the cost without considering them
      if A[ i - 1 ] == B[ j - 1 ]:
        M[i][j] = M[i - 1][j - 1]
        S[i][j] = [-1, -1, A[i - 1], B[j - 1]] 
      else:
        # All these changes will cost 1 plus the change from arriving to that partial state

        # Insert will be not considering one letter from B
        insert  = M[i][j-1] + 1
        # Erase will be not considering one letter from A
        erase   = M[i-1][j] + 1
        # Change will be not considering one letter from both A and B
        change  = M[i-1][j-1] + 1

        if insert < erase and insert < change:
          # If Insert is the best option, save the cost for Insertion and in BT put that the solution will be insert [0, -1] the letter B_j
          M[i][j] = insert
          S[i][j] = [0, -1, None, B[j - 1]] 
        elif erase < insert and erase < change:
          # If Erase is the best option, save the cost for Erase and in BT put that the solution will be erase [-1, 0] the letter A_j
          S[i][j] = [-1, 0, A[i - 1], None] 
          M[i][j] = erase
        else:
          # If Change is the best option, save the cost for Change and in BT put that the solution will be change [-1, -1] the letter A_j to B_j     
          S[i][j] = [-1, -1, A[i - 1], B[j - 1]] 
          M[i][j] = change
  
  # printMatrix(S)

  '''
  Initialize vector of instructions. Instructions will be written in the form [type, position, letter[, letterChange]].
    - type is 0 for change, 1 for erase and 2 for insert
    - position is the index starting from 1 of the original string (an offset that changes in each Erase and Insert instruction must be used if these instructions are going to be used programatically)
    - letter is the letter that will be used in the instruction. If letterChange is present, it means that the instruction is a Change from letter to letterChange.'''
  T = []
  x, y = m, n
  # Backtracking starts in the bottom right corner of the BT matrix
  dx, dy = S[x][y][0], S[x][y][1]
  # While there's an instruction to move, move to that new position
  while (x != 0 or y != 0) and (dx != 0 or dy!= 0):
    dx, dy = S[x][y][0], S[x][y][1]
    lA, lB = S[x][y][2], S[x][y][3]
    # Instruction is a Change or a do nothing?
    if dx == -1 and dy == -1:
      #Instruction is a Change?
      if lA != lB:
        #If so, build instruction accordingly
        T.append([0,y,lA,lB])
    # Instruction is an Erase?
    elif dx == -1:
      T.append([1,x,lA])
    #If not, Instruction is an Insert
    else:
      T.append([2,y,lB])
    # Move throught the BT matrix accordingly
    x = dx + x
    y = dy + y
  # Reverse the order from the instructions to be consistent
  T.reverse()
  return [M[m][n], T ]

def ED(A, B):
  # Initialize Memo matrix with +infinity because is a minimum optimization
  M = [ [ math.inf for i in range(len(B) + 1) ] for j in range(len(A) + 1) ]
  n3 = ED_BottomUp(A, B, len(A), len(B), M)
  return( n3 )

'''
Transforms a string A using a set of instructions T. The instructions come as explained in the ED_BottomUp function.
'''
def Transform(A, T):
  B = A
  # An offset is needed to account for changes in the indexes after insertions and erasings.
  offset = 0
  for instruction in T:
    print(B)
    printInstructions(instruction)
    _type = instruction[0]
    # pos comes like an index starting from 1, so 1 must be substractes
    _pos = instruction[1] - 1
    if _type == 0: # Change
      _letter = instruction[3]
      B = B[:_pos] + _letter + B[(_pos + 1):]
    elif _type == 1: # Erase
      _pos = _pos + offset
      _letter = instruction[2]
      B = B[:_pos] + B[(_pos + 1):]
      # Substract from the offset because B is now one letter less in size
      offset -= 1
    else: # Insertion
      _letter = instruction[2]
      B = B[:_pos] + _letter + B[_pos:]
      # Add to the offset because B is now one letter more in size
      offset += 1
  print(B)  
  return B

''' 
Prints an instruction in a human readable way
'''
def printInstructions( instruction ):
  _type = instruction[0]
  _pos = instruction[1]
  if _type == 0: #intercambio
    print("Intercambiar la letra '%s' por '%s' en la posición %d"%(instruction[2],instruction[3],_pos))
  elif _type == 1: #erase
    print("Eliminar la letra '%s' en la posición %d"%(instruction[2],_pos))
  else:
    print("Agregar la letra '%s' en la posición %d"%(instruction[2], _pos))

A = "anita lava la tina"
B = "tres tristes tigres comian trigo en un trigal"
print("Origen: '%s' - Destino: '%s'"%(A, B))
res = ED(A, B)
print(res[1])
print("Cantidad de cambios:",res[0])
# printInstructions(res[1])
print("Expected:",B,"- Result:",Transform(A, res[1]))