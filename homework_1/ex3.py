try:
    n = int(input('Print number: '))
except ValueError:
    print('it is not a number')
    exit()
if n < 0:
    n = -n

while n > 9:
    s = 0
    for i in str(n):
        s += int(i)
    n = s
else:
    print(n)
