lst = [8, 1, 0, 4]


def reverse_list(lst, n=0):
    if len(lst) <= 1:
        return lst
    lst[n], lst[-n - 1] = lst[-n - 1], lst[n]
    if n + 1 != int(len(lst) / 2):
        return reverse_list(lst, n + 1)
    return lst


print(reverse_list(lst))