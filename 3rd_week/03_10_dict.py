
# put(key, value) -> dictionary에 key 해당하는 곳에 value를 저장하겠다
# get(key) -> dictionary에 key에 해당하는 value를 반환해라.

class Dict:
    def __init__(self):
        self.items = [None] * 8


# 1. Chaning 기법 : 충돌이 발생했을 때, 그 값들을 링크드 리스트로 관리한다.

    def put(self,key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]

my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))
