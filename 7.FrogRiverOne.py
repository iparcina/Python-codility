def solution(X,A):
    steps = set([i for i in range(1,X+1)]) #create set of steps 1,2,...X
    fs = set() 
    for i,a in enumerate(A):
        fs.add(a) #one by one, add element from A to set fs
        if fs==steps:
            return i #we are finding a position where position
        #of number X is such that before that position, we have all elements 1,2,3,..X
    return -1

