import sys

sys.stdin = open('sample_input(6).txt')

from collections import deque

T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    infos = [tuple(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())  # 출발 노드, 도착 노드
    graph_arr = [[] for _ in range(v+1)]

    for si, ei in infos:
        graph_arr[si].append(ei)
        graph_arr[ei].append(si)  # 방향성이 없으니까
    # print(graph_arr)

    queue = deque()
    queue.append((s, 0))
    visited = [0] * (v+1)
    # print(queue)

    while queue:
        now, level = queue.popleft()
        if now == g:
            break
        # 방문 표시; 방문 한 애들은 ? 아래 코드 안 통과하게 하기
        if not visited[now]:
            visited[now] = 1

            # 다음 점으로 이동 => 큐에 넣기
            len_s = len(graph_arr[now])
            for i in range(len_s):
                queue.append([graph_arr[now][i], level+1])
    print(f'#{tc} {level}')