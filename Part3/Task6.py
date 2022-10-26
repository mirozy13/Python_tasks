from random import randint

n = (randint(100, 1000))
print("Число:", n)
mult = 1
while n > 0:
    a = n % 10
    if a != 0:
        mult *= a
    n = n // 10
print("Произведение цифр:", mult)