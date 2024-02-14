group1 = [1, 10, 4, 20, 25, 16, 200, 56, 75]
group2 = [2, 7, 29, 75, 99, 16, 10, 4, 16]

intersection = list(filter(lambda x: x in group1 and x in group2, group1))

print(intersection)