import sys

sys.stdin = open('input.txt')

from collections import deque

r, c = map(int, input().split())  # 100이하의 자연수
arr = [list(map(int, input().split())) for _ in range(r)]
si, sj, sd = map(int, input().split())
ei, ej, ed = map(int, input().split())
si -= 1
sj -= 1
sd -= 1
ei -= 1
ej -= 1
ed -= 1

INF = int(1e9)
orders = [[INF] * c for _ in range(r)]  #출발점부터 해당 좌표까지 오는데 필요한 최소 명령의 배열
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 동서남북 순
change = [[3, 2], [2, 3], [0, 1], [1, 0]]  # 동서남북 각각이 왼/오 90도 회전했을 때의 방향
res = INF

q = deque()
q.append((si, sj, sd, 0))
while q:
    # 현재 좌표, 출발점부터 지금까지 오는데 필요한 명령
    ci, cj, now_dir, num = q.popleft()

    # if res < num: break
    # orders[ci][cj] > num이면; 저장된 최소 명령 수보다 지금 들어온 명령의 수가 더 작으면 갱신
    # orders 배열에 최소 명령 갱신하기
    if orders[ci][cj] > num:
        orders[ci][cj] = num

    if ci == ei and cj == ej:
        print(ci, cj, now_dir, num)
        if res < num: break
        if now_dir == ed:
            res = min(res, num)
        else:  # 방향이 다른 경우
            if ed in change[now_dir]:  # 한 번만 꺾으면 됨
                res = min(res, num + 1)
            else:
                res = min(res, num + 2)

    # 인접 찾기
    for k in range(4):
        # order_now = 0  # 이번 k에서 각 칸에 내리는 명령의 수
        ni, nj = ci + delta[k][0], cj + delta[k][1]
        if ni < 0 or ni >= r or nj < 0 or nj >= c or arr[ni][nj] == 1 or (ni == ci and nj == cj): continue
        # 명령 2: 갈 수 있는데 방향을 바꿔야 하는 경우 : 오른쪽으로 90도, 왼쪽으로 90도만 가능
        if k != now_dir:  # k: 다음 방향
            if k in change[now_dir]:  # 회전 가능
                q.append((ci, cj, k, num+1))
            # else:
            #     q.append((ci, cj, k, num + 2))

        # 명령 1: 방향이 같아서 뻗어 나가는 경우; 가능하면 1, 2, 3칸 뛰는 것을 모두 append한다.
        else:
            if not arr[ni][nj]:  # 한 칸
                if orders[ni][nj] < num + 1: continue
                q.append((ni, nj, k, num+1))
            else: continue

            nni, nnj = ni + delta[k][0], nj + delta[k][1]  # 두 칸
            if nni < 0 or nni >= r or nnj < 0 or nnj >= c or arr[nni][nnj] == 1: continue
            if not arr[nni][nnj]:
                if orders[nni][nnj] < num + 1: continue
                q.append((nni, nnj, k, num + 1))
            else: continue

            nnni, nnnj = nni + delta[k][0], nnj + delta[k][1]  # 세 칸
            if nnni < 0 or nnni >= r or nnnj < 0 or nnnj >= c or arr[nnni][nnnj] == 1: continue
            if not arr[nnni][nnnj]:
                if orders[nnni][nnnj] < num + 1: continue
                q.append((nnni, nnnj, k, num + 1))

print(res)