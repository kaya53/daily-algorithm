import sys
sys.stdin = open('input.txt')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


# 7개의 조합된 자리가 서로 인접한 지 확인하는 함수
def check(num):
    global available  # 연결 되면 1씩 올라감
    x = num // 5
    y = num % 5
    # 4 방향 탐색
    for t in range(4):
        nx = x + dx[t]
        ny = y + dy[t]
        # 범위를 벗어났거나 이미 방문한 자리라면
        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5 or isVisited[nx][ny]:
            continue
        # 위치를 기반으로 번호 만들어 냄
        nextNum = nx * 5 + ny
        # 그 번호가 조합 안에 있다면 재귀로 다음 번호 탐색
        if nextNum in p:
            isVisited[nx][ny] = True
            available += 1
            check(nextNum)


# 7자리의 조합을 구하는 함수
def dfs(depth, y_cnt, idx):
    global result, available, isVisited

    # '임도연'파가 4명 이상 이거나 탐색할 수 있는 남은 수가 남은 선택 수 보다 적다면 종료
    if y_cnt > 3 or 25 - idx < 7 - depth:
        return
    # 7개의 위치를 다 뽑았다면
    if depth == 7:
        # 연결됐는지 체크할 변수 초기화
        available = 1
        # 방문 체크할 배열 초기화
        isVisited = [[False for _ in range(5)] for _ in range(5)]
        # 만들어진 조합 중 첫번째 자리번호를 가지고 현재 조합이 모두 연결됐는지 확인
        x = p[0] // 5
        y = p[0] % 5
        isVisited[x][y] = True  # 현재 자리 방문 체크
        # 모두 연결됐는지 체크하는 함수
        check(p[0])
        # 가능한 자리 7개가 모두 연결됐다면 '칠공주' 결성 가능
        if available == 7:
            result += 1
        return

    x = idx // 5
    y = idx % 5
    # 현재 위치가 '임도연'파 라면
    if board[x][y] == 'Y':
        p.append(idx)
        dfs(depth + 1, y_cnt + 1, idx + 1)
        p.pop()
    # 현재 위치가 '이다솜'파 라면
    else:
        p.append(idx)
        dfs(depth + 1, y_cnt, idx + 1)
        p.pop()
    # 인덱스(자리 번호)만 1 올려서 다음 재귀로 넘김 -> 모든 조합 만들어보기 위해
    dfs(depth, y_cnt, idx + 1)


board = [list(input()) for _ in range(5)]  # 입력받은 원본 배열
isVisited = [[False for _ in range(5)] for _ in range(5)]  # 방문 체크할 배열
result = 0
p = []  # 자리 조합 저장할 배열
dfs(0, 0, 0)

print(result)