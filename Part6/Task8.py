def more_than_five(lst):
    new_lst = []
    for number in lst:
        if abs(number) > 10:
            new_lst.append(number)
    return new_lst


print(more_than_five([-10, 12, -1, 0, 600,-99]))