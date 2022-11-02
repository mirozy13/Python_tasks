x: str = input('Введите целое неотрицательное число : ')
x1: int = int(x)

if (x1 % 3 == 0) and (x1 % 5 == 0):
    print('Fizz Buzz')
elif x1 % 3 == 0:
    print('Fizz')
elif x1 % 5 == 0:
    print('Buzz')
else:
    print(x)