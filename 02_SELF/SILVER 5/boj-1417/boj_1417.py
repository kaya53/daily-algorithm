import sys

sys.stdin = open('input.txt')

for _ in range(5):
    N = int(sys.stdin.readline().rstrip())  # 총 후보 수
    arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]  # n-1번째 후보들의 득표 수

    cnt = 0
    while len(arr) > 1 and (max(arr) >= arr[0]):  # 후보들의 최대 득표수가 다솜이의 득표수가 같거나 더 클 때
        mmax = max(arr)
        if mmax == arr[0] and mmax not in arr[1:N]:  # 다솜이의 득표수가 유일한 최대일 때
            break
        # max_idx = arr.index(mmax)  # 문제: 이렇게 하니까 모두 득표수가 같을 때 다솜이 표가 깎임
        max_idx = 0
        for i in range(1, N):  # idx 1 이후로 최대값 하나만 찾기
            if arr[i] == mmax:
                max_idx = i
                break
        arr[max_idx] -= 1
        arr[0] += 1
        cnt += 1


    print(cnt)

# 디버깅 1
# 이렇게 했을 때 후보가 1명인 경우 cnt = 1로 잡힘 => line 10에 len(arr) > 1 추가
# while max(arr) >= arr[0]:  # 후보들의 최대 득표수가 다솜이의 득표수가 같거나 더 클 때
#     mmax = max(arr)
#     if mmax == arr[0] and mmax not in arr[1:N]:  # 다솜이의 득표수가 유일한 최대일 때
#         break
#     # max_idx = arr.index(mmax)  # 문제: 이렇게 하니까 모두 득표수가 같을 때 다솜이 표가 깎임
#     max_idx = 0
#     for i in range(1, N):
#         if arr[i] == mmax:
#             max_idx = i
#             break
#     arr[max_idx] -= 1
#     arr[0] += 1
#     cnt += 1

# 디버깅 2 => 이렇게 제출했더니 틀림
# cnt = 0
# while len(arr) > 1 and (max(arr) >= arr[0]):  # 후보들의 최대 득표수가 다솜이의 득표수가 같거나 더 클 때
#     mmax = max(arr)
#     # max_idx = arr.index(mmax)  # 문제: 이렇게 하니까 모두 득표수가 같을 때 다솜이 표가 깎임
#     max_idx = 0
#     for i in range(1, N):
#         if arr[i] == mmax:
#             max_idx = i
#             break
#     arr[max_idx] -= 1
#     arr[0] += 1
#     cnt += 1
#     if max(arr) == arr[0] and max(arr) not in arr[1:N]:  # 다솜이의 득표수가 유일한 최대일 때
#         break

# 찾은 반례 ) 원래 다솜이가 가장 고득표인 경우에 cnt = 1로 잡힘 (4 100 1 1 1)
# => while문 가장 끝에 작성한 if문을 처음으로 옮김 ; 이렇게 하니까 통과함
