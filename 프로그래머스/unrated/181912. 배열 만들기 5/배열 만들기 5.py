def solution(intStrs, k, s, l):
    answer = []
    
    for ints in intStrs:
        if int(ints[s:l+s]) > k:
            answer.append(int(ints[s:l+s]))
    # intStrs의 각 원소마다 s번 인덱스에서 시작하는 길이
    # l짜리 부분 문자열을 잘라내 정수로 변환합니다. 
    # 이때 변환한 정수값이 k보다 큰 값들을 담은 배열을 
    # return 하는 solution 함수를 완성해 주세요.


    return answer