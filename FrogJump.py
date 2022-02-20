def solution(X, Y, D):
    # write your code in Python 3.6
    if (X == Y or X>Y):
        return 0
    a = Y - X
    if a%D == 0 :
        a = a//D
        return 
    else:
        a = (a//D)+1
        return a

    
