from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

even = filter(lambda x: x % 2 == 0, nums)
print(list(even))

result = map(lambda x: x + 1, nums)
print(list(result))

sum = reduce(lambda p, c: p + c, nums, 0)
print(sum)
