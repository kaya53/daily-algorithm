# 소요시간 의미없음 python 40ms
# 약간의 머리쓰기 문제
# - 둘레 길이가 반시계 방향으로 나오고, ㄱ, ㄴ 형태의 육각형이기 때문에
# - 가장 긴 가로 변 양 옆으로 나오는 세로 길이의 차 = 뺄 부분 세로 길이
# - 가로 길이도 마찬가지!
import sys
sys.stdin = open('input.txt')

num = int(input())
inside = 0
width = []
height = []
arr = []
w, h = 0, 0
for i in range(6):
    d, l = map(int, input().split())
    if d == 2: w += l
    elif d == 4: h += l
    arr.append(l)
    if d < 3: width.append(l)
    else: height.append(l)
wIdx = arr.index(max(width))
hIdx = arr.index(max(height))

inside = abs(arr[(wIdx-1)%6] - arr[(wIdx+1)%6]) * abs(arr[(hIdx-1)%6] - arr[(hIdx+1)%6])
print(((w*h) - inside)*num)


