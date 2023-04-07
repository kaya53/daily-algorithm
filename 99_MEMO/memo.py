arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for l in list(map(list, zip(*arr[::-1]))):
    print(l)
# 격자 시계 90도 회전
n = 6
half = 3
rotated = [[0] * 3 for _ in range(3)]
for i in range(0, n, half + 1):
    for j in range(0, n, half + 1):
        for ki in range(half):
            for kj in range(half):
                # rotated[i + kj][j + half - ki - 1] = arr[i + ki][j + kj]
                rotated[i + half - kj -1][j + ki] = arr[i + ki][j + kj]
        break
    break

for r in rotated:
    print(r)