N = int(input())

quotient = N // 4
remainder = N % 4

result = "long " * quotient + "int"

if remainder > 0:
    result = "long " + result

print(result)
