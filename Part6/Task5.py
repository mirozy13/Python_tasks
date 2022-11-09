a = 'Привет мир'

result = ''
for i, s in enumerate(a):
    if i >=4 and i<9:
        result += s.upper()
    else:
        result += s

print(result)