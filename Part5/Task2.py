x: str = input('Введите целое число : ')
x1: int = int(x)

if x1 % 2 != 0:
    print('Плохо')
elif (x1 % 2 == 0) and (2 <= x1 <= 5):
    print("Неплохо")
elif (x1 % 2 == 0) and (6 <= x1 <= 20):
    print("Так себе")
elif (x1 % 2 == 0) and (x1 > 20):
    print("Отлично")