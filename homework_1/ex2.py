try:
    n = int(input('Print number from 1 to 999: '))
except ValueError:
    print('it is not a number')
    exit()
if n < 1 or n > 999:
    print("your number is not correct")
    exit()

number = []

hundreds = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот",
            "семьсот", "восемьсот", "девятьсот"]

if n > 99:
    h = int(n / 100)
    number.append(hundreds[h - 1])
    n = n - h * 100

decimals = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят",
            "семьдесят", "восемьдесят", "девяносто"]

if n > 19:
    d = int(n / 10)
    number.append(decimals[d - 2])
    n = n - d * 10

tails = ["один", "два", "три", "четыре", "пять", "шесть",
         "семь", "восемь", "девять", "десять", "одиннадцать",
         "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
         "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
if n != 0:
    number.append(tails[n - 1])

print(*number, sep=" ")
