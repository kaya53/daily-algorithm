import sys

sys.stdin = open('input.txt')


def backtrack(idx):
    # 종료 조건: 부등호 개수를 맞게 숫자를 다 채웠을 때
    if idx == n+1:
        if res[0]: res[1] = ''.join(map(str, choice))
        else:
            res[0] = ''.join(map(str, choice))
        return
    for num in range(10):  # 숫자를 고른다.
        if visited[num]: continue
        if idx == 0:
            choice[idx] = num
            visited[num] = 1
        else:
            if infos[idx-1] == '>':
                if choice[idx-1] > num:
                    choice[idx] = num
                    visited[num] = 1
                else: continue  # 숫자를 찾기 전까지 다음 재귀로 넘어가지 않게
            elif infos[idx-1] == '<':
                if choice[idx-1] < num:
                    choice[idx] = num
                    visited[num] = 1
                else: continue
        backtrack(idx+1)
        visited[num] = 0
        # choice[idx] = -1


n = int(input())
infos = list(input().split())

choice = [-1] * (n+1)  # 숫자를 채워따!
visited = [0] * 10
res = [[], []]
backtrack(0)
print(res[1], res[0], sep='\n')
