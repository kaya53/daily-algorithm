def backtrack(ci, N, col, diag):
    global res
    if ci == N:
        res += 1
        return

    for nj in range(N):
        if col[nj]: continue
        if check_diag(ci, nj, diag): continue
        col[nj] = 1
        diag.append((ci, nj))
        backtrack(ci+1, N, col, diag)
        col[nj] = 0
        diag.pop()


def check_diag(ci, cj, diag):
    for di, dj in diag:
        if abs(ci-di) == abs(cj-dj): return True
    return False


res = 0
def solution():
    N = int(input())
    backtrack(0, N, [0] * N, [])

solution()
print(res)