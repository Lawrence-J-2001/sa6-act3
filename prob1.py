from functools import reduce

num = 121
num_string = str(num)

sum_of_digits = reduce(lambda x, y: int(x) + int(y), num_string)
print(sum_of_digits)