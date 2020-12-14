import re, itertools, collections

input_file = 'day-14/input.txt'

def updateMemory1(mem, mask, address, value):
  or_mask = int(mask.replace('X', '0'), 2)
  value |= or_mask
  and_mask = int(mask.replace('X', '1'), 2)
  value &= and_mask
  mem[address] = value

def decoder_chip(input, update_func):
  mem = collections.defaultdict(int)
  curr_mask = ''
  for line in input.splitlines():
    if line.startswith("mask"):
      curr_mask = line.split(' = ')[1]
    else:
      address, value = list(map(int,re.match(r"mem\[(\d+)\] = (\d+)", line).groups()))
      update_func(mem, curr_mask, address, value)
  return sum(mem.values())

def part1(input):
  return decoder_chip(input, updateMemory1)

def updateMemory2(mem, mask, address, value):
  floating_values = []
  for i,b in enumerate(reversed(mask)):
    if b == '1' and (address & 2**i) == 0:
      address += 2**i
    elif b == 'X':
      if (address & 2**i) != 0:
        # Remove bit for wildcards
        address -= 2**i
      floating_values.append(2**i)

  for l in range(len(floating_values) + 1):
    for comb in itertools.combinations(floating_values, l):
      mem[address + sum(comb)] = value

def part2(input):
  return decoder_chip(input, updateMemory2)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))