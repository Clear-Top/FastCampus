# 브라운개수    = (yellow1+2) X (yellow2+2) - (노랑약수1Xyellow2)
# 노량약수1 과 yellow2 를 모두 탐색해서 위 수식을 만족하는 경우 찾기
# 노랑격자수가 2백만 이므로, O(nlogn) 안에 해결해야 함...?

def cal_brown(brown, yellow1, yellow2):
    estimate_brown = (yellow1+2) * (yellow2+2) - (yellow1*yellow2)
    if brown == estimate_brown:
        return True
    return False

def solution(brown, yellow):
    answer = [] # [0]가로, [1]세로

    # 약수가 될 수 없는거 빨리거르기 (에라토스테네스의 체)
    for yellow1 in range(1, int(yellow**(0.5))+1):
        if yellow % yellow1 == 0:
            yellow2 = yellow // yellow1
            if cal_brown(brown, yellow1, yellow2):
                if yellow1<yellow2:
                    yellow1, yellow2 = yellow2, yellow1
                answer.append(yellow1+2)
                answer.append(yellow2+2)
                break    
                # 뒤에서부터 찾았어야 했는데...
    return answer


print(solution(10, 2))
# print(solution(8, 1))
# print(solution(24, 24))