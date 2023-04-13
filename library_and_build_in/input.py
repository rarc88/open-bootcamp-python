from getpass import getpass
from pprint import pprint

# name = input('What is your name? ')
# print(f'Hello {name}')

# password = getpass('Password: ', stream=None)
# print(f'Your password is {password}')

secret = 50
value = 0
while True:
    value = input('Intro a number: ')
    if not value.isdigit():
        print(f'{value} is not a number')
        continue
    value = int(value)
    if value > secret:
        print('High')
    elif value < secret:
        print('Low')
    else:
        print('You got!!!')
        break
