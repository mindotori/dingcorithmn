all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

#푸는 방식 3가지
# 1. 2중 반복문 -> O(N^2)
#     for student in all_students: O(N)
#         is_present = False
#         for present_student in present_students: O(N)
#             is_present = True
#         if not is_present:
#             return student
# 2. 정렬
#   O(NlogN)

# 3. Dictionary, Hash table O(N+N) = O(N)
#    O(N) * 1
#     all_students를 돌면서, hash table의 키 값에 해당하는 학생들을 등록한다.
#     present_students를 돌면서 hash table의 키값의 값을 제거한다.
#     그리고 나서는 남아있는 hash table의 키 값에 해당하는 학생이 결석한 학생이다.

def get_absent_student(all_array, present_array):
    dict = {} #비어있는 딕셔너리 선언  = 딕셔너리는 {}로 선언해야함
    for student in all_array: #전체 학생 명단에 있는 학생들을 딕셔너리에 등록
        dict[student] = True # 딕셔너리에서 []는 key를 이용한 접근

    for present_student in present_array: #출석한 학생들 키값 제거
        del dict[present_student] #키 값 제거

    # 남아있는 키값(결석한 학생)만 반환
    for key in dict.keys(): #keys() = 딕셔너리의 모든 키값들을 모아서 반환해주는 메서드
        return key # 하나 반환하고 종료 (결석 학생이 여러명이면 불가능)



print(get_absent_student(all_students, present_students))

print("정답 = 예지 / 현재 풀이 값 = ",get_absent_student(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
print("정답 = RM / 현재 풀이 값 = ",get_absent_student(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))