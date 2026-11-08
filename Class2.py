class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def shift(self, dx, dy):
        self.x += dx
        self.y += dy

x = int(input())
y = int(input())
p = Point(x, y)

# Читаем сдвиги
dx = int(input())
dy = int(input())

p.shift(dx, dy)
print(p.x)
print(p.y)
