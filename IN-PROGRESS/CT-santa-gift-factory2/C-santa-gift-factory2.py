import sys

sys.stdin = open('input.txt')

class Gift:
    def __init__(self, p_num=''):
        self.p_num = p_num
        self.prev = None
        self.next = None

class Belt:
    def __init__(self, b_num):
        self.b_num = b_num
        self.head = Gift()
        self.tail = Gift()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cnt = 0

    def insert_gift(self, p_num):
        now_gift = Gift(p_num)
        prev_gift = self.tail.prev
        prev_gift.next = now_gift
        self.tail.prev = now_gift
        now_gift.next = self.tail
        now_gift.prev = prev_gift
        self.cnt += 1  # 선물 개수 증가

    def move_gift(self, dst):
        m_src = belt[self.b_num]
        m_dst = belt[dst]
        if m_src.head.next == m_src.tail: return
        src_cnt = m_src.cnt
        # 꼬리와 머리 연결
        src_first = m_src.head.next
        src_last = m_src.tail.prev
        n_node = m_dst.head.next

        m_dst.head.next = src_first
        n_node.prev = src_last
        src_first.prev = m_dst.head
        src_last.next = n_node
        # src 비우기
        m_src.head.next = m_src.tail
        m_src.tail.prev = m_src.head
        # 카운트 갱신
        self.cnt = 0
        m_dst.cnt += src_cnt
        return m_dst.cnt

    def change_gift(self, dst):
        m_src = belt[self.b_num]
        m_dst = belt[dst]
        src_head = m_src.head.next
        dst_head = m_dst.head.next
        src_next = src_head.next
        dst_next = dst_head.next
        # print(src_next, dst_next.p_num)
        # 일단 지우기
        m_src.head.next = src_next
        src_next.prev = m_src.head
        m_dst.head.next = dst_next
        dst_next.prev = m_dst.head
        print(m_src, m_dst)
        # 집어 넣기
        m_src.head.next = dst_head
        dst_head.next = src_next
        m_dst.head.next = src_head
        src_head.next = dst_next
        if src_head.p_num and not dst_head.p_num:
            m_src.cnt -= 1
        elif not src_head.p_num and dst_head.p_num:
            m_dst.cnt -= 1
        print(m_src, m_dst, m_src.head.next.p_num, m_dst.head.next.p_num)
        return m_dst.cnt


    def divide_gift(self, dst):
        if self.cnt == 1: return
        src = belt[self.b_num]
        floor_cnt = self.cnt // 2
        start = src.head.next  # 시작점
        end = start  # 끝점
        now_cnt = 1
        while now_cnt < floor_cnt:
            end = end.next
            now_cnt += 1
        print()
        # 시작점부터 끝점까지 dst 벨트에 붙이기
    

    def get_gift_num(self):
        pass

    def get_belt_num(self, b_num):
        now = belt[b_num]
        head_no = now.head.next
        tail_no = now.tail.prev
        now_cnt = now.cnt
        if not head_no.p_num: head_no = -1
        if not tail_no.p_num: tail_no = -1
        return head_no + (2*tail_no) + (3*now_cnt)

    def __str__(self):
        # return self.b_num
        ans = []
        now = self.head.next
        while now != None:
            ans.append(now.p_num)
            now = now.next
        return ''.join(map(str, ans))


q = int(input())
ans = []
for _ in range(q):
    inp = list(map(int, input().split()))
    if inp[0] == 100:
        n, m, gift_ls = inp[1], inp[2], inp[3:]
        belt = [0] * (n+1)
        # 벨트 만들기
        for b in range(1, n+1):
            belt[b] = Belt(b)
        # 선물 집어넣기
        for p_no, b_no in enumerate(gift_ls, start=1):
            belt[b_no].insert_gift(p_no)

    elif inp[0] == 200:
        m_src, m_dst = inp[1], inp[2]
        res = belt[m_src].move_gift(m_dst)
        ans.append(res)

    elif inp[0] == 300:
        m_src, m_dst = inp[1], inp[2]
        res = belt[m_src].change_gift(m_dst)
        ans.append(res)

    elif inp[0] == 400:
        m_src, m_dst = inp[1], inp[2]
        belt[m_src].divide_gift(m_dst)

    elif inp[0] == 500:
        p_num = inp[1]

    else:
        b_num = inp[1]


