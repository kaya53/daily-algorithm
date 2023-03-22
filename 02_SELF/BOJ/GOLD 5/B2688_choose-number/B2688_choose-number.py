import sys

sys.stdin = open('input.txt')

N = int(input())
arr = [0] + [int(input()) for _ in range(N)]

# print(arr)

def dfs(si):
    global cycle

    visited[si] = 1
    cycle.append(si)
    next = arr[si]

    if not visited[next]:
        dfs(next)
    else:  # 방문했다면
        for idx, elem in enumerate(cycle):
            if elem == next:  # 사이클 시작점 찾기
                for k in range(idx, len(cycle)):
                    res.append(cycle[k])
        cycle = []
        return

visited = [0] * (N+1)
cycle = []
res = []
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)

print(len(res))
for r in sorted(res):  # 작은 수 -> 큰 수 순으로 출력하는 걸 간과함
    print(r)