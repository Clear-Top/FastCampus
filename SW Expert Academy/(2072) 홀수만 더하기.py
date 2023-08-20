# 링크
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq

import sys
import os

# 테스트케이스 텍스트파일 위치설정
path = os.getcwd() + '/SW Expert Academy/' + 'input.txt'

# 표준입력을 파일로 설정
sys.stdin = open(path, "r")
input = sys.stdin.readline

number_of_cases = int(input())

for testcase in range(number_of_cases):
    lst = list(map(int, input().split(' ')))
    sum = 0
    for data in lst:
        if data % 2 == 0:
            continue
        sum += data
    print(f'#{testcase+1} {sum}')


