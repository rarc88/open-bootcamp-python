num = 5
text = 'Test'
amount = 10.58

# Old way
print('Num = %d, Text = %s, Amount = %f' % (num, text, amount))
print('Num = %d' % num)
print('Amount = %.2f' % amount)

# Old way <= 3.6
print(
    'Num = {}, Text = {}, Amount = {}'
    .format(num, text, amount)
)

print(
    'Num = {1}, Text = {0}, Amount = {2}'
    .format(num, text, amount)
)

print(
    'Num = {n}, Text = {t}, Amount = {a}'
    .format(n=num, t=text, a=amount)
)

# New way > 3.6
print(f'Num = {num}, Text = {text}, Amount = {amount}')


def sum(a, b):
    return a + b


print(f'{2} + {3} = {sum(2, 3)}')
