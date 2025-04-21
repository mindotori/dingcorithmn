class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # 처음엔 연결된 노드가 없으니까 None으로 시작
        # [ data | next ]


class LinkedList:
    def __init__(self, value):
        self.head = Node(value) # self.head = 링크드 리스트의 시작 지점

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

def get_single_linked_list_sum(liked_list):
    sum = 0
    cur = liked_list.head
    while cur is not None:
        sum = sum * 10 + cur.data
        cur = cur.next
    return sum


def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_1 = get_single_linked_list_sum(linked_list_1)
    sum_2 = get_single_linked_list_sum(linked_list_2)

    return sum_1 + sum_2


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)
# head
# cur
# sum_1 = 6
# [6] -> [7] -> [8]
# sum+1 = 6 * 10 + 7 = 67
# sum_1 = 67 * 10 + 8 = 678
linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)
# [3] -> [5] -> [4]

print(get_linked_list_sum(linked_list_1, linked_list_2))