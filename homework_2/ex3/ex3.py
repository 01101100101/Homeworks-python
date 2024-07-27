def read_file(file_name):
    try:
        with open(file_name, 'r') as text_file:
            datalines = text_file.readlines()
    except FileNotFoundError:
        print('File not found')
        exit()
    return datalines


data_lines_1 = read_file('input1.txt')
data_lines_2 = read_file('input2.txt')

data_of_all_lines = data_lines_1 + data_lines_2
data_of_all_lines.sort()

with open('output.txt', 'w') as text_file:
    for line in data_of_all_lines:
        text_file.write(line.strip('\n') + '\n')
