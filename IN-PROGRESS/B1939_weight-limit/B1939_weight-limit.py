# python3 232ms
# 이진 탐색 문제라고 해서 풀긴 했는 데 크루스칼로 풀림
# 이전 크루스칼 풀이에서 틀린 이유
# 1. parents[start], parents[end]를 비교하면 같은 부모를 보고 있더라도 다른 경우가 있을 수 있음
# - 그래서 find로 비교를 해줘야 함

# 이진 탐색 사용 방식
# 1. 최소거리(left) = 0, 최대 거리(right) = max(간선 가중치) or 1억
# - 거리를 이진탐색 한 후 해당 거리에서 간선이 모두 이어지는 지 본다
# => 이렇게 생각해보면 간선 가중치가 큰 순서대로 봤을 때
# start, end가 연결이 되었을 때 그 가중치가 가능한 최대값이라는 것을 유추할 수 있으므로
# 크루스칼을 쓰는 게 더 빠르다
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find(k, parents):
    if k == parents[k]: return k
    parents[k] = find(parents[k], parents)
    return parents[k]


def union(a, b, parents):
    a_root = find(a, parents)
    b_root = find(b, parents)
    if a_root == b_root: return False # 이미 합쳐진 것
    parents[b_root] = a_root
    return True


def solution(n, m, bridges, start, end):
    bridges.sort(key=lambda x: -x[2]) # 가중치에 내림차순으로

    start -= 1
    end -= 1
    parents = list(range(n))  # 자기 자신으로 초기화
    for s, e, w in bridges:
        union(s-1, e-1, parents)  # s-1, e-1 합치기
        if find(start, parents) == find(end, parents):
            return w


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
S, E = map(int, input().split())

print(solution(N, M, arr, S, E))