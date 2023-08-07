import sys
# from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input().strip())

def find(name):
    '''
    이름에 대한 부모찾기
    '''
    if name == parent_table[name]:
        return name
    parent_table[name] = find(parent_table[name])
    return parent_table[name]

def union(name1, name2):
    parent1 = find(name1)
    parent2 = find(name2)
    if parent1 != parent2:
        parent_table[parent2] = parent1 # 오른쪽을 왼쪽이름에 합치기
        count_table[parent1] += count_table[parent2]
    return None

for _ in range(n):
    parent_table = dict()
    count_table = dict()
    number_of_relations = int(input().strip())
    for _ in range(number_of_relations):
        name1, name2 = input().strip().split(' ')
        if name1 not in parent_table:
            parent_table[name1] = name1
            count_table[name1] = 1
        if  name2 not in parent_table:
            parent_table[name2] = name2
            count_table[name2] = 1
        
        union(name1, name2)

        print(count_table[find(name1)])
