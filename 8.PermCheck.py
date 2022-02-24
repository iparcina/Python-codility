def solution(A):
    myset = set([i for i in range(1,len(A)+1)])
    A = set(sorted(A))
    if A == myset:
        return 1
    return 0


