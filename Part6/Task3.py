def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5 + 1)):
        if x % i == 0:
            return False
    else:
        return True


print(is_prime(int(input())))