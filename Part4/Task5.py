def reverse(x):
    if x >= 0:
        number = int(str(x)[::-1])
    else:
        number = -int(str(-x)[::-1])
    if -2**31 <= number <= 2**31 - 1:
        return number
    else:
        return 0
print(reverse(-76434))