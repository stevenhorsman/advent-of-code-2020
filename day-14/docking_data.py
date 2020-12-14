import re, itertools, collections

input_file = 'day-14/input.txt'

def part1(input):
  mem = collections.defaultdict(int)
  curr_mask = ''
  for line in input.splitlines():
    if line.startswith("mask"):
      curr_mask = line.split(' = ')[1]
    else:
      address, value = list(map(int,re.match(r"mem\[(\d+)\] = (\d+)", line).groups()))
      or_mask = int(curr_mask.replace('X', '0'), 2)
      value |= or_mask
      and_mask = int(curr_mask.replace('X', '1'), 2)
      value &= and_mask
      mem[address] = value
  return sum(mem.values())

def part2(input):
  mem = collections.defaultdict(int)
  curr_mask = ''
  for line in input.splitlines():
    if line.startswith("mask"):
      curr_mask = line.split(' = ')[1]
    else:
      address, value = list(map(int,re.match(r"mem\[(\d+)\] = (\d+)", line).groups()))
      floating_values = []
      for i,b in enumerate(reversed(curr_mask)):
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
  return sum(mem.values())

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))