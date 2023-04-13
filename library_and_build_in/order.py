list1 = ['z', 'c', 'd', 'a']

result = sorted(list1)
print(result)

result = sorted(list1, reverse=True)
print(result)

result = sorted(list1, reverse=True, key=lambda x: x)
print(result)
