import sys

sys.stdin = open('input.txt')

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

cnt = 0
for i in range(n-2):
    frog = arr[i]
    for j in range(i+1, n-1):  # 첫번째 턴: 현재 원소 다음 원소부터 마지막 원소 전까지
        n_frog = arr[j]  # 다음 요소
        reap1 = n_frog - frog  # 첫번째 턴에서 뛴 거리
        for k in range(j+1, n):  # 두번째 턴: n_frog 다음 원소부터 끝까지
            l_frog = arr[k]
            reap2 = l_frog - n_frog
            if reap1 <= reap2 <= 2*reap1:
                cnt += 1
print(cnt)