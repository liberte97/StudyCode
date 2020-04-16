import collections

def solution(participant, completion):
    answer = ''
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(collections.Counter(participant))
    answer = list(answer.keys())
    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))