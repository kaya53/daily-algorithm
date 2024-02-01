# 참고 : https://www.ai-bio.info/programmers/152995
def solution(scores):
    answer = 0
    ta, tb = scores[0]
    ts = ta + tb

    maxb = 0
    # 두 점수 중에서 하나를 기준으로 정렬해 놓는다
    # a 점수는 내림차순으로 "고정되어 있으니까"
    # b 점수에 대해서만 대소를 확인하면 된다
    scores.sort(key=lambda x: (-x[0], x[1]))

    for a, b in scores:
        print(a, b, maxb)
        if ta < a and tb < b: return -1

        if b >= maxb:  # 인센 받을 수 있는 조건
            maxb = b
            if (a + b) > ts: answer += 1
    return answer + 1