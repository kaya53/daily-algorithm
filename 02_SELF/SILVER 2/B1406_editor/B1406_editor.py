import sys

# sys.stdin = open('input.txt')

input = sys.stdin.readline

# for _ in range(3):
char = list(input().rstrip())
m = int(input().rstrip())
after = []
for _ in range(m):
    inp = list(input().rstrip().split())
    if inp[0] == 'P':
        char.append(inp[1])
    elif inp[0] == 'L':
        if not char: continue
        after.append(char.pop())
    elif inp[0] == 'D':
        if not after: continue
        char.append(after.pop())
    elif inp[0] == 'B':
        if not char: continue
        char.pop()

print(''.join(char)+''.join(after[::-1]))


