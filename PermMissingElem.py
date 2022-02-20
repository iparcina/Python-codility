def solution(A):
    A.sort()
    i = 1
    B = []
    if A != []:
        
        for i in range(1,len(A)+2):
            B.append(i)
        C = set(B) - set(A)
        return  list(C)[0]
        
    else:
        return 1
    
