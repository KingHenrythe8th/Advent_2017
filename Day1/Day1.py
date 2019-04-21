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

with open('input.txt', 'r') as file:
    text = file.readline().strip()

print(day1func_part1(text))
