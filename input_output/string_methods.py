from pprint import pprint

pprint(dir(''))

text = 'my name es Roberto Ruiz'

print(text.capitalize())
print(text.upper())
print(text.lower())
print(text.count('a'))
print(text.split('es'))

num = '2'
print(num.isdigit())
num = 'a2'
print(num.isalnum())

text = '   white spaces   '
print(text)
print(text.strip())
