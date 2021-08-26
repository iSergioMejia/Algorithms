import random

def Partition(S, p, r):
    x = S[r]
    i = p - 1
    for j in range(p, r):
        if S[j] <= x:
            i += 1
            (S[i], S[j]) = (S[j], S[i])
    (S[i+1], S[r]) = (S[r], S[i+1])
    return (i+1)

def RandomizedPartition(S, p, r):
    random.seed(None)
    i = random.randint(p, r+1)
    (S[r], S[i]) = (S[i], S[r])
    return Partition(S, p, r)

def QuickSort_Aux(S, p, r):
    if p < r:
        q = RandomizedPartition(S, p, r)
        QuickSort_Aux(S, p, q - 1)
        QuickSort_Aux(S, q + 1, r)

def QuickSort(S):
    QuickSort_Aux(S, 0, len(S)-1)

S = [2, 5, 7, 1, 8, 10, 3]
QuickSort(S)
print(S)