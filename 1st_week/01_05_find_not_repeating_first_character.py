input = "abadabac"

# 시간복잡도: O(N)
def find_not_repeating_first_character(string):
    # 반복되지 않는 첫번째 알파벳
    # 반복되는지 아닌지를 판단해야 함
    # alphabet_occurrence_array
    # string에서 알파벳의 빈도수를 찾는다.
    alphabet_occurrence_array = [0] * 26
    # 그리고 빈도수가 1인 알파벳들 중에서 string에서 뭐가 먼저 나왔는지를 찾아본다.
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = [] # 빈도수가 1인 알파벳들을 담아두는 변수
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence == 1: # 1이면 반복하지 않는 숫자
            not_repeating_character_array.append(chr(index + ord("a")))
    print(not_repeating_character_array)

    for char in string:
        if char in not_repeating_character_array:
            return char
    return "_"


result = find_not_repeating_first_character # result에 함수 할당
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))