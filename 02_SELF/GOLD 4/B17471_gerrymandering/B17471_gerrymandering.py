import sys

sys.stdin = open('input.txt')


def count_population(arr):
    cnt_a1 = cnt_a2 = 0
    for i in range(1, n+1):
        if arr[i] == 1:
            cnt_a1 += population[i]
        elif arr[i] == 2:
            cnt_a2 += population[i]
    # if arr == [0, 1, 2, 1, 1, 2, 2, 2, 1] or arr == [0, 2, 1, 2, 2, 1, 1, 1, 2]:
    #     print(arr, abs(cnt_a1 - cnt_a2))
    return abs(cnt_a1 - cnt_a2)


# def gerry_dfs(si, x, cnt1, cnt2):
#     global min_res
#
#     if cnt1 + x == cnt2:
#         # 여기를 기준으로 아직 안 방문한 애들끼리 서로 연결이 되어 있지 않다면 리턴
#         # 연결이 되어 있다면 인구 차이를 구하기
#         visit = list(visited)
#         if x == 4: print(visit)
#         for i in range(1, n+1):
#             # if not visit[i]:
#             res = connected(i, cnt2+1, 1, visit)  # 나머지도 연결이 되어 있는 지 판별
#             if res and res.count(0) == 1:  # 모두 연결이 되어 있는 상태
#                 # 인구 차이 세기
#                 min_res = min(min_res, count_population(res))
#             return
#         # 0을 카운트 한 것이 1 이상이면 연결 1개이면
#         return
#     for ni in infos[si]:
#         if not visited[ni]:
#             visited[ni] = 1
#             gerry_dfs(ni, x, cnt1, cnt2+1)
#             visited[ni] = 0

def connected(num1, num2, i, selected): # cnt2: 2번째 영역의 크기
    for i in range(1, n + 1):
        if selected[i]:
            if selected[i] == 1 or selected[i] == 2:
                return []  # 연결이 안되어 있는 것
            for ni in infos[i]:
                if selected[ni] == num1:
                    selected[ni] = num2
                    connected(num1, num2, ni, selected)
            return selected


def subset(idx):
    if idx == n:
        print(selected)
        res_ls = connected(1, 3, selected)  # 판별할 번호, 바꿀 번호, 연결을 판별할 배열
        if res_ls:
            pass

        # 여기서 selected가 연결이 되어 있으면 그 배열을 가지고
        # 다른 아이들도 연결이 되어 있는 지 판별하기
        return
    selected[idx] = 1
    subset(idx+1)
    selected[idx] = 0
    subset(idx+1)



# for _ in range(4):
n = int(input())  # 구역의 개수
population = [0] + list(map(int, input().split()))  # 각 구역 인구; 1번 부터 세기 위해
infos = [0] + [list(map(int, input().split()))[1:] for _ in range(n)]
min_res = float('inf')
combs = []


# for y in range(1, n+1):  # 시작점
#     visited = [0] * (n + 1)
#     visited[y] = 1
#     for x in range(n-1):  # 뽑을 개수; n개를 다 고르면 선거구가 2개가 안되니까
#         gerry_dfs(y, x, 0, 0)

numbers = list(range(1, n+1))
tmp = [0] * n
selected = [0] * n
subset(0)

if min_res != float('inf'):
    print(min_res)
else:
    print(-1)