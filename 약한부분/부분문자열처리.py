# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181842


# 핵심: 'in' 키워드로 처리

def solution(str1="abcd", str2="aabcc"):
    if str1 in str2:
        print(str1 + "은 " + str2 + "에 속해있습니다.")
    else:
        print(str1 + "은 " + str2 + "에 속해있지 않습니다.")

    answer = 0
    return answer

solution()