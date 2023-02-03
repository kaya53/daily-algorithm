import sys

sys.stdin = open('input.txt')

T = int(input())

arr = [2, 3, 5, 7, 11]  # 모든 테케에 대해 같으니까 여기에 위치

for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 5
    for i, num in enumerate(arr):
        while not (N % num):
            N //= num
            cnt[i] += 1

    res = ' '.join(map(str, cnt))
    print(f'#{tc} {res}')