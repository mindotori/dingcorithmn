# 회문 = 펠린드롬
input = "abcba"

# 맨 처음 맨 마지막 / 두번째 맨 뒤 두번째 같아야함 / 가운데는 상관 무
# 문자열 길이 구하기
# 문자열의 길이만큼 반복
def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n - 1  - i]:
            return False
    return True


print(is_palindrome(input))