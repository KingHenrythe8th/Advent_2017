def day2func_part1(x):
    checksum = 0
    for num in x.readlines():
      L = num.split('\t')
      num_L = []
      num_T = [int(l.strip()) for l in L]
      checksum = checksum + max(num_T) - min(num_T)
    return checksum



def day2func_part2(x):
    checksum = 0
    for num in x.readlines():
      L = num.split('\t')
      num_L = []
      num_T = sorted([int(l.strip()) for l in L], reverse=True)
      for n in num_T:
        for q in num_T:
          i_n = num_T.index(n)
          i_q = num_T.index(q)
          nq = float(n)/q
          qn = float(q)/n
          if nq.is_integer() and i_n != i_q:
            checksum = checksum + nq
          elif qn.is_integer() and i_n != i_q:
            checksum = checksum + qn
          else:
            continue
    return checksum / 2

with open('input.txt', 'r') as f:
    print(day2func_part2(f))
