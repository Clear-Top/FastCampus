''' 시간초과
문자열 길이가 최대 100만인데, insert 와 pop 으로 인해서 당기거나 미는 시간소요가 큼

대안1:  
대안2:  
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input().strip())

for _ in range(n):
    password_cursor = 0
    password = list()
    texts = list(input().strip())
    for text in texts:
        if 'a'<= text <='z' or 'A' <= text <= 'Z':
            password.insert(password_cursor, text)
            password_cursor+=1
        elif text == '<':
            password_cursor -= 1
            if password_cursor < 0:
                password_cursor = 0
        elif text == '>':
            password_cursor += 1
            if password_cursor > len(password):
                password_cursor = len(password)
        elif '0' <= text <= '9':   # text == '-'
            password.insert(password_cursor, text)
            password_cursor+=1
        else:
            if len(password) == 0 or password_cursor == 0:
                continue
            password.pop(password_cursor-1)
            password_cursor -= 1
    print(''.join(password))