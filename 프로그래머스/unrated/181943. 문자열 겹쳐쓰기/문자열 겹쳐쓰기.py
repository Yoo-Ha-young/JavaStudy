# 문자열 my_string, overwrite_string과 정수 s가 주어집니다. 
def solution(my_string, overwrite_string, s):
# 문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 
# 문자열 overwrite_string으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
    answer =  my_string[0:s] + overwrite_string + my_string[s+len(overwrite_string):]

    return answer


