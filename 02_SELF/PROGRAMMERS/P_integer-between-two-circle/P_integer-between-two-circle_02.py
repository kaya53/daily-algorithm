from math import sqrt


def solution(r1, r2):
    answer = 0
    for x in range(1, r2 + 1):
        y2 = sqrt((r2 * r2) - (x * x))
        y2 = int(y2) * 2 + 1
        y1 = 0
        if x < r1:
            y1 = sqrt((r1 * r1) - (x * x))
            if int(y1) == y1:
                y1 = int(y1)
                y1 = 2 * y1 - 1
            else:
                y1 = int(y1)
                y1 = 2 * y1 + 1
        # print(x, y2-y1)
        answer += (y2 - y1)
    answer *= 2
    answer += 2 * (r2 - r1 + 1)

    return answer