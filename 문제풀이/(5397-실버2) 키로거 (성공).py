''' 시간초과
문자열 길이가 최대 100만인데, insert 와 pop 으로 인해서 당기거나 미는 시간소요가 큼

대안: 커서를 기준으로 왼쪽과 오른쪽 스택을 사용
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input().strip())

for _ in range(n):
    texts = list(input().strip())

    # 핵심 (두개의 스택사용)
    left = []
    right = []

    for text in texts:
        if text == '>':
            # '>' 입력되었을 때
            if not right:
                continue
            left.append(right.pop())
        elif text == '<':
            # '<' 입력되었을 때
            if not left:
                continue
            right.append(left.pop())
        elif text == '-':
            # '-' 입력되었을 때
            if left:
                left.pop()
        else:
            # 문자나 숫자가 입력되었을 때
            left.append(text)
    right.reverse()
    print(''.join(left + right))
    # print(left.extend(right))


    
    