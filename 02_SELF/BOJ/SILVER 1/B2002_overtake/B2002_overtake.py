# 소요시간 20분 python 144ms
# - 현재 차의 뒤에 스타팅 그리드가 낮은 차가 하나라도 있으면 => 추월을 한 것
import sys

sys.stdin = open('input.txt')

for _ in range(3):
    N = int(input())
    in_dict = {}
    out = []
    for i in range(N):
        s = input()
        in_dict[s] = i
    for j in range(N, 2*N):
        c = input()
        out.append(c)

    overtake = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if in_dict[out[i]] > in_dict[out[j]]:
                overtake += 1
                break
    print(overtake)

