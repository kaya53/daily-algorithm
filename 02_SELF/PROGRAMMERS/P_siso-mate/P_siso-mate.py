from collections import defaultdict


def solution(weights):
    answer = 0
    siso = defaultdict(int)
    weights.sort()

    for w in weights:
        if siso[w]:
            answer += siso[w]
        if not w % 2:
            siso[(w // 2) * 3] += 1
        if not w % 3:
            siso[(w // 3) * 4] += 1
        siso[w] += 1
        siso[w * 2] += 1
        # print(w, answer)

    return answer