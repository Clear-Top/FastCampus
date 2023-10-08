# 첫단어를 대문자화 하는 메소드: capitalize

def solution(s):
    answer = ''

    arr = list(map(lambda x:x.capitalize(), s.split()))
    # print(*arr)
    
    answer += " ".join(arr)
    
    return answer

print(solution("for the last      week"))