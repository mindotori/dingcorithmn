def find_max_occurred_alphabet(string):
    # 알파벳의 빈도수를 저장한 배열을 만든다.
    # 그리고 문자열을 돌면서 해당 문자가 알파벳이라면, 알파벳을 인덱스화 시켜서 알파벳의 빈도수를 업데이트 한다.

    alphabet_occurence_array = [0] * 26 # 알파벳 배열 설정

    for char in string:
        if not char.isalpha(): #알파벳인지 아닌지 검사
            continue
        arr_index = ord(char) - ord('a') # 해당 문자를 인덱스로 치환
        alphabet_occurence_array[arr_index] += 1 # 빈도수 배열에 인덱스로 찾아가서 해당 값을 추가해준다.

    max_occurrence = 0
    max_alphabet_index = 0

    for index in range(len(alphabet_occurence_array)): #배열의 길이만큼 순회
        alphabet_occurrence = alphabet_occurence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index
        #인덱스를 -> 아스키코드로 만들고 -> 알파벳으로 변환해야함
    return chr(max_alphabet_index + ord('a'))



def find_alphabet_occurence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():  # str.is_alpha() : 해당 문자열이 알파벳인지 확인
            continue
        arr_index = ord(char) - ord('a') # a의 아스키 97 빼준다
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))

# 알파벳을 아스키코드값으로 바꾸고 -97 해준다
# 97 = 'a'
# 알파벳은 총 26개 => 26짜리 배열 생성