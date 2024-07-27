datalines = []
students = {}

try:
    with open('input.txt', 'r') as text_file:
        datalines = text_file.readlines()
except FileNotFoundError:
    print('File not found')
    exit()

for line in datalines:
    m = line.split(",")
    if len(m) != 2:
        print('Incorrect format of input file')
        exit()
    if m[0].strip() == '':
        print('Incorrect name')
        exit()
    try:
        students[m[0].strip()] = int(m[1].strip())
    except ValueError:
        print('here is no mark')
        exit()

s = 0
i = 0
for student in students:
    s += students[student]
    i += 1
s = int(s/i)

with open('output.txt', 'w') as text_file:
    for student in students:
        if students[student] >= s:
            text_file.write(student + "\n")
