from math import sqrt


def solution(r1, r2):
    answer = 0
    for x in range(r2):
        r = 0
        y2 = sqrt(r2 ** 2 - x ** 2)
        y1 = 0
        if x < r1:
            y1 = sqrt(r1 ** 2 - x ** 2)
        r += int(y2) - int(y1)
        if int(y2) == y2 or int(y1) == y1:  # 여기가 문제인 것 같음
            r += 1
        answer += r
        # print(x, r)
    answer += 1
    # print(answer)
    answer *= 4  # 4사분면
    answer -= 4 * (r2-r1+1)  # 한 사분면 당 r2-r1 총 두개

    return answer


print(solution(2, 5))