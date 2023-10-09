import random as r

def listBreaking():
    print('\n'*2)

# 0. 리스트 초기화하는 법
lst1 = []
lst2 = list()


listBreaking()
# 1. range 를 활용해서 리스트 초기화하기
lst = list(range(1,11))
print(lst)


listBreaking()
# 2. 두 리스트 파일 붙이기 ('+')
lst1 = [1,2,3]
lst2 = list(range(1,5))
print(lst1 + lst2)


listBreaking()
# 3. 리스트에 원소삽입하기
# 1) append 사용 (마지막에 원소추가)
lst = []
lst.append(1)
lst.append(2)
lst.append(3)
print(lst)

# 2) insert 사용 (index 지정해서 원소 추가하기, 원소를 한 칸씩 밀어야해서 시간 Bad)
lst.insert(0, 10)
print(lst)


listBreaking()
# 4. 리스트에서 원소제거하기
# 1) pop 사용 (마지막 혹은 원하는 index의 원소 삭제)
lst = [1,2,3,4,5]
value = lst.pop()
print(f'삭제후 lst: {lst}\n삭제한 값: {value}')
value = lst.pop(1)
print(f'삭제후 lst: {lst}\n삭제한 값: {value}')

# 2) remove 사용 (원하는 값 삭제)
lst = [1,2,3,4,5,1]
value = lst.remove(1)   # remove는 삭제한 값을 return 하지 않는다..
# lst.remove(1)
print(f'삭제후 lst: {lst}\n삭제한 값: {value}')


listBreaking()
# 5. 리스트에서 특정 원소의 index 찾기 (index())
# ** 문자열에서는 find를 사용하고, 리스트에서는 index를 사용한다
lst = [1,2,3,4,5,1]
idx = lst.index(5)


listBreaking()
# 6. 리스트의 모든 원소값의 합구하기 (sum)
lst = list(range(1, 11))
print(lst)
print(sum(lst))


listBreaking()
# 7. 리스트의 원소중 최대/최소 값구하기 (max/min)
lst = list(range(1,11))
print('최댓값:',max(lst))
print('최솟값:',min(lst))


listBreaking()
# 8. random 모듈을 사용해서 리스트 shuffle 하기
lst = list(range(1,11))
print('Shuffle 전:',lst)
r.shuffle(lst)
print('Shuffle 후:',lst)


listBreaking()
# 9. 원소 정렬하기 (sort, sorted)
# 1) 리스트 내장함수 .sort() 사용하기 (원본자체를 정렬)
lst = list(range(1,11))
r.shuffle(lst)
print('원본리스트: {list}'.format(list=lst))
lst.sort()
print('오름차순 정렬후 원본리스트: {list}'.format(list=lst))
lst.sort(reverse=True)
print('내림차순 정렬후 원본리스트: {list}'.format(list=lst))

# 2) 파이썬 내장함수 sort() 사용하기 (정렬된 사본 생성)
lst = list(range(1,11))
r.shuffle(lst)
print('원본리스트: {list}'.format(list=lst))
copied_lst = sorted(lst)
print('오름차순 정렬후 원본리스트: {list}'.format(list=lst))
print('오름차순 정렬된 사본리스트: {list}'.format(list=copied_lst))
copied_lst = sorted(lst, reverse=True)
print('내림차순 정렬후 원본리스트: {list}'.format(list=lst))
print('내림차순 정렬된 사본리스트: {list}'.format(list=copied_lst))


listBreaking()
# 10. 특정 범위 원소제거하기 (del)
lst = list(range(1,11))
print('원본리스트:',lst)
del lst[:5] # index 0~4 까지 삭제
print('삭제후리스트:',lst)


listBreaking()
# 11. 리스트의 모든 원소 제거하기 (clear(), del[:])
lst = list(range(1,11))
print('원본리스트:',lst)
lst.clear()
print('clear() 삭제후리스트:',lst)

lst = list(range(1,11))
print('원본리스트:',lst)
del lst[:]
print('del [:] 삭제후리스트:',lst)
'''
주의: "del lst" 는 lst 변수 자체를 메모리에서 지워버림. 즉, 빈 리스트랑 다름. 아예 없는거...
'''


listBreaking()
# 12. 리스트 슬라이싱 (특정 범위만큼의 원소를 가져와서 새로운 리스트를 생성)
lst = [23,12,36,53,19]
sliced_lst = lst[:3]
print('슬라이싱 완료!')
print(f"원본리스트 {lst}, 주소값: {id(lst)}") 
print(f"슬라이싱된 리스트 {sliced_lst}, 주소값: {id(sliced_lst)}")  


listBreaking()
# 13. 원소개수 세기 (len)
lst = list(range(1,11))
print('원소의 개수:',len(lst))


listBreaking()
# 14. 리스트내의 원소에 접근하기
# 1) index 접근방식
lst = list(range(1,11))
for idx in range(len(lst)): # range(len(lst)): [0,len(lst)-1]
    print(lst[idx], end=' ')
print()
# 2) iterator 접근방식
for e in lst:
    print(e, end=' ')

listBreaking()
# 15. 리스트내의 원소와 인덱스 정보를 모두 원할때 (enumerate)
lst = [e for e in range(1, 11)]
for tuple in enumerate(lst):
    idx, e = tuple  # Unpacking
    print(f'lst[{idx}] = {e}')


listBreaking()
# 16. All 사용하기
# ** 모든 조건이 참인 경우 판별하기: all(논리식)
max = 10
lst = list(range(1,max))
print(lst)
print(f"Q: lst 내의 모든 원소가 {max}보다 작습니까?")
if all( max>x for x in lst):
    print(f"A: lst 내의 모든 원소는 {max}보다 작습니다.")
else:
    print(f"A: lst 내의 모든 원소 중에 하나라도 {max}보다 작지 않은 것이 존재합니다.")


listBreaking()
# 17. Any 사용하기
# ** 하나라도 참인 경우 판별하기: any(논리식)
lst = [1,2,3,4,5,6]
max = 2
print(lst)
print(f"Q: lst 내의 어떤 원소가 {max}보다 작습니까?")
if any( max>x for x in lst):
    print(f"A: lst 내의 원소 중에 {max}보다 작은 원소가 있습니다.")
else:
    print(f"A: lst 내의 모든 원소는 {max}보다 크거나 같습니다.")
