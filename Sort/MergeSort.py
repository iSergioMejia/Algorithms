def Merge_Aux(A, b, q, e):
    print("(", b, ", ", q, ", ", e, ")")
    n_1 = q - b + 1
    n_2 = e - q
    L = [None]*(n_1 + 1)
    R = [None]*(n_2 + 1)
    for i in range(n_1):
        L[i] = A[b + i]
    for i in range(n_2):
        R[i] = A[q + i + 1]
    L[n_1] = float('inf')
    R[n_2] = float('inf')
    print(L, R)
    i = 0
    j = 0
    for k in range(b, e + 1):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def MergeSort_Aux(A, b, e):
    if b < e:
        q = (b + e)//2
        MergeSort_Aux(A, b, q)
        MergeSort_Aux(A, q + 1, e)
        Merge_Aux(A, b, q, e)

def MergeSort(A):
    MergeSort_Aux(A, 0, len(A) - 1)

A = [2, 5, 3, 9, 10, 1]
MergeSort(A)
print(A)