''' 문제 설명
문자열 S가 주어졌을 때, SHA-256 해시값을 구하는 프로그램을 작성하시오.
'''
''' 입출력 설명
[ 입력 ]
첫째 줄에 문자열 S가 주어진다. S는 알파벳 대문자와 소문자, 그리고 숫자로만 이루어져 있으며, 길이는 최대 50이다.

[ 출력 ]
첫째 줄에 S의 SHA-256 해시값을 출력한다.
'''
import hashlib
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

string = input().strip()

# 바이트로 암호화
string_encode = string.encode()

# sha256 암호화 (256bit 로 암호화)
result = hashlib.sha256(string_encode)

print(result.hexdigest())

