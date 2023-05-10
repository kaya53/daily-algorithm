# 한칸씩 옆으로 가면서 보기 때문에 visited를 굳이 쓸 필요가 없음
import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline


def row_first(line, visited):
    j = 0
    while j < n-1:
        # 같아서 지나갈 수 있는 경우
        if line[j] == line[j+1]: j += 1
        elif abs(line[j] - line[j+1]) > 1: return False
        # 다음 수가 더 큰 경우
        elif line[j] - line[j+1] == -1:
            for k in range(j, j-l, -1):
                if k < 0 or line[j] != line[k] or visited[k]:
                    return False
            else:
                for k in range(j, j - l, -1):
                    visited[k] = 1
                j += 1
        # 다음 수가 더 작은 경우
        elif line[j] - line[j+1] == 1:
            for k in range(j+1, j+l+1):
                if k >= n or line[j+1] != line[k] or visited[k]:
                    return False
            else:
                for k in range(j + 1, j + l + 1):
                    visited[k] = 1
                j += l
    return True


# for _ in range(4):
n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for row in arr:
    if row_first(row, [0] * n):
        # print(i, end=' ')
        cnt += 1

zip_arr = list(map(list, zip(*arr)))
for col in zip_arr:
    # print(j)
    if row_first(col, [0] * n):
        cnt += 1
print(cnt)