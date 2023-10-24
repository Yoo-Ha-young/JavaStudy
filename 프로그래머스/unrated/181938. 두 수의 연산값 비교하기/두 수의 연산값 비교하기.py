def solution(a, b):
    A = str(a)
    B = str(b)
    ab = A+B
    intAB = int(ab)
    AB2 = 2 * a * b
    
    if intAB > AB2:
        return intAB
    elif AB2 > intAB:
        return AB2
    elif AB2 == intAB:
        return intAB
