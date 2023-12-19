# 소요시간 30분 python 48ms
# 전형적 백트래킹 문제
import sys

sys.stdin = open('input.txt')


def backtrack(idx, ci, b, block, teacher, arr, choice):
    if idx == 3:
        if check(teacher, arr, choice): return True
        return False

    for ni in range(ci, b):
        choice[idx] = block[ni]
        if backtrack(idx+1, ni+1, b, block, teacher, arr, choice): return True
        choice[idx] = ()
    return False


def check(teacher, arr, choice):
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for ti, tj in teacher:
        for di, dj in delta:
            k = 1
            while True:
                ni, nj = ti + di*k, tj + dj*k
                # 인덱스 밖이거나 장애물이면 다음으로
                if ni < 0 or ni >= N or nj < 0 or nj >= N or (ni, nj) in choice:
                    break
                if arr[ni][nj] == 'S': return False
                k += 1
    return True


def solution(n, arr):
    block = []
    teacher = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'X': block.append((i, j))
            elif arr[i][j] == 'T': teacher.append((i, j))
    if backtrack(0, 0, len(block), block, teacher, arr, [(), (), ()]):
        return 'YES'
    return 'NO'


# for _ in range(2):
N = int(input())
a = [list(input().split()) for _ in range(N)]
print(solution(N, a))