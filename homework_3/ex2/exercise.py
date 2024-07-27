import json

try:
    with open('input.txt', 'r') as text_file:
        data = json.load(text_file)
except FileNotFoundError:
    print('File not found')
    exit()
except json.decoder.JSONDecodeError:
    print('it is not json dict')
    exit()

storage = {}

for magazine in data:
    for food in data[magazine]:
        if food not in storage:
            storage[food] = data[magazine][food]
        else:
            storage[food] += data[magazine][food]

with open('output.txt', 'w') as text_file:
    text_file.write(json.dumps(storage, indent=4))
