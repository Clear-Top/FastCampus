### 람다 함수
# 리스트 모든 원소에 1씩 더하기 위한 람다

lst = list(range(1,6))
print(lst)

lst2 = list(map(lambda x:x+1, lst))
print(lst2)