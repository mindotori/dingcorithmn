def find_max_plus_or_multiply(array):
    plus_or_multiply_sum = 0 #결과 저장 변수
    for number in array:
        if number <= 1 or plus_or_multiply_sum <= 1:
            plus_or_multiply_sum += number
        else:
            plus_or_multiply_sum *= number
    return plus_or_multiply_sum
 # 시간 복잡도: for문이 한 번 나왔으니까 입력값의 길이인 N번만큼은 반복한다
 # O(N)


result = find_max_plus_or_multiply #함수 할당
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))