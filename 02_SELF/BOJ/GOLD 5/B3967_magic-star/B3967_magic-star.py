# 230601 python 592ms, pypy 440ms => 2시간 소요
# 유의할 점
# 가장 먼저 나온 것이 무조건 사전 순으로 먼저이므로 하나 나오면 리턴한다.
import sys

sys.stdin = open('input.txt')


def comb(idx):
    global res
    if res: return
    if idx == len_e:
        for s in status:
            if sum(s) != 26: break
        else:
            res = list(choice)
        return

    for nnext in range(1, 13):
        if not num_cnt[nnext]: continue
        ci, cj = empty[idx]  # 빈 칸의 좌표
        l1, l2 = loc_dic[(ci, cj)]
        if not check(l1, l2, nnext): continue
        status[l1].append(nnext)
        status[l2].append(nnext)
        choice[idx] = nnext
        num_cnt[nnext] = 0
        comb(idx+1)
        status[l1].pop()
        status[l2].pop()
        choice[idx] = 0
        num_cnt[nnext] = 1


def check(l1, l2, num):
    for l_no in [l1, l2]:
        if sum(status[l_no]) + num > 26: return False
    return True


loc_dic = {
    (0, 4): [0, 1], (1, 1): [3, 4], (1, 3): [0, 3], (1, 5): [1, 3], (1, 7): [3, 5],
    (2, 2): [0, 4], (2, 6): [1, 5], (3, 1): [0, 2], (3, 3): [2, 4], (3, 5): [2, 5],
    (3, 7): [1, 2], (4, 4): [4, 5]
}
arr = []
num_cnt = [1]*13
empty = []  # 채워야 할 빈칸
status = [[] for _ in range(6)]
for r in range(5):
    inp = list(map(str, input()))
    for c in range(9):
        if inp[c] == '.': continue
        elif inp[c] == 'x':
            empty.append((r, c))
        else:
            inp[c] = ord(inp[c])-64
            num_cnt[inp[c]] -= 1
            for line in loc_dic[(r, c)]:
                status[line].append(inp[c])
    arr.append(inp)
# print(empty)
len_e = len(empty)
choice = [0] * len_e
res = []
comb(0)

# output
for e in range(len_e):
    ei, ej = empty[e]
    arr[ei][ej] = res[e]

for ii in range(5):
    for jj in range(9):
        if arr[ii][jj] == '.': continue
        arr[ii][jj] = chr(arr[ii][jj] + 64)
    print(''.join(map(str, arr[ii])))

