import sys
import os
path = os.getcwd() + '/SW Expert Academy/sample.txt'
sys.stdin = open(path, 'r')
input = sys.stdin.readline

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    days = int(input())
    lst = list(map(int, input().split(' ')))
    # print(days)
    # print('매매가 모음', end = ':')
    # print(*lst)
    profits = 0
    cur_sales = lst[-1]
    for day in range(days-2,-1,-1):
        ''' 메인 아이디어
        뒤에서부터 읽으면서 현재 매매가 보다 작은 매매가들의 차이값을 누적하고,
        이 행위는 현재 매매가보다 큰 매매가를 만날때까지 반복한다.
        '''
        if lst[day] > cur_sales:
            cur_sales = lst[day]
            continue
        profits += (cur_sales - lst[day])
        # print(lst[day], end=' ')
    print(f'#{test_case} {profits}')