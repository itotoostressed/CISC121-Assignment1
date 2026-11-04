a = [0, 1, 0, 1]
def passingCars(A):
    counter0 = 0
    totalpairs = 0
    for n in range (len(A)):
        if A[n] == 0:
            counter0 += 1
        elif A[n] == 1: 
            totalpairs += counter0
    print (totalpairs)
passingCars(a)