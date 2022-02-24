def solution(A):
    counter = 0
    for j, a in enumerate(A):
        if a == 0:
            for i in range(j+1,len(A)):
                if A[i] == 1:
                    counter +=1
                    if counter>1000000000:
                        return -1
    return counter

a = [0,1,0,1,1]
print(solution(a))
