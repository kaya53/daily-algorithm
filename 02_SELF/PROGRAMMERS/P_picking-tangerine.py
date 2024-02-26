from collections import Counter


def solution(k, tangerine):
    # answer = 0
    n = len(tangerine)
    tang_dict = Counter(tangerine)
    cnt_ls = sorted(list(tang_dict.values()))
    m = len(cnt_ls)
    tot = 0
    # print(cnt_ls)
    for c in cnt_ls:
        # print('now', c, tot)
        n -= c
        if n == k:
            # print('딱 0개', m-(tot+1))
            return m-(tot+1)
        elif n < k:
            # print('k 이하', m-(tot))
            return m-tot
        tot += 1