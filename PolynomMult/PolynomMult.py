'''
Polynomial Multiplication Algorithm
Dynamic Programming
 Sergio A. Mejía - 2020
Python script for the solution of the problem 
"Given two polyonomials, calculate result of the multiplication 
of the two of them"

Iterative and Recursive variants
'''

def InnocentMult(A, B):
    n_1 = len(A)
    n_2 = len(B)
    R = [0]*(n_1 + n_2 - 1)
    for expA, coefA in enumerate(A, 0):
        for expB, coefB in enumerate(B, 0):
            R[expA + expB] += coefA*coefB
    return R

def mult(A, B, R, i):
    for j in range(len(B)):
        R[j + i] += A[i]*B[j]

def PolyMult_Aux(A, B, R, b, e):
    if b >= e:
        mult(A, B, R, b)
    else:
        q = (b + e)//2
        PolyMult_Aux(A, B, R, b, q)
        PolyMult_Aux(A, B, R, q + 1, e)

def PolyMult(A, B):
    R = [0]*(len(A) + len(B) - 1)
    if len(A) > len(B):
        PolyMult_Aux(A, B, R, 0, len(A) - 1)
        return R
    else:
        PolyMult_Aux(B, A, R, 0, len(B) - 1)
        return R

import time

tries = 3000
i = 0
while i < tries:
    A = [1]*i
    B = [1]*i
    tIS = time.process_time()
    InnocentMult(A, B)
    tI = time.process_time() - tIS
    tDS = time.process_time()
    PolyMult(A, B)
    tD = time.process_time() - tDS
    print(i, tI, tD)
    i += 100

print(InnocentMult(A, B))
print(PolyMult(A, B))
