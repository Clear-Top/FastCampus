# 목적: 하루에 최대한 던전을 많이 탐험했을 때, 탐험한 던전 수 구하기

# 조건
#   현재피로도: k (1-5,000)
#   최소피로도, 소모피로도 (1~1,000)
#   최소피로도 >= 소모피로도 (always)
#   던전의 개수 (1~8) (팩토리얼가능)
#   행의 값이 똑같은 던전이 있을수도 있다. (중복허용해야함)

# ex. k=80, 던전=[[80,20]
#                [50,40],
#                [30,10]]
# 1 -> 2 -> X 은 두 번 탐험가능
# 3 -> X      은 한 번 탐험가능
# 1 -> 3 -> 2 은 세 번 탐험가능 (정답)

''' 던전관련 2차원 배열

        ["최소 필요 피로도", "소모 피로도"]
던전1         피로드1           피로도2
던전2         피로드1           피로도2
던전3         피로드1           피로도2
...           ...               ...

'''

from itertools import permutations

def solution(k, dungeons):
    # O(n!)
    # combi_dungeons = list(combinations(dungeons, 3))
    
    # O(n)
    # for combi_dungeon in combi_dungeons:
    
    # 일단 소모피로도 오름차순으로 정렬, 그 후에 최소 필요 피로도 내림차순
    # 그 후 별도의 처리가 필요?
    
    # dungeons.sort(key=lambda x:(x[1],-x[0]))
    # print(dungeons)
    # for dungeon in dungeons:
    #     if k >= dungeon[0]:
    #         k -= dungeon[1]
    #         answer += 1
    answer = 0    
    save_k = k
    pers =list( permutations(dungeons, len(dungeons)))
    
    for per in pers:
        search = 0
        save_k = k
        for dungeon in per:
            if save_k >= dungeon[0]:
                search += 1
                save_k -= dungeon[1]
        if answer < search:
            answer = search
    return answer

    # search = 0
    # for dungeon in [[80, 20], [30, 10], [50, 40]]:
    #     print(f"현재피로도: {k}")
    #     if k >= dungeon[0]:
    #         print("던전입장")
    #         search += 1
    #         k -= dungeon[1]
    #         print(f"남은피로도: {k}")
    #         print()
    #     if answer < search:
    #         answer = search
    # print(answer)