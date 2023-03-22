# import sys
#
# sys.stdin = open('input.txt')
#
# # 빨강에서 초록, 파랑보드로 움직임
# def move(b, si, sj):
#     if b == 1:
#         # 아래 두 보드에서 쓰이는 ci, cj 변수 안꼬이나 잘 보기
#         # 파랑 보드
#         ci, cj = si, sj
#         for nj in range(sj+1, 10):
#             if arr[si][nj] == 1: break
#             cj = nj
#         arr[si][cj] = 1
#         # 초록 보드
#         for ni in range(si+1, 10):
#             if arr[ni][sj] == 1: break
#             ci = ni
#         arr[ci][sj] = 1
#
#     elif b == 2:
#         ci, cj = si, sj
#         for nj in range(sj+1, 10):
#             pass
#     else:
#         pass
#
#
# # 초록, 파랑보드에 지워질 행/열이 있는 지
# def check():
#     pass
#
#
# # 연한 부분 체크
# def check_pastel():
#     pass
#
#
# n = int(input())
# infos = [list(map(int, input().split())) for _ in range(n)]
#
# # 도미노판 구현
# arr = [[0]* 10 for _ in range(10)]
# for i in range(4, 10):
#     for j in range(4, 10):
#         arr[i][j] = -1
#
# # 주어진 블럭 개수만큼 진행
# for info in infos:
#     b, si, sj = info
#     move(b, si, sj)
#     check()
#     check_pastel()

for i in range(2, 0, -1):
    print(i)