def write(file, data):
    f = open(file, 'a')
    for line in data:
        if not line.endswith('\n'):
            line += '\n'
        f.write(f'{line}')
    f.close()


data = [
    'Robert Ruiz',
    'Arelbis Carpio\n',
    'Ashley Ruiz'
]
write('file.txt', data)
