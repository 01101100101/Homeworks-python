def read_file(file_name):
    try:
        with open(file_name, 'r') as text_file:
            datalines = text_file.readlines()
    except FileNotFoundError:
        print('File not found')
        exit()
    return datalines


results = []

brackets_open = "({<["
brackets_close = ")}>]"
brackets = brackets_open + brackets_close
#print(brackets)
brackets_close_open = dict(zip(brackets_open, brackets_close))
#print(brackets_close_open)


def format_string(s):
    s_format = ''
    for symbol in s:
        if symbol in brackets:
            s_format += symbol
    return s_format


def check_line(l):
    brackets_stack = []
    for symbol in l:
        if symbol in brackets_open:
            brackets_stack.append(symbol)
        if symbol in brackets_close:
            if len(brackets_stack) == 0:
                return False
            expected_opened = brackets_stack.pop(-1)
            if brackets_close_open[expected_opened] != symbol:
                return False
    if len(brackets_stack) != 0:
        return False
    return True


read_lines = read_file('input.txt')
for line in read_lines:
    results.append(check_line(format_string(line)))


with open('output.txt', 'w') as text_file:
    for line in results:
        text_file.write(str(line) + '\n')
