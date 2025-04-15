#재귀함수를 통해서 펠림드롬인지 아닌지 구할 수 있다.
#재귀함수: 문제의 범위를 조금씩 좁혀나가는 것임
input = "abcba"

# 가운데 한글자일 경우에는 회문일지 따질 필요 없이 True다
def is_palindrome(string):

    if string[0] != string[-1]: # 맨 앞 글자랑 맨 뒤 글자가 다르면 False 반환
        return False
    if len(string) <=1:
        return True

    return is_palindrome(string[1:-1]) # 1번째 인덱스부터 -1번째 인덱스까지 문자열을 자르겠다



print(is_palindrome(input))