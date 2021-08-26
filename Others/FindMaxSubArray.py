'''
Find Maximum Sub Array Algorithm
Divide & Conquer
 Sergio A. Mejía - 2020
Python script for the solution of the problem 
"Given a sequence of prices in a period of time, find the subperiod of time
where buying and selling is the best"
This problem can be rewritten as "Find the subsequence where the sum of its elements
is the largest" if this sequence is the discrete derivatives between the prices.

D&C Variant
'''

'''
Auxiliar function for the D&C variant that finds the Maximum Sub Array (maximum sum)
in an interval [l,m] crossing strictly through m
'''
def FindMaxCrossSubArray(A, l, m, h):
    vl = -float("inf")
    s = 0
    for i in reversed(range(l, m + 1)):
        s = s + A[i]
        if s > vl:
            vl = s
            ml = i
    vr = -float("inf")
    s = 0
    for i in range(m + 1, h + 1):
        s = s + A[i]
        if s > vr:
            vr = s
            mr = i
    return(ml, mr, vl + vr)

'''
Divide & Conquer Variant
    The array is recursively divided in two sections, finding the Maximum Sub Array in each one
    of them (depicted as a pair of three values (l, h, s) -> Interval[l, h] where s is the size).
    We also check for a Maximum Sub Array that is passing through this 2 sections
    using the auxiliary function. The longest length from this 3 options is returned,
    with the indexes of the interval.
''' 
def FindMaxSubArray_Aux(A, l, h):
    if h <= l:
        return (l, h, A[l])
    else:
        m = (l+h)//2
        (ll, lh, ls) = FindMaxSubArray_Aux(A, l, m)
        (rl, rh, rs) = FindMaxSubArray_Aux(A, m + 1, h)
        (cl, ch, cs) = FindMaxCrossSubArray(A, l, m, h)
        if ls > rs and ls > cs:
            return(ll, lh, ls)
        elif rs > ls and rs > cs:
            return(rl, rh, rs)
        else:
            return(cl, ch, cs)

def FindMaxSubArray(A):
    return FindMaxSubArray_Aux(A, 0, len(A) - 1)

price = [ 100, 113, 110 , 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
A = [ (price[i + 1] - price[i]) for i in range(len(price) - 1) ]
print(A)
(minD, maxD, gan) = FindMaxSubArray(A)
print("El mejor rango de días es entre el día %d y el día %d con una ganancia de %d" 
        % (minD, maxD, gan))