def season(moth):

    if month == 12 or month < 3:
        return "Зима"
    elif month == 3 or month < 6:
        return "Весна"
    elif month == 6 or month < 9:
        return "Лето"
    else:
        return "Осень"


month = input("Введите номер месяца от 1 до 12:")
month = int(month)
answer = season(month)
print(month)