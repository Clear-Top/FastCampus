# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/86491

# 해결여부: O
# 해결시간: 25분

def solution(sizes):
    x = [garo[0] for garo in sizes]
    y = [sero[1] for sero in sizes]
    max_x = []
    max_y = []
    for g,s in zip(x,y):
        if (g>=s):
            max_x.append(g)
            max_y.append(s)
        else:
            max_x.append(s)
            max_y.append(g)

    return max(max_x) * max(max_y)


''' 다른 사람풀이
def solution(sizes):
    answer = max(max(size) for size in sizes * min(size) for size in sizes)
    return answer
'''