'''
수포자 1: 1,2,3,4,5, ...
수포자 2: 2,1,2,3,2,4,2,5,2, ...
수포자 3: 2,2,1,1,3,3,4,4,5,5, ...
'''

# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42840

# 해결여부: O
# 해결시간: 30분 초과

def solution(answers):
    
    rule_1 = [1,2,3,4,5]
    rule_2 = [2,1,2,3,2,4,2,5]
    rule_3 = [3,3,1,1,2,2,4,4,5,5]

    exam_1 = rule_1 * int(len(answers)/len(rule_1)) + [rule_1[i] for i in range(len(answers)%len(rule_1))]
    exam_2 = rule_2 * int(len(answers)/len(rule_2)) + [rule_2[i] for i in range(len(answers)%len(rule_2))]
    exam_3 = rule_3 * int(len(answers)/len(rule_3)) + [rule_3[i] for i in range(len(answers)%len(rule_3))]

    results = [0] * 3
    for answer, one, two, three in zip(answers, exam_1, exam_2, exam_3):
        if answer == one:
            results[0] += 1
        if answer == two:
            results[1] += 1
        if answer == three:
            results[2] += 1
    
    max_value = max(results)
    results_2 = list(filter(lambda x:results[x]==max_value,range(3)))


    return list(map(lambda x:x+1, results_2))


# print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))

'''다른사람풀이
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
'''