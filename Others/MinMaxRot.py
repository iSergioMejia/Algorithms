'''
Min and Max of Rotated Sequence Algorithm
Dynamic Programming
 Sergio A. Mejía - 2020
Python script for the solution of the problem 
"Given an ordered array that has been rotated (offseted), find the
smallest and largest number"

Recursive variants
'''


def MinMaxRot_Aux(S, b, e):
    if b >= e:
        return b
    else:
        q = (b+e)//2
        if S[b] > S[q]:
            return MinMaxRot_Aux(S,b, q)
        elif S[q] > S[e]:
            return MinMaxRot_Aux(S, q+1, e)
        else:
            return b

def MinMaxRot(S):
    r = MinMaxRot_Aux(S, 0, len(S)-1)
    s = r - 1

    if s < 0:
        s = len(S) - 1
    return (r, s)

S = [3,4,5,6,7,8,0,1,2]
(r,s) = MinMaxRot(S)
print(S[r],S[s])
