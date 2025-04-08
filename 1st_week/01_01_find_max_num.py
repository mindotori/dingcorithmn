def find_max_num(array): #배열을 입력값으로 받고 있는 상태
   #방법1 (이중포문)
    # for number in array:
    #     is_max_num = True # flag 변수
    #     for compare_number in array:
    #         if number < compare_number:
    #             is_max_num = False
    #     if is_max_num:
    #         return number

  #방법2: 하나의 변수를 잡아서 그 변수와 비교하여 가장 큰 수를 찾는 방법(초기 변수 설정)
    max_number = array[0]

    for number in array:
        if number > max_number:
            max_number = number
    return max_number



print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))