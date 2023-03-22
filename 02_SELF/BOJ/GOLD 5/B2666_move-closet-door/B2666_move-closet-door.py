import sys

sys.stdin = open('input.txt')

# from collections import deque

# def check(closet_no, door):
#     q = deque()
#     q.append((closet_no, 0))
#     visited = [0] * (n+1)
#     visited[closet_no] = -1
#     while q:
#         now, cnt = q.popleft()
#         if now == door:
#             return cnt
#         for di in [-1, 1]:
#             nnext = now + di
#             if nnext < 1 or nnext > n: continue
#             if visited[nnext]: continue
#             visited[nnext] = cnt + 1
#             q.append((nnext, cnt + 1))


def recur(idx, res, door1, door2):
    global mmin, c1, c2
    if res >= mmin: return  # 이거 넣었더니 10배 빨라짐
    if idx == m:
        # 최소값 갱신
        if mmin > res:
            mmin = res
        return
    # val1 = check(infos[idx], door1)  # 이걸 굳이 해줄 필요없이 1차원 배열이니까 그냥 빼주면 됨..!(유진이 코드 참고)
    val1 = abs(infos[idx] - door1)
    recur(idx+1, res+val1, infos[idx], door2)  # 문 1 고르기
    val2 = abs(infos[idx] - door2)
    recur(idx+1, res+val2, door1, infos[idx])  # 문 2 고르기


n = int(input())
c1, c2 = map(int, input().split())  # 처음에 열려있는 벽장 정보
m = int(input())  # 사용할 벽장의 개수
infos = [int(input()) for _ in range(m)]  # 사용할 벽장 정보
mmin = int(1e9)
recur(0, 0, c1, c2)
print(mmin)