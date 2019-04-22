def day2func_part1(x):
    checksum = 0
    for num in x.readlines():
      L = num.split('\t')
      num_L = []
      num_T = [int(l.strip()) for l in L]
      checksum = checksum + max(num_T) - min(num_T)
    return checksum

with open('input.txt', 'r') as f:
    print(day2func_part1(f))
