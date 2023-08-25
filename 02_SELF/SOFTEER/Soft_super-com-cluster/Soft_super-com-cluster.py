# 230804 185ms 67mb => 1시간 30분 소요 / 이진 탐색
# 예산이 10**18까지 주어지는데 right 최대값을 10**9로 해놔서 틀렸었다
# 그것보다 크게 하니까 맞았음
import sys

sys.stdin = open('input.txt')

# for _ in range(3):
N, B = map(int, input().split())
inp = list(map(int, input().split()))
cnt_dict = {}
for n in inp:
    if cnt_dict.get(n, -1) != -1: cnt_dict[n] += 1
    else: cnt_dict[n] = 1

perform = sorted(inp)
left = perform[0]
right = int(1e10)

while right-left > 1:
    mid = (left + right) // 2
    cost = 0
    for k, v in cnt_dict.items():
        if k < mid:
            cost += ((mid-k)**2)*v
            if cost > B:
                right = mid
                break
    # cost가 예산보다 커서 break 걸린 적이 없는 경우
    # cost 총합이 예산보다 작으니까 최저 성능을 높이기 위해 left를 mid로 옮김
    else:
        left = mid
print(left)