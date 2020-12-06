input_file = 'day-06/input.txt'

def get_groups(input):
  return [group.split('\n') for group in input.split('\n\n')]

def part1(input):
  return sum([len(set.union(*[set(sub) for sub in group])) for group in get_groups(input)])

def part2(input): 
  return sum([len(set.intersection(*[set(sub) for sub in group])) for group in get_groups(input)])

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))