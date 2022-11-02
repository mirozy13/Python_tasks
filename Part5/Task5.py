str1 = "start 5 one two three 7 end"
str2 = "1 2 3 4"


def check(three_words):
    count = 0
    for w in three_words.split():
        if w.isalpha():
            count += 1
        else:
            count = 0
        if count == 3:
            return True
    return False

x1 = check(str1)
x2 = check(str2)
print(x1)
print(x2)
