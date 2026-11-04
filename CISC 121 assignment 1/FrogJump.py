X = 3
A = [1, 2, 1, 3, 1, 3]
def CheckLeaf(X, A):
    B = []
    n = len(A)
    for j in range (n):
        if A[j] in B: # membership check to see if the current value is already in B. 
            continue
        B.append(A[j])
        if len(B) == X:
            print("Frog can jump!")
            return j
    return -1