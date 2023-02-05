# N명의 점수가 주어질 때 상위 3명의 ID를 출력하는 프로그램을 작성하시오.
# 입력
# 첫 줄에 학생 수 N(3≤N≤30,000)이 주어진다.
# 둘째 줄에는 N개의 점수가 공백으로 구분되어 ID 순으로 주어진다. (각 점수는 0 이상 10억 이하)
# 맨 먼저 입력된 점수는 ID가 1인 학생의 점수이고, 이후부터 순서대로 ID가 1씩 증가한다.
# 8
# 70 30 70 40 60 50 90 80
# 출력
# 점수가 가장 높은 학생의 ID 3개를 순서대로 출력한다.
# 만일 점수가 같은 경우는 ID가 작은 학생을 선택한다.
# 7 8 1
import random
import math
random.seed(0)

N = 30000
scores = random.sample(range(0, 1000000000), N)
#
# # 시간복잡도 O(3N)
# ids = list(range(1, N+1))
# i = 0
# for _ in range(3):
#     for j in range(1, N):
#         if scores[j] > scores[i]:
#             scores[i], scores[j] = scores[j],scores[i]
#             ids[i], ids[j] = ids[j], ids[i]
#     print(ids[0])
#     scores,ids = scores[1:],ids[1:]
#     N -= 1


def code_01(scores):
    lst = [(idx, score) for idx, score in enumerate(scores, start=1)]
    student, grade = [-1, -1, -1], [-1, -1, -1]

    for idx, score in lst:
        if score > grade[0]:
            grade[1], grade[2] = grade[0], grade[1]
            student[1], student[2] = student[0], student[1]
            student[0], grade[0] = idx, score
        elif score > grade[1]:
            student[2], grade[2] = student[1], grade[1]
            student[1], grade[1] = idx, score
        elif score > grade[2]:
            student[2], grade[2] = idx, score
    return student

a = [1, 8, 2, 4, 8, 8, 2, 10, 6, 9]
student = code_01(a)
print(*student)

#print(N * math.log(N, 2))

# 시간복잡도 : O(N**2)
def simple_sort(N, a):

    for i in range(N-1):
        for j in range(i+1, N):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    return a


# 시간복잡도 : O(M*N)
def simple_sort_wIDs(N, M, a):
    a = a.copy()
    ids = list(range(1, N + 1))

    for i in range(M):
        for j in range(i+1, N):
            if a[i] < a[j]:  # max 찾아 a[i]에 위치
                a[i], a[j] = a[j], a[i]  ## 큰걸 앞으로 이동
                ids[i], ids[j] = ids[j], ids[i]   # 동일한 값일 때 id가 작은 것을 ids[i]에 위치
            elif (a[i] == a[j]) and (ids[i] > ids[j]):
                ids[i], ids[j] = ids[j], ids[i]

    return ids[:M]


# N = 10
# #a = random.sample(range(0, 100), N)
# a = [1, 8, 2, 4, 8, 8, 2, 10, 6, 9]
# print(a)
# sol = simple_sort_wIDs(N, 3, a)
# print(a)
# print(' '.join(map(str, sol)))

