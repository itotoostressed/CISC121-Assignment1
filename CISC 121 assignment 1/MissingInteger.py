a = [1, 2, 3, 5] #the example array we have. 
b = [1, 2, 3]
c = [-3, -1]
def missingInt(A):
    count = 0
    A.sort()
    for n in range (len(A)):
        if A[n] == count + 1:
            count += 1 #keeps a record of the integers we've encountered. 
            continue
        elif A[n] == count: #to check if the current index is equal to the last number we've encountered (duplicates) 
            continue
        elif A[n] > count + 1:
            print(count + 1) 
            return count + 1
    print(count + 1)
    return count + 1
missingInt(a)
missingInt(b)
missingInt(c)