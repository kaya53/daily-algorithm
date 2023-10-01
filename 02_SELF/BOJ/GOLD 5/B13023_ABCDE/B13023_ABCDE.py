import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline

def backtrack(f_ls, cnt, arr, curr):
    if cnt == 5:
        # print(f_ls)
        return 1

    for nnext in arr[curr]:
        # print(curr, arr[curr], f_ls, cnt)
        if nnext in f_ls: continue
        f_ls.add(nnext)
        if backtrack(f_ls, cnt+1, arr, nnext): return 1
        f_ls.remove(nnext)
    return 0


def solution():
    n, m = map(int, input().rstrip().split())
    arr = [[] for _ in range(n)]
    for _ in range(m):
        s, e = map(int, input().rstrip().split())
        arr[s].append(e)
        arr[e].append(s)

    for i in range(n):
        s = set()
        s.add(i)
        if backtrack(s, 1, arr, i): return 1
    return 0


# for _ in range(4):
print(solution())