try:
    x = int(input('Print x: '))
    y = int(input('Print y: '))
except ValueError:
    print('it is not a number')
    exit()
if x < 0 or y < 0 and x * y != 0:
    print("your numbers is not good")
    exit()


def alg_euclid(a, b):
    if b == 0:
        return a
    q = (a // b)
    r = a - q * b
    if r == 0:
        return b
    return alg_euclid(b, r)


if x > y:
    print(alg_euclid(x, y))
else:
    print(alg_euclid(y, x))
