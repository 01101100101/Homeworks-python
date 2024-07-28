# кузнечик прыгает на 1 или на 2 метра, сколько способов пропрыгать n метров

hd = {0:0, 1:1, 2:2}


def grasshopper(x):
    if x not in hd:
        hd[x] = grasshopper(x - 1) + grasshopper(x - 2)
    return hd[x]


try:
    n = int(input('Print n: '))
except ValueError:
    print('it is not a number')
    exit()
if n <= 0:
    print("your number is not integer")
    exit()

print(grasshopper(n))
