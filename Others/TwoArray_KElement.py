'''
Two Array K-Element Algorithm
Dynamic Programming
 Sergio A. Mejía - 2020
Python script for the solution of the problem 
"Given two ordered sequences of numbers, calculate the nth smallest number
among both sequences"

Recursive variant

NOT WORKING
'''

def KElem_Aux(A, B, k, a, b, c , d):
    if a >= b and c <= d:
        return B[k]
    elif a <= b and c >= d:
        return A[k]
    else:
        f = (b - a)//2
        g = (d - c)//2
        #s = (f-a+1)+(g-c+1)-1
        s = f + g
        if s < k:
            if A[f] > B[g]:
                return KElem_Aux(A, B, k - g - 1, a, b, c + g + 1, d)
            else:
                return KElem_Aux(A, B, k - f - 1, a + f + 1, b, c, d)
        else:
            if A[f] > B[g]:
                return KElem_Aux(A, B, k, a, b + f, c, d)
            else:
                return KElem_Aux(A, B, k, a, b, c, d + g)

def KElem(A, B, k):
    return KElem_Aux(A, B, k, 0, len(A)-1, 0, len(B)-1)

A = [1, 2, 3]
B = [4, 5, 6]
k = 3
print(KElem(A, B, k - 1))
