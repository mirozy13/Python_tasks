def reverse(x):
    if x >= 0:
        number = int(str(x)[::-1])
    else:
        number = -int(str(-x)[::-1])
        return number
print(reverse(-76434674846508))