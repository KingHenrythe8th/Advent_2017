# Use Day1 function to assert 3 statements

# 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the
# second digit and the third digit (2) matches the fourth digit.

from Day1 import day1func_part1

assert day1func_part1("1122") == 3, ("1122 produces a sum of 3 (1 + 2) because the first \
 digit (1) matches the second digit and the third digit (2) matches \
 the fourth digit.")

assert day1func_part1("1111") == 4, ("1111 produces 4 because each digit (all 1) \
matches the next.")

assert day1func_part1("1234") == 0, ("1234 produces 0 because no digit matches the \
next.")

assert day1func_part1("91212129") == 9, ("91212129 produces 9 because the only \
digit that matches the next one is the last digit, 9.")

print ("Tests passed")
