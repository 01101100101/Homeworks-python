datalines = []

try:
    with open('input.txt', 'r') as text_file:
        datalines = text_file.readlines()
except FileNotFoundError:
    print('File not found')
    exit()

string_edit = input('Print edit for strings: ')


def logic(line1, se):
    se = se + ';' + '\n'
    line1 = line1.rstrip(se)
    return line1[::-1]


with open('output.txt', 'w') as text_file:
    for line in datalines:
        text_file.write(logic(line, string_edit) + "\n")
