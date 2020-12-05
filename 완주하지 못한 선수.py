import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# collections.Conter idx, data로 분류


# def solution(participant, completion):
#     p = {}
#     save = 0
#     for i in participant:
#         p[hash(i)] = i
#         save += int(hash(i))
#     for j in completion:
#         save -= hash(j)

#     return p[save]

# i를 hash 주소 i에 저장해 놓고 같은 해쉬 주소의 저장 데이터를 빼낸다.
