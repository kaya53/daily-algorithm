# 재귀를 이용하는 이유?  경우의 수 만들기

# recursive 로 순열(permutation)만들기
# [0 1 2 3] 를 가지고
# 2개의 순열은?
# 0 1, 0 2, 0 3, 1 0, 1 2, 1 3, 2 0, 2 1, 2 3, 3 0, 3 1, 3 2


def p2_permutation(n):
    permu_list = []
    for i in range(n):
        for j in range(n):
            if i == j: continue  # 두개가 같은 경우만 빼고 순서없이 다 뽑기
            permu_list.append([i, j])
    print(permu_list)

p2_permutation(4)

# 반복문으로 쓰기
def p3_permutation(n):
    permu_list = []
    for i in range(n):
        for j in range(n):
            if i == j: continue
            for z in range(n):
                if j == z: continue
                if i == z: continue
                permu_list.append([i, j, z])


    print(permu_list)

p3_permutation(4)

P = 3
N = 4
visit = [0] * N
permu_list = []
def pP_permutation1(L, choice):
    if L >= P:
        permu_list.append(list(choice))
        return
    for i in range(N):
        if not visit[i]:
            choice.append(i)
            visit[i] = 1
            pP_permutation1(L+1, choice)
            choice.pop()
            visit[i] = 0

pP_permutation1(0, [])
print(permu_list)
