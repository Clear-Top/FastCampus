'''
N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를 오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.
'''

import sys
input = sys.stdin.readline

T = int(input().strip())
# print('테스트케이스 개수 =',T)
for idx, _ in enumerate(range(T)):
    N, s, e, k = map(int, input().strip().split())
    lst = list(map(int, input().split()))
    # print(N, s, e, k)
    # print(*lst)

    result = sorted(lst[s-1:e])
    
    print(f'#{idx+1} {result[k-1]}')



