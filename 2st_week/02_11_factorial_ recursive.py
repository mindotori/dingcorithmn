# 3! = 3 * 2 * 1

# factorial(n) = n * factorial(n-1)
# factorial(n - 1) = (n - 1) * factorial(n-2)

def factorial(n):
    if n == 1:
        return 1 # 탈출조건

    return n * factorial(n - 1)


print(factorial(5)) # 5*4*3*2*1