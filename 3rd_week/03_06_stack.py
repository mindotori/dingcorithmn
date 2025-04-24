class Node:
    def __init__(self, data):
        self.data = data # 여기서 self.data 처음 만드는거임
        self.next = None # self.next도 이 시점에서 처음 만드는 거임

# 스택: 한 곳에서만 자료를 넣고 뺄 수 있다
# LIFO -> Last in first out. 가장 마지막에 넣은게 제일 빨리 나온다.
class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value) # 새 노드 하나 만들어
        new_head.next = self.head # 다음 값을 현재 헤드로 만들어 줌
        self.head = new_head # 이제 head를 새 노드로 바꿈

    # pop 기능 구현 : 단순히 값을 빼는게 아니라 빼서 반환을 해줘야함.
    # 현재에 있는 헤드를 없애고 그 다음에 있는 노드를 헤드로 만들면 된다
    def pop(self):
        #비어 있을 경우 예외 처리
        if self.is_empty():
            print("stack is Empty")

        delete_head = self.head # 제거할 값 반환하기 위해 저장
        self.head = self.head.next
        return delete_head


    def peek(self):
        if self.is_empty():
            return "stack is Empty"

        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None

stack = Stack()
stack.push(4)
print(stack.peek())

stack.push(3)
print(stack.peek())

stack.push(5)
print(stack.peek())

stack.pop()
print(stack.peek())

stack.pop()
print(stack.peek())

stack.pop()
print(stack.peek())
