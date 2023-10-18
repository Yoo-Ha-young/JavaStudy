def solution(a, b):
    
    a = str(a)
    b = str(b)
    A = int(a+b)
    B = int(b+a)

    if A >= B:
        return A
    elif B >= A:
        return B