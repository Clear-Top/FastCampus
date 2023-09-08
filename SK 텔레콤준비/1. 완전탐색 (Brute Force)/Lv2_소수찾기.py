# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42839

# 해결여부: O (시간초과 => '에라토스테네스의 체'로 해결)
# 해결시간: 30분초과

'''
종이조각은 7개니까 itertools의 permutations 가능할 듯?
순열은 O(n!) 이기 때문에 n<=10 이면 가능함
'''

from itertools import permutations

def eratos(number): 
    ''' (에라토스테네스의 체)
    # O(nlog(longn)) = O(n) 만큼의 성능
    # 소수가 아닌것들의 배수들은 검토할 필요가 없다. 
        => 수 A가 주어졌을 떄, sqrt(A) 까지만 돌면서 나눠지는지 확인한다.
    '''
    for i in range(2, int(number**(0.5)) + 1):
        if number % i == 0:
            return 0
    return 1

def solution(numbers):
    # count = 0
    answer = 0
    lists = list()
    for i in range(1, len(numbers) + 1):
        lists += list(map(int, map("".join, permutations(numbers, i))))
    # count += find_prim(set(lists))

    p = set(lists)
    for lst in p:
        if lst < 2:
            continue
        val = eratos(lst)
        if val:
            print(f"{lst}는 소수입니다.")
            answer += val
    return answer


# print(solution('17'))
print(solution("011"))