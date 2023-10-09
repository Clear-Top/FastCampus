import sys
input = sys.stdin.readline
N, K = map(int, input().strip().split())

def find_yak(N):
    result = [1,N]
    for i in range(2, int(N**0.5)+1):
        if N % i == 0 and i not in result:
            result.append(i)
            result.append(int(N/i))
    return result

result = find_yak(N)
if len(result) < K:
    print(-1)
else:
    result.sort()
    print(result)
    print(result[K-1])