try:
    n = int(input('Print number of strings: '))
except ValueError:
    print('it is not a number')
    exit()
if n <= 0:
    print("your number is not integer")
    exit()

for i in range(1, n+1):
    print(' ' * (n-i), '*' * (i*2-1), sep='')

