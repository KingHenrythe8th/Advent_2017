# Day 1 solution part 1

def day1func_part1(text):
  counter = iter(text)
  captcha = 0
  pos_1 = text[(len(text) - 1)]

  while True:
    try:
      pos_2 = counter.next()
      if pos_1 == pos_2:
        captcha = captcha + int(pos_1)
        pos_1 = pos_2
      else:
        pos_1 = pos_2
        continue
    except StopIteration:
      break

  return captcha

def day1func_part2(text):
  s_1 = text[:(len(text) / 2)]
  s_2 = text[(len(text) / 2):]
  line_1 = iter(s_1)
  line_2 = iter(s_2)
  captcha = 0
  while True:
    try:
      x = line_1.next()
      y = line_2.next()
      if x == y:
        captcha = captcha + 2 * int(x)
      else:
        continue
    except:
      break

  return captcha

with open('input.txt', 'r') as file:
    text = file.readline().strip()


print day1func_part2(text)
