class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

linked_tuple = LinkedTuple()

linked_tuple.add("333", 7)
linked_tuple.add("77", 6)

print(linked_tuple.items)

print(linked_tuple.get("333"))

class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple)


    def put(self,key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value) # index 번째의 LinkedTuple [(key, value)]
                                             #한번 더 호출되면?
                                          # index 번째의 LinkedTuple [(key,value), (key2, value2)] - 링크드 리스트 형태로 구성

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key) # LinkedTuple

my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))
