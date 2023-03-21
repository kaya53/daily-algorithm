# double linked list
import sys, os, __pypy__
sys.stdin = open('input.txt')

input = sys.stdin.readline


n, m = map(int, input().split())  # 공사 시작 전 역의 개수, 공사 횟수
node = [0] * (10**6 + 1)
# 앞으로 연결된 노드들
node_prev = [0] * (10**6 + 1)  # 0 대신 None을 쓰면 시간 초과가 날 수 있음
# 뒤로 연결된 노드들
node_next = [0] * (10**6 + 1)

ls = list(map(int, input().split()))
# 초기 연결 리스트 만들기
for d in range(n):
    # node[ls[d]] = 1
    node_prev[ls[d]] = ls[d-1]
    node_next[ls[d]] = ls[d+1]

# print(node_prev[:8], node_next[:8], sep='\n')

ans = __pypy__.builders.StringBuilder()
for _ in range(m):
    inp = list(input().split())
    if inp[0] == 'BN':
        i, j = int(inp[1]), int(inp[2])
        after = node_next[i]  # 2
        node_next[i] = j
        node_prev[after] = j
        node_prev[j] = i
        node_next[j] = after
        # print(node_prev[:12], node_next[:12], sep='\n')
        ans.append(str(after) + '\n')
    elif inp[0] == 'BP':
        i, j = int(inp[1]), int(inp[2])  # 3, 6
        before = node_prev[i] # 7
        node_prev[i] = j
        node_next[before] = j
        node_prev[j] = before
        node_next[j] = i
        # print(node_prev[:12], node_next[:12], sep='\n')
        ans.append(str(before) + '\n')
    elif inp[0] == 'CP':
        i = int(inp[1])
        target = node_prev[i]
        target_prev = node_prev[target]
        # print(target, target_prev)  # 11 5
        node_prev[i] = target_prev
        node_next[target_prev] = i
        node_prev[target] = node_next[target] = 0
        ans.append(str(target) + '\n')
    elif inp[0] == 'CN':
        i = int(inp[1])
        target = node_next[i]  # 6
        target_next = node_next[target]  # 3
        node_next[i] = target_next
        node_prev[target_next] = i
        node_prev[target] = node_next[target] = 0
        # print(node_prev[:12], node_next[:12], sep='\n')
        ans.append(str(target) + '\n')

print(node_prev[:12], node_next[:12], sep='\n')
os.write(1, ans.build().encode())