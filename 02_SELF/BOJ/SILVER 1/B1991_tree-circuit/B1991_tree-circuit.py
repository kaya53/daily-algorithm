import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline

def pre(start):
    if node_info[start] == ['.', '.']:
        print(start, end='')
        return

    print(start, end='')
    nnext1, nnext2 = node_info[start]
    if nnext1 != '.': pre(nnext1)
    if nnext2 != '.': pre(nnext2)


def mid(start):
    if node_info[start] == ['.', '.']:
        print(start, end='')
        return

    nnext1, nnext2 = node_info[start]
    if nnext1 != '.': mid(nnext1)
    print(start, end='')
    if nnext2 != '.': mid(nnext2)


def post(start):
    if node_info[start] == ['.', '.']:
        print(start, end='')
        return

    nnext1, nnext2 = node_info[start]
    if nnext1 != '.': post(nnext1)
    if nnext2 != '.': post(nnext2)
    print(start, end='')


n = int(input())
node_info = {}
for _ in range(n):
    par, *child = input().split()
    node_info[par] = child

pre('A')
print()
mid('A')
print()
post('A')

