# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=449
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=458

# 재귀를 이용하는 이유?  경우의 수 만들기

# reculsive 로 조합(combination)만들기
# [0 1 2 3] 를 가지고
# 2개의 조합은?
# 0 1, 0 2, 0 3, 1 2, 1 3, 2 3
# 3개의 조합은?
# 0 1 2, 0 1 3, 0 2 3, 1 2 3

def c2_combination(n):
    combi_list = []
    for i in range(n-1):
        for j in range(i+1, n):
            combi_list.append([i, j])
    print(combi_list)


def c3_combination(n):
    combi_list = []
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                combi_list.append([i, j, k])
    print(combi_list)

# [0, 1, 2], [0, 1, 3], [0, 1, 4] ....
#c3_combination(5)

# 재귀를 사용한  combination
C = 3
N = 5
# 5개 데이터에서 3개를 뽑는
choice = [0]*C
combi_list = []
def cC_combination(L, p):
    if L == C:
        print('cC_combination', choice)
        return
    for i in range(p+1, N+1):
        choice[L] = i
        cC_combination(L+1, i)
        choice[L] = 0

cC_combination(0, 0)
# print(combi_list)

C = 3
N = 5
choice = [0] * C
combi_list = []
def cC_combination2(L, p):
    pass

cC_combination2(0, 0)
print(combi_list)

C = 3
N = 5

combi_list = []
def cC_combination3(L, p, choice):
    pass

cC_combination3(0, 0, [])
print(combi_list)
