def solution(N, A):
    counter = [0] * (N)
    maxval=0
    for a in A:
        if a < N+1:
            counter[a-1] +=1
        else:
            counter = [max(counter)]*N
            
    return counter
   

a = [3,4,4,6,1,4,4]
n = 5
   
print(solution(n,a))
