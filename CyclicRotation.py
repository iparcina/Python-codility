def solution(A, K):
    if len(A)>0:
        for i in range(0,K):
            A.insert(0,A[-1])
            A.pop(-1)
    return(A)
