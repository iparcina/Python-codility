# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A,B,K):
    counter =0
    a = B -A 
    if A != B and A != 0 and B != 0 and K == 2 :
        if a != K:
            return a//2 +1
        else:
            return a//2 
    if A ==0 and B ==K and A !=B:
        return 2
    if  A == B == K:
        return 1
    if B < K and B !=0:
        return 0
    if (B > A or B ==A):
        if A==0 :
            if K ==1:
                return B +1
            elif K == 2:
                return (B//2)+1
            else:
                return 1
        elif A ==1 :
            if K ==1:
                return B
            elif K ==2:
                return B//2
        else:
            if A == B:
                if A%K == 0:
                    return 1
                else:
                    return 0
    
            else:
                temp = A
                for i in range(0,K):
                    if temp%K != 0:
                        temp += 1
                for i in range(temp, B+1,K):
                    counter+=1
                return counter
    else:
        return 0
