# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42839

# 해결여부: 
# 해결시간: 

'''
한 자릿수 종이조각 이어붙여서 소수를 몇개 만들수 있는지 => eval()

종이조각은 7개니까 combination 가능할 듯?
'''

from itertools import permutations

def find_prim(str_lists):
    result = 0
    sets = set()
    for str_list in str_lists:
        number = int(''.join(str_list))
        if number == 0 or number == 1:
            continue
        print(f"{number} 추가")
        sets.add(number)
    print(sets)
    for x in sets:
        flag = True
        for i in range(2, x//2+1):
            if x % i == 0:
                flag = False
        if flag:
            result += 1
        print(f"소수: {x} => count: {result}")
    return result

def solution(numbers):
    # numbers : string

    count = 0
    lists = []
    for i in range(1, len(numbers) + 1):
        lists += list(permutations(numbers, i))
    count += find_prim(lists)
    return count


# print(solution('17'))
print(solution("011"))

# 조합한걸 하나의 set에 넣어서 중복을 없애야 함