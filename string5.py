N = int(input())
result = "".join(chr(122 - i) for i in range(N))
print(result)
