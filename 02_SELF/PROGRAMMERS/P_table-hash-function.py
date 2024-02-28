def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    tot = 0
    for i in range(row_begin - 1, row_end):
        now = 0
        for val in data[i]:
            now += (val % (i + 1))
        # print(now)
        tot ^= now
    return tot
