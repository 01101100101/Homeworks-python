datalines = []
cities = {}

try:
    with open('cities.txt', 'r') as text_file:
        datalines = text_file.readlines()
except FileNotFoundError:
    print('File not found')
    exit()

for line in datalines:
    m = line.split(":")
    if len(m) != 2:
        print('Incorrect format of input file')
        exit()
    if m[0].strip() == '':
        print('Incorrect name')
        exit()
    try:
        cities[m[0].strip()] = int(m[1].strip())
    except ValueError:
        print('here is no mark')
        exit()

try:
    n = int(input('Print low limit of population: '))
except ValueError:
    print('it is not a number')
    exit()

list_of_cities = list(cities.keys())
list_of_cities.sort()

with open('filtered_cities.txt', 'w') as text_file:
    for city in list_of_cities:
        if cities[city] > n:
            text_file.write(city + ":" + str(cities[city]) + "\n")
