# 1406 에디터
# 단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.
# 이렇게 특정 위치에서 시작할 때 연결 리스트가 적합함

class DLL_NODE:
    def __init__(self, c=''):  # 인스턴스가 반드시 해야하는 일을 정의하는 함수; self => instance
        self.c = c
        self.prev_node = None
        self.next_node = None

    def __str__(self):
        return self.c

    # def __add__(self, other):
    #     return self.c + other.c
    

class DLL: 
    def __init__(self):
        # 맨 앞과 맨 뒤로 접근/삽입삭제를 쉽게 하기 위해 생성함
        self.head = DLL_NODE()
        self.tail = DLL_NODE()

        # 앞-뒤를 서로 연결
        self.head.next_node = self.tail
        self.tail.prev_node = self.head
        self.cursor = self.tail

    # 커서의 왼쪽에 새로운 노드 삽입
    def insert_left(self, c):
        new_node = DLL_NODE(c)  # 새로운 노드 생성
        prev = self.cursor.prev_node
        new_node.prev_node = prev
        new_node.next_node = self.cursor
        # new node가 끼기 전에 앞뒤에 있던 애들 간의 연결 관계를 끊고, new_node와의 연결 관계로 바꾸기
        new_node.prev_node.next_node = new_node
        self.cursor.prev_node = new_node
        self.print_info()

    def move_left(self):
        # if self.cursor != self.head:  # 커서는 헤드까지 가져가지 않을 것
        prev = self.cursor.prev_node
        if prev is self.head: return
        self.cursor = prev  # 커서를 왼쪽으로 한 칸

    def move_right(self):
        nnext = self.cursor.next_node
        if nnext is None: return
        self.cursor = nnext


    def print_info(self):
        cur = self.head.next_node
        while cur.next_node != self.tail:
            print(cur.c, end=' ')
            cur = cur.next_node
        print()
    
    # 커서

a = DLL_NODE('a')
b = DLL_NODE('b')
c = DLL_NODE('c')
print(a, b, c)
# print(a+b)  # TypeError: unsupported operand type(s) for +: 'DLL_NODE' and 'DLL_NODE'
# print(a+b)  # 클래스에__add__ 설정 후; ab

# a, b, c를 연결해보기
a.next_node = b
print(a.next_node)
b.next_node = c
c.prev_node = b
b.prev_node = a
print(c, c.prev_node, c.prev_node.prev_node)
print(b.prev_node.next_node)  # 앞으로 갔다가 다시 뒤로 => 자기 자신

# linked list에서 하지 말아야 할 것 => 처음부터 끝까지 순회하는 것
# a와 연결된 모든 노드 찾기
cur = a
while cur is not None:
    print(cur, end=' ')  # a b c
    cur = cur.next_node

# c와 연결된 모든 노드 찾기 -> 역순으로
curr = c
while curr is not None:
    print(curr, end=' ')  # c b a
    curr = curr.prev_node

# print()
editor = DLL()
editor.insert_left('A')
editor.insert_left('B')
editor.insert_left('C')
editor.print_info()
