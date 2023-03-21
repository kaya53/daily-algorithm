import sys

input = sys.stdin.readline

class NODE:
    def __init__(self, name=''):
        self.name = name
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = NODE()
        self.tail = NODE()
        self.tail.prev = self.head
        self.head.next = self.tail
        self.cursor = self.tail

    def insert_node(self, new_node):
        new = NODE(new_node)
        prev_node = self.cursor.prev
        next_node = self.cursor
        new.prev = prev_node
        new.next = next_node
        new.next.prev = new
        new.prev.next = new

    def cursor_left(self):
        if self.cursor == self.head.next: return
        self.cursor = self.cursor.prev

    def cursor_right(self):
        if self.cursor == self.tail: return
        self.cursor = self.cursor.next

    def delete_left(self):
        if self.cursor == self.head.next: return
        del_node = self.cursor.prev
        n_prev = del_node.prev
        n_prev.next = self.cursor
        self.cursor.prev = n_prev

    def __str__(self):
        ans = []
        now = self.head.next
        while now != self.tail:
            ans.append(now.name)
            now = now.next
        return ''.join(map(str, ans))


# 초기 설정
editor = DLL()
for k in input().rstrip():
    editor.insert_node(k)

for _ in range(int(input())):
    inp = input().split()
    if inp[0] == 'L':
        editor.cursor_left()
    elif inp[0] == 'D':
        editor.cursor_right()
    elif inp[0] == 'B':
        editor.delete_left()
    else:
        editor.insert_node(inp[1])

print(editor)


