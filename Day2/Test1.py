#For example, given the following spreadsheet:

# 5, 1, 9, 5
# 7, 5, 3
# 2, 4, 6, 8

from Day2 import day2func_part1

with open('test_input.txt', 'r') as file:

    assert day2func_part1(file) == 18,("The first row's largest and \
smallest values are 9 and 1, and their difference is 8. The second row's \
largest and smallest values are 7 and 3, and their difference is 4.The third \
row's difference is 6.")

print ("Test passed")
