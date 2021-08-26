def BinSearch_Aux(S, v, b, e):
    if e < b:
        return -1
    else:
        q = (b+e)//2
        if v < S[q]:
            return BinSearch_Aux(S, v, b, q-1)
        if S[q] < v:
            return BinSearch_Aux(S, v, q+1, e)
        else:
            return q

def BinSearch(S, v):
    return BinSearch_Aux(S, v, 0, len(S))

S = [0, 1, 1.5, 3, 4, 5, 6, 7]
v = 2
print(BinSearch(S,v))
    