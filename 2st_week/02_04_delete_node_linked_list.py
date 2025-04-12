class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0

        while cur_index != index:
            cur = cur.next
            cur_index += 1

        return cur

    def add_node(self, index, value):
        new_node = Node(value)

        # 인덱스가 0일때는 과연 어떻게 될까? => 예외 처리
        # head 새로 만들기 : head -> prev.head
        if index == 0:
            new_node.next = self.head

            self.head = new_node
            return

        #index - 1번째의 노드가 필요하다.
        #넣고 싶은 위치의 "직전 노드"가 필요한 것임
        prev_node = self.get_node(index - 1)

        next_node = prev_node.next

        prev_node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):

        # Index 0일 경우 예외 처리
        if index == 0:
            self.head = self.head.next
            return

        # index - 1 번째 칸 우선 구할거임
        prev_node = self.get_node(index - 1)
        index_node = self.get_node(index)
        # prev_node가 next_node를 보게 함으로써 delete_node 구현 가능
        prev_node.next = index_node.next

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
# linked_list.print_all()
# [5] -> [12]
# 0번째 인덱스 : 5
# 1번째 인덱스 : 12
# [5]->[12]->[8]
linked_list.add_node(1,6) # 1번째 인덱스에 6을 넣어줌
# [5]->[6]->[12]->[8]

linked_list.add_node(0,7)
# linked_list.print_all()
# [7] -> [5]->[6]->[12]->[8]

linked_list.delete_node(1)
linked_list.print_all()
# [7] -> [6] -> [12] -> [8]

linked_list.delete_node(0)
linked_list.print_all()
# [6] -> [12] -> [8]