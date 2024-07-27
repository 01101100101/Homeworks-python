datalines = []
students_on_subjects = {}


try:
    with open('input.txt', 'r') as text_file:
        datalines = text_file.readlines()
except FileNotFoundError:
    print('File not found')
    exit()


for line in datalines:
    m = line.split(":")
    if len(m) != 2:
        print('Incorrect format of input file')
        exit()

    student = m[0].strip()
    if student == '':
        print('Incorrect name')
        exit()

    subjects = m[1].split(",")
    subjects = [u.strip() for u in subjects]

    for sub in subjects:
        if sub == '':
            continue
        if sub not in students_on_subjects:
            students_on_subjects[sub] = []
        if student not in students_on_subjects[sub]:
            students_on_subjects[sub].append(student)


n = input('Course name: ')
n = n.strip()

if n == '':
    print('incorrect name')
    exit()

if n not in students_on_subjects:
    print('no students on tish course')
    exit()

for student in students_on_subjects[n]:
    print(student)