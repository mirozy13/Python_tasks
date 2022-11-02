a = str('How are you? Eh, ok. Low or Lower? Ohhh.')


def message(s):
    res = ""
    for i in s:
        if i.isupper():
            res += i
    return res


print(message(a))
