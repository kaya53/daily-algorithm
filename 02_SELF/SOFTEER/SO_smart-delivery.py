# 그리디

# 틀린 이유
# - get_value 함수에서 for문 range 설정 오류
# 처음엔 이렇게 했었다
# for d in [-1, 1]:
#     for dist in range(K, 0, -1):
# 이렇게 하면 
# ci-K, ci-K+1, ci-K+2, .... ci-1 => 여기까진 괜찮은데 그 다음이
# ci+ K, ci+K-1,...., ci+1 => 이런 순서로 간다
# 이렇게 되면 안되고 ci-K부터 ci+K까지 연속적으로 증가하도록 되어야 답이 정상적으로 나온다


def get_value(ci):
    for v in range(ci - K, ci + K + 1):
        if v < 0 or v >= N or line[v] == 'P' or check[v]: continue
        check[v] = 1
        return 1
    return 0


N, K = map(int, input().split())
line = list(input())

cnt = 0
check = [0] * N
for i in range(N):
    if line[i] == 'H': continue
    cnt += get_value(i)

print(cnt)