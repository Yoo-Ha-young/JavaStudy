def solution(s):
    answer=True
    a=0
    for k in s:
        if k =='(':
            a += 1
        else:
            a -= 1
        if a == -1:
            answer = False
    if a > 0:
        answer = False
    return answer