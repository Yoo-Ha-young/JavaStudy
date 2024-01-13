def solution(n):
    answer = 0
    
    # n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return
    if n % 2 == 1:
        answer += sum(range(1, n+1, 2))
    else:
        # n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return
        for i in range(2, n+1, 2):
            answer += i ** 2

    return answer
