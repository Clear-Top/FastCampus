import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
stack = list()

list_target = [int(input()) for _ in range(n)]
list_symbol = list()

push_number = 1
flag = True

for target in list_target:
    if len(stack) != 0:
        if stack[-1] == target:
            stack.pop()
            list_symbol.append('-')
        elif stack[-1] < target:
            # push
            while stack[-1] != target:
                stack.append(push_number)
                list_symbol.append('+')
                push_number += 1
            stack.pop()
            list_symbol.append('-')
        else:
            print("NO")
            flag = False
            break
    else:
        # push
        while push_number <= target:
            stack.append(push_number)
            list_symbol.append('+')
            push_number += 1
        stack.pop()
        list_symbol.append('-')

if flag:
    for symbol in list_symbol:
        print(symbol)

''' push 조건
= stack 이 비었거나, stack 의 top 원소가 target 보다 작다면 !
    => target 과 같아 질때까지 push 하기
'''

''' No 출력조건
= pop 할 때 stack 의 top 이 target 보다 클 때 !
'''