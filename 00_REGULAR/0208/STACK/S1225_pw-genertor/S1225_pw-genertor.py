import sys
from collections import deque

sys.stdin = open('input.txt')


for _ in range(1, 11):
    tc = int(input())
    nums = deque(map(int, input().split()))
    minuses = list(range(1, 6))
    now_m = 0

    while True:
        # 종료 조건: 배열 내 어떤 수가 0이 될 때
        if now_m > 4:
            now_m %= 5
        calc = nums.popleft() - minuses[now_m]
        if calc <= 0:
            nums.append(0)
            break
        nums.append(calc)
        now_m += 1

    res = ' '.join(map(str, nums))
    print(f'#{tc} {res}')
