class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(3)
print(node.data, node.next)

next_node = Node(3)
node.next = next_node



class LinkedList:
    def __init__(self, value):
        self.head = Node(value) # head에 시작하는 Node를 연결한다

    # LinkedList의 가장 끝에 있는 노드에 새로운 노드를 연결해줘 => append 메서드
    def append(self, value): #LinkedList 가장 끝에 있는 노드에 새로운 노드를 연결한다
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

   # linked_list 에서 저장한 head를 따라가면서 현재 있는 노드들을 전부 출력해주는 함수
    def print_all(self):
        cur = self.head
        while cur is not None: #current node가 none이 아닐때까지 반복
            print(cur.data)
            cur = cur.next


linked_list = LinkedList(5)
print(linked_list.head.data)

linked_list.append(12)

linked_list.append(8)
linked_list.print_all()

