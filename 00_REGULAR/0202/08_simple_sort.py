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
# N = 30000
# scores = random.sample(range(0, 1000000000), N)
N = 8
scores = list(map(int, '70 30 70 40 60 50 90 80'.split()))
ids = [i for i in range(1, N+1)] # list(range(1, N+1))과 같음

# 버블 소트 3번
# 소팅은 되는 데 점수가 같은 경우 id가 작은 학생을 선택하는 것은 안된다
for _ in range(3):
    for i in range(N-1):
        if scores[i] > scores[i+1]:
            ids[i], ids[i+1] = ids[i+1], ids[i]
            # scores[i], scores[i+1] = scores[i+1], scores[i]
        if scores[i] == scores[i+1]:  # 인접한 원소끼리만 비교하니까 반례가 존재함
            ids[i], ids[i+1] = ids[i+1], ids[i]

print(' '.join(map(str, ids[-1: -4: -1])))
print(ids)


## 강사님 해설
# 시간 복잡도: O(M*N); M=N이면 O(N**2)
def simple_sort(N, M, arr):
    ids = list(range(1, N+1))
    for i in range(M):
        for j in range(i+1, N):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                ids[i], ids[j] = ids[j], ids[i]
            elif (arr[i] == arr[j]) and (ids[i] > ids[j]):  # 점수가 같으면 더 작은 아이디가 나오도록
                ids[i], ids[j] = ids[j], ids[1]
    return ids[:M]

print(simple_sort(N, 3, scores))