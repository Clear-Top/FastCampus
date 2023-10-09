import time
### 함수만들기

MAX = 10**6

def isPrime(num):
    for i in range(2, num):
        if num%i==0:
            return None
    return num

def isPrime_improve(num):
    for i in range(2, int(num**0.5)+1): # 에라토스테네스의 체
        if num%i==0:
            return None
    return num

lst = [num for num in range(1, MAX)]    # 답: [False, True, True, False, True]
answer = []
start = time.process_time()
for num in lst:
    result = isPrime_improve(num)
    if result != None:
        answer.append(result)
end = time.process_time()
print(f'에라토스테네스의 체: {end-start:.3f} sec')
# print(len(answer))
# 약 0.1초


answer = []
start = time.process_time()
for num in lst:
    result = isPrime(num)
    if result != None:
        answer.append(result)
end = time.process_time()
print(f'일반적인 방식: {end-start:.3f} sec')
# print(len(answer))
# 약 20초
        