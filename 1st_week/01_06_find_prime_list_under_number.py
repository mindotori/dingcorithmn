# for ~ else문: for반복 완료한 다음에 else문이 정상 호출된다.
# for문이 멈추게 된다면 else이하는 실행되지 않는다.

# 수학적 개념을 코드화 시켜야함

# 소수는 자기 자신과 1 외에는 아무 것도 나눌 수 없다.
input = 20


def find_prime_list_under_number(number):
    prime_list = []

    # 2~ 20까지 찾아서 이것들이 소수인가? 소수라면 prime_list에 넣어라
    for n in range(2, number + 1): # 2 ~ n까지의(n포함) 숫자들이 n에 들어가는 것을 반복한다.
        # n = 19
        # n = 19 / 2    19 / 3   19 / 4  19 / 5    19 / 6 ,,,, 19/18
        # n이 2랑 3으로 나눠 떨어지지 않는다면 6으로도 나눠 떨어지지 않음
        # 모든 수랑 비교할 필요 없이 소수들과만 비교하면 된다.
        # N의 제곱근보다 크지 않은 어떤 소수로도 나눠 떨어지지 않는다 ( i * i <=n )
        # for i in range(2, n): # 2부터 n-1까지를 i에 들어가는 것을 반복한다
        for i in prime_list:
            if i * i <= n and n % i == 0: # n이 i로 나누어 떨어지면 소수가 아님
                break
        else: # break안하면 else문 실행 (소수임)
            prime_list.append(n)
    return prime_list


result = find_prime_list_under_number(input)
print(result)