# def dp(n):
#     global cnt
#
#     if N == 1 or N == 2:
#         arr[n] = n - 1
#         return arr[n]
#     if not n % 3:
#         arr[n] = 1 + dp(n//3)
#         return arr[n]
#     if not n % 2:
#         arr[n] = 1 + dp(n//2)
#         return arr[n]
#     arr[n] = dp(n-1)
#     return arr[n]

N = int(input())
arr = [0] * (N+1)

# 1은 해야 의미가 없으니 2부터
for i in range(2, N+1):
    # 3번 연산
    arr[i] = arr[i-1] + 1
    # 1번 연산
    if not i % 3:
        arr[i] = min(arr[i], arr[i//3] + 1)
    if not i % 2:
        arr[i] = min(arr[i], arr[i//2] + 1)
print(arr[N])