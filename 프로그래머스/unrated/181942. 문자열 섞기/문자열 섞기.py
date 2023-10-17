def solution(str1, str2):
    answer = ''
    
    for i in range(len(str1)):
        answer+=str1[i]
        answer+=str2[i]

        # if i % 2 == 0:
        #     answer += str1.split()[i]
        # else:
        #     answer += str2.split()[i]

    return answer