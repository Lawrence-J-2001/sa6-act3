from functools import reduce

numbers = [2, 10, 14, 20, 1, 7, 4, 2]
max_num = numbers[0]

new_max = reduce(lambda x, y: x if x >= y else y, numbers)
print(new_max)
