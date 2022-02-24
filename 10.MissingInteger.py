def solution(A):
    B = [x for x in A if x > 0]
    if len(B) == 0:
        return 1
    else:
        New = [i for i in range(1,max(A)+2)]
        a =list(set(New)-set(A))
        return min(a)

a = [1,3,6,4,1,2]
print(solution(a))
        
