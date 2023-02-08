## 정올 함수3(재귀함수) - 형성평가 3과 같음
N, M = map(int, input().split())

choice = [0] * N
def dice(level, ssum):
    if level == N:
        if ssum == M:
            print(' '.join(map(str,choice)))
        return
    # 가지치기
    if ssum + (N - level) * 6 < M or ssum > M:
        return

    for i in range(1, 7):
        choice[level] = i
        dice(level+1, ssum+i)
        choice[level] = 0

dice(0, 0)

def code_x():
    # permutation
    result = []
    answer = []
    #n = int(input())
    n = 3
    def permutation(start):
        if len(result) == n:
            answer.append(result)
            print(answer)
            return

        for i in range(start, n + 1):
            if i not in result:
                result.append(i)
                permutation(1)
                result.pop()

    permutation(1)

    print(answer)


code_x()