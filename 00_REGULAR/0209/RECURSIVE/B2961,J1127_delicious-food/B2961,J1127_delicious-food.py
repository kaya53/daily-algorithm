## 재귀 구조로 짜야하는 이유: 재료를 선택해야 하는 데 몇 개를 선택해야 하는 지 나와있지 않다

# 1) 재료 선택의 모든 경우의 수
# 2) argument 설계
# 3) 함수의 동작을 1줄 기술
# 4) 전역 변수
import sys
sys.stdin = open('input.txt')
for _ in range(3):
    N = int(input())
    ingredients = [list(map(int, input().split())) for _ in range(N)]

    # 파워셋 이용하기
    ans = 10**9
    is_selected = [False] * N
    def powerset(idx, sour, bitter):
        global ans
        # 종료 조건
        if idx == N:
            if is_selected != [False] * N: # 공집합 빼기
                ans = min(ans, abs(sour-bitter))
            return

        # 재귀 유도
        is_selected[idx] = True
        powerset(idx+1, sour*ingredients[idx][0], bitter+ingredients[idx][1])
        is_selected[idx] = False
        powerset(idx+1, sour, bitter)

    powerset(0, 1, 0)  # 신맛은 곱셈이고, 쓴맛은 덧셈이니까 이렇게 초기화
    print(ans)

    # 조합 이용하기
    # choice = []
    # res = 10**9
    # def food(num, cnt, si, sour, bitter):  # num: 고를 재료 수, cnt: 지금까지 고른 재료 수, si: 고른 재료 번호
    #     global res
    #     if num == cnt:
    #         # print(choice)
    #         # print(abs(sour-bitter))
    #         # print('---------')
    #         res = min(res, abs(sour-bitter))
    #         return
    #     for i in range(si, N+1):
    #         choice.append(i)  # i: 고른 재료 번호
    #         food(num, cnt+1, i+1, sour*ingredients[i][0], bitter+ingredients[i][1])  # 다음 조합 구하러 가기
    #         choice.pop()
    #     # comb(num+1, 0, 0, [])  # 고를 재료 수 늘려서 고르러 가기
    #     # return
    #
    # for num in range(1, N+1):
    #     food(num, 0, 1, 1, 0)
    #
    # print(res)
# N = 3 # 전체 재료 수
# choice = []
# def comb(num, cnt, si, arr):  # num: 고를 재료 수, cnt: 지금까지 고른 재료 수, si: 고른 재료 번호
#     if num > N:
#         return
#     if num == cnt:
#         print(arr)
#         return
#     for i in range(si, N+1):
#         # cnt += 1  # 골랐으니까 증가
#         comb(num, cnt+1, i+1, arr+[i])  # 다음 조합 구하러 가기
    # comb(num+1, 0, 0, [])  # 고를 재료 수 늘려서 고르러 가기
    # return

# for num in range(1, N+1):
#     comb(num, 0, 1, [])
# print('------------')
