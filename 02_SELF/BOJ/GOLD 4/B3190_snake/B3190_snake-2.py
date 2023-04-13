import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')


def move():
    # 몸길이 한칸 늘리기
    ci, cj = snake[-1]
    ni, nj = ci + delta[sd][0], cj + delta[sd][1]
    if ni < 0 or ni >= N or nj < 0 or nj >= N or (ni, nj) in snake:
        return False
    snake.append((ni, nj))

    # 사과 체크
    if apple.get((ni, nj), -1) <= 0: # 사과 x
        snake.pop(0)
    elif apple.get((ni, nj), -1) == 1:  # 사과 o:
        apple[(ni, nj)] = 0
    return True


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# for _ in range(3):
N = int(input())
K = int(input())
apple = {}
for _ in range(K):
    y, x = map(lambda x: int(x)-1, input().split())
    apple[(y, x)] = 1
L = int(input())
change = {}
for _ in range(L):
    t, d = input().split()
    change[int(t)] = d

si, sj, sd = 0, 0, 1  # 오른쪽 방향으로 시작
snake = [(si, sj)]  # 초기 뱀의 상태
time = 0
while True:
    time += 1
    if not move():
        print(time)
        break
    if change.get(time, -1) == 'L':
        sd = (sd - 1) % 4
    elif change.get(time, -1) == 'D':
        sd = (sd + 1) % 4
