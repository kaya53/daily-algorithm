import sys

sys.stdin = open('input.txt')

for _ in range(10):
    now = 1  # 현재 줄 시작 수
    line = 1  # 현재 줄
    iinput = int(sys.stdin.readline().rstrip())

    # 입력 값이 몇번째 줄에 있는 것인지 판별
    while True:
        if now + line > iinput:
            break
        now += line
        line += 1
    # print(iinput, now, line)

    # 짝수 줄 => 분모 내림차순, 홀수줄 => 분모 오름차순
    under = iinput - now + 1
    top = line + 1 - under

    if not (line % 2):
        under, top = top, under
    print(f'{top}/{under}')
