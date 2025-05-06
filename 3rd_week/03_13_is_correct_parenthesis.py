# 닫는 괄호가 나오면, 바로 직전에 열렸었던 괄호가 닫힌다.
# 열린 괄호가 나오면, 순서대로 쌓아서 저장해놔야되는구나.
# 닫힌 괄호가 나오면 제일 최신의 열린 괄호를 제거(pop)해서 짝을 맞춘다

# <스택>
# 순서대로 데이터를 쌓아놓고, 가장 마지막에 생긴 데이터가 먼저 빠져나가는 형태의 자료구조 (LIFO)

def is_correct_parenthesis(string):
    stack = [] # stack 빈 배열 선언
    for i in range(len(string)):
        if string[i] == "(":
            stack.append("(") # 열린 괄호는 스택에 추가
        elif string[i] == ")":
            if len(stack) == 0: #스택이 비어있다면, 닫을 괄호가 없는 상태 - False
                return False
            stack.pop() # 비어있지 않다면 pop() = 스택의 가장 최근의 열린 괄호를 제거 (마지막 열린 괄호 닫음)

    if len(stack) != 0: #모든 괄호가 닫히지 않고 열린 괄호가 남아있는 상황
        return False
    else: # 스택이 모두 비어있는 상태 (짝 맞춰서 pop된 상태 - 괄호가 올바르게 닫힌 것임)
        return True

print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))