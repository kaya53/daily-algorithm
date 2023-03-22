import sys, math

input = sys.stdin.readline

n = int(input())
infos = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = n
for num in infos:
    if num < b: continue  # 주감독관 혼자 커버 가능한 경우
    val = math.ceil((num - b) / c)
    cnt += val
print(cnt)