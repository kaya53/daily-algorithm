import sys

sys.stdin = open('input.txt')

for _ in range(1):
    n, m, r = map(int, input().split())  # 행, 열, 회전 횟수
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    # 각각의 사각형을 1차원 배열로 만들기
    dir_ls = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    mono_ls = []
    for i in range(n//2 + 1):
        si, sj = i, i+1
        if si < i or si >= n-i or sj < i or sj >= m-i or visited[si][sj]: continue

        tmp = []
        k = 0
        while True:
            if si == i and sj == i:
                visited[si][sj] = 1
                break
            ni, nj = si + dir_ls[k][0], sj + dir_ls[k][1]
            if ni < i or ni >= n-i or nj < i or nj >= m-i:
                k = (k+1) % 4
                continue
            visited[si][sj] = 1
            tmp.append(arr[si][sj])
            si, sj = ni, nj
        tmp = [arr[i][i]] + tmp
        # print(tmp)
        mono_ls.append(tmp)

    for idx, ls in enumerate(mono_ls):
        lenL = len(ls)
        r %= lenL
        mono_ls[idx] = ls[r:] + ls[:r]

    for ii, mono in enumerate(mono_ls):
        ssi, ssj = ii, ii
        kk = 0
        for el in mono:
            visited[ssi][ssj] = el
            ni, nj = ssi + dir_ls[kk][0], ssj + dir_ls[kk][1]
            if ni < ii or ni >= n - ii or nj < ii or nj >= m - ii:
                kk = (kk + 1) % 4
                ssi, ssj = ssi + dir_ls[kk][0], ssj + dir_ls[kk][1]
                continue
            ssi, ssj = ni, nj

    for elem in visited:
        print(' '.join(map(str, elem)))
    print()


