# 백준 (에디터) - 1406
# https://www.acmicpc.net/problem/1406

import sys

sys.stdin = open('B_1406_input.txt', 'r')

# 커서를 왼쪽으로 한 칸 옮김
# 커서를 오른쪽으로 한 칸 옮김
# 커서 왼쪽에 있는 문자를 삭제
# 문자를 커서 왼쪽에 추가
import __pypy__

class NODE:
    def __init__(self, c=''):
        self.c = c
        self.prev = None
        self.next = None

# head - tail
# head 보다 앞에는 NODE 없음
# tail 보다 뒤에는 NODE 없음
# head, tail : 더미노드를 연결, 삽입과 삭제시 head, tail을 변경하지 않아도 되어 코드가 간결해 짐
# cursor : head 보다 뒤에 있어야 함 (head와 같을 수 없음, head.next 까지는 가능, 왼쪽에 삽입)
# cursor : tail 과 같을 수 있음
class Editor:
    def __init__(self):
        self.head = NODE()
        self.tail = NODE()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cursor = self.tail
        self.cnt = 0
    #  cursor.prev - cursor
    #  cursor.prev - new_node - cursor
    def insert_left(self, c):
        new_node = NODE(c[0])
        # new_node의 prev, next 채우기
        new_node.prev = self.cursor.prev
        new_node.next = self.cursor
        new_node.next.prev = new_node
        new_node.prev.next = new_node
        self.cnt += 1

    # p_node - n_node
    # p_node - new_node - n_node
    def insert_left_easy(self, c):
        new_node = NODE(c[0])
        p_node = self.cursor.prev
        n_node = self.cursor
        new_node.prev = p_node
        new_node.next = n_node
        p_node.next = new_node
        n_node.prev = new_node
        self.cnt += 1

    def move_left(self):
        if self.cursor == self.head.next: return
        self.cursor = self.cursor.prev

    def move_right(self):
        if self.cursor == self.tail: return
        self.cursor = self.cursor.next

    #  n_prev - del_node - cursor
    def delete_left(self):
        if self.cursor == self.head.next: return
        #if self.cnt == 0: return
        self.cnt -= 1
        del_node = self.cursor.prev
        n_prev = del_node.prev

        n_prev.next = self.cursor
        self.cursor.prev = n_prev

        # self.cursor.prev = self.cursor.prev.prev
        # self.cursor.prev.next = self.cursor

    def __str__(self):
        ans = __pypy__.builders.StringBuilder()
        curr = self.head.next
        while curr != self.tail:
            ans.append(curr.c)
            curr = curr.next
        return ans.build()


editor = Editor()
words = input()
for c in words:
    editor.insert_left(c)

M = int(input())
for _ in range(M):
    cmd, *args = input().split()
    if cmd == 'L':
        editor.move_left()
    elif cmd == 'D':
        editor.move_right()
    elif cmd == 'B':
        editor.delete_left()
    else:
        editor.insert_left(args)

print(editor)
