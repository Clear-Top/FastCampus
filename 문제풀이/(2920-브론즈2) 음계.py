''' 문제설명
다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.

1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.

연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.
'''

''' 제약사항
1초, 128MB
'''

''' 입출력 설명
입력: 첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.

출력: 첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

numbers = list(map(int, input().split()))

check_for_asc = True
check_for_desc = True
check_for_mix = False

for i in range(1, len(numbers)):
    if numbers[i]-numbers[i-1] == 1:
        check_for_desc = False
    elif numbers[i]-numbers[i-1] == -1:
        check_for_asc = False
    else:
        check_for_mix = True
        break

if check_for_mix:
    print('mixed')
elif check_for_asc:
    print('ascending')
elif check_for_desc:
    print('descending')
