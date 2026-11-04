a = [4, 1, 3, 2]
b = [1, 2, 1, 4]
def PermCheck(A):
    n = len(A) # the number of elements within a. 
    A.sort()  # Sort the array to check for permutation
    for i in range(n):
        if i + 1 != A[i]:# Check if the current element is equal to the array's element. Also checks for double ints.  
            print("I'm not a permutation!") #debug
            return 0 # Exits the function and returns 0 if not a perm
    print("I'm a permutation!") #debug
    return 1 # is a permutation.

PermCheck(a)
PermCheck(b)