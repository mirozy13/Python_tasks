from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)


print("x1=", end='')
x1 = float(input())
print("y1=", end='')
y1 = float(input())
print("x2=", end='')
x2 = float(input())
print("y2=", end='')
y2 = float(input())

print(distance(x1, y1, x2, y2))