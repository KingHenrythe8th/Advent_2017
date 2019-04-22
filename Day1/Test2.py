# Use Day1 function to assert 3 statements

# 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the
# second digit and the third digit (2) matches the fourth digit.

from Day1 import day1func_part2

assert day1func_part2("1212") == 6, ("The list contains 4 items, and all four \
digits match the digit 2 items ahead.")

assert day1func_part2("1221") == 0, ("because every comparison is between a 1 \
and a 2.")

assert day1func_part2("123425") == 4, ("because both 2s match each other, but \
no other digit has a match.")

assert day1func_part2("123123") == 12, ("Just does")

assert day1func_part2("12131415") == 4, ("Just does")

print ("Tests passed")
