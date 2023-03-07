# print(2**15 - 22077)  # 10691

import sys

sys.stdin = open('input.txt')


def nemmo(linear):
    # 1차원으로 펼쳐진 배열을 이용해서 2*2가 존재하면 -= 1
    for i in range((n-1)*(m-1)):
        if not (n-1 % (i+1)): continue
        if linear[i] == 1:
            if linear[i+1] == 1 and linear[i+n] == 1 and linear[i+n+1] == 1:
                return False
            linear[i] = linear[i+1] = linear[i+n] = linear[i+n+1] = 0
    return True

def comb(cnt):
    global res_cnt
    if cnt == n*m:
        if not nemmo(linear):
            res_cnt -= 1
        return
    linear[cnt] = 1
    comb(cnt + 1)
    linear[cnt] = 0
    comb(cnt + 1)


n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
NUM = n*m
linear = [0] * NUM
res_cnt = 2**NUM


# for k in range(n*m):
comb(0)
print(res_cnt)
# print(tmp)