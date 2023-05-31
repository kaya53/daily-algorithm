import sys

sys.stdin = open('input.txt')


def comb(idx):
    if idx == len_e:
        print(choice)
        return

    for nnext in range(1, 13):
        if not num_cnt[nnext] or not check(idx, nnext): continue
        choice[idx] = nnext
        num_cnt[nnext] -= 1
        comb(idx+1)
        choice[idx] = 0
        num_cnt[nnext] += 1


def check(idx, num):
    ci, cj = empty[idx]  # 빈 칸의 좌표
    flag = 0
    for delta in [[(-1, 1)], [(1, -1)], [(-1, -1)], [(1, 1)], [(-2, 0), (2, 0)]]:
        tot = cnt = 0
        for di, dj in delta:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= 5 and nj < 0 or nj >= 9 or arr[ni][nj] == '.': break
            tot += arr[ni][nj]
            cnt += 1
        if cnt == 4 and tot + num <= 26: flag += 1
    if flag == 2: return True
    return False


arr = []
num_cnt = [2]*13
empty = []
for r in range(5):
    inp = list(map(str, input()))
    for c in range(9):
        if inp[c] == '.': continue
        elif inp[c] == 'x':
            inp[c] = 0
            empty.append((r, c))
        else:
            inp[c] = ord(inp[c])-64
            num_cnt[inp[c]] -= 1
    arr.append(inp)
# print(empty)
len_e = len(empty)

choice = [0] * len_e
comb(0)
# print(num_cnt)
# for a in arr:
#     print(a)