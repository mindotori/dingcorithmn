finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# 존재하면 True, 존재하지 않으면 False

# 이진 탐색
# => 찾고자 하는 범위가 탐색을 통해 줄어든다
# (배열[0] + 배열[len(배열) - 1]) // 2
def is_existing_target_number_binary(target, array):
    current_min = 0 # 0번째 인덱스
    current_max = len(array) - 1 # 맨 끝 인덱스 (인덱스는 0번부터니까)
    current_guess = (current_min + current_max) // 2   #(나머지 버림) => 얘를 인덱스로
    # ㄴ 탐색하는 값
    while current_min <= current_max: # 최소랑 최대가 같거나 작을 때까지 반복
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target: # Up : 최소 인덱스가 올라가야함
            current_min = current_guess + 1
        else: # Down : 탐색 인덱스가 줄어야함
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2 # 줄어든 범위에서 다음 설정할 값을 설정해야함

    return False

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)