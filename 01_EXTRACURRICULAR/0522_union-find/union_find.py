N = 5
parents = [0] * N


# 단위 서로소 집합(크기 1)
def make_sets():
    # 모든 원소의 부모 => 자기 자신
    # 자기 자신이 곧 집합의 대표자
    for i in range(N):
        parents[i] = i


def union(a, b):
    # 대표자 구하기
    a_root = find(a)
    b_root = find(b)

    # 두 집합이 같은 집합인 경우
    if a_root == b_root: return False

    # 대표자끼리 합쳐준다 => 조직원(a, b)끼리 합치면 안된다!
    # 왼쪽 집합을 오른쪽으로 붙이든 그 반대로 하든 상관없음
    parents[b_root] = a_root

    # 유니온 성공
    return True
    

# a가 속한 집합의 대표자를 찾아서 반환
def find(a):
    # 자기 자신이 곧 대표자인지 확인
    if a == parents[a]: return a
    # return find(parents[a])  # path compression을 하지 않은 것
    parents[a] = find(parents[a])  # path compression을 한 것
    return parents[a]


make_sets()
print(parents)
print("union"+("="*30))
# print(f"union(0, 1) {union(0, 1)}")
# print(parents)
# print(f"union(1, 2) {union(1, 2)}")
# print(parents)
# print(f"union(3, 4) {union(3, 4)}")
# print(parents)
# print(f"union(0, 2) {union(0, 2)}")
# print(parents)
# print(f"union(0, 3) {union(0, 3)}")
# print(parents)
print(f"union(0, 1) {union(0, 1)}")
print(parents)
print(f"union(2, 1) {union(2, 1)}")
print(parents)
print(f"union(3, 2) {union(3, 2)}")
print(parents)
print(f"union(4, 3) {union(4, 3)}")
print(parents)

print("===find===")
print(f"find(4) {find(4)}")
print(parents)
print(f"find(3) {find(3)}")
print(parents)
print(f"find(0) {find(0)}")
print(parents)
print(f"find(2) {find(2)}")
print(parents)
print(f"find(1) {find(1)}")
print(parents)
