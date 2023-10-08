# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181875

# 핵심:
# 소문자화 (str.lower())
# 대문자화 (str.upper())
# 교차변환 (str.swapcase())

def solution(strArr):
    for idx in range(len(strArr)):
        if idx % 2 == 0:    # 소문자화
            strArr[idx] = strArr[idx].lower() 
        else:   # 대문자화
            strArr[idx] = strArr[idx].upper()

    answer = [strA.lower() if idx % 2 == 0 else strA.upper() for idx, strA in enumerate(strArr)]
    
    print(answer)
    return answer

solution(["AAA","BBB","CCC","DDD"])