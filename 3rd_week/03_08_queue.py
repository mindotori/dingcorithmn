class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self): #큐는 양방향이라 head, tail 둘 다
        self.head = None
        self.tail = None

    def enqueue(self, value): #새로 들어오는게 있으니까 value가 있는 것임
        new_node = Node(value)
        if self.is_empty(): #비어 잇는 상태면 새로 들어오는게 head, tail 둘 다
            self.head = new_node
            self.tail = new_node
            return
        #비어있지 않은 경우
        self.tail.next = new_node # tail의 다음 값이 뉴 노드
        self.tail = new_node #새로 들어온 노드를 tail로 설정

    def dequeue(self): # 맨 앞에 있는 애가 빠져나감
        if self.is_empty():
            return "Queue is empty"

        delete_head = self.head # 삭제될 헤드에 현재 헤드 대입 (FIFO)
        self.head = self.head.next #삭제되니깐 다음 것이 헤드가 되어야함

        return delete_head

    def peek(self):
        if self.is_empty():
            return "Queue is empty"

        return self.head.data # 헤드만 반환

    def is_empty(self):
        return self.head is None

queue = Queue()
queue.enqueue(4)
print(queue.peek())
queue.enqueue(2)
print(queue.peek())
queue.enqueue(3)
print(queue.peek())

queue.dequeue()
print(queue.peek()) # 2
queue.dequeue()
print(queue.peek()) # 3
