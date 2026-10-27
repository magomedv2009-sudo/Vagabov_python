N = int(input())
C1 = input()
C2 = input()
result = (C1 + C2) * (N // 2)
if N % 2 != 0:
    result += C1
print(result)
