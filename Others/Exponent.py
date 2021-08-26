'''
Exponent Algorithm
Divide & Conquer
 Sergio A. Mejía - 2020
Python script for the solution of the problem 
"Calculate a^b in a complexity no bigger than O(log n)"
'''

'''
Divide into two the required multiplications
    If b is even, i.e. a^4 = a*a*a*a, it can be rewritten as (a*a)*(a*a) where both
    operands are the same, so one of them can be found recursively and multiply it by itself.
    If b is odd, i.e. a^5 = a*a*a*a*a, it can be rewritten as (a*a)*(a*a)*a where two of the operands
    are the same, so one of them can be found recursively and multiply it by it self and then
    multiply it by one a.
'''
def pow(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        r = pow(a, b//2)
        return r*r
    else:
        r = pow(a,(b-1)//2)
        return r*r*a
    
print(pow(4,3))