input = "011110"

# 0에서 1을 마주쳤을 때 뒤집는다 -> 전체를 0으로 만들기 위한 작업
# 1에서 0을 마주쳤을 때 뒤집는다 -> 전체를 1으로 만들기 위한 작업

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    # 맨 앞 숫자 0인지 1인지도 고려해야함
    if string[0] == '0':
        count_to_all_one += 1  # 0을 1로 뒤집
    elif string[0] == '1':
        count_to_all_zero += 1 # 1을 0으로 뒤집

    for i in range(len(string) - 1): # i는 0부터 문자열의 길이 -2 까지가 됩니다. (인덱스 기준)
        if string[i] != string[i + 1]: # 현재 인덱스가 다음에 있는 인덱스와 다르다면 (뒤집어야 하는 포인트)
            if string[i + 1] == "1":
                count_to_all_zero += 1
            if string[i + 1] == "0":
                count_to_all_one += 1
    print(count_to_all_zero, count_to_all_one)
    return min(count_to_all_zero, count_to_all_one) # 최솟값 반환 내장함수


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)