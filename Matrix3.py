m = int(input())
n = int(input())
values = [int(x) for x in input().split()]
a = []

for i in range(m):
    row = [values[i]] * n
    a.append(row)

for row in a:
    print(row)
