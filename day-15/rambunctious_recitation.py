import collections

input_file = 'day-15/input.txt'

def van_eck(input, iterations):
  given = [int(x) for x in input.split(',')]
  last_seen = collections.defaultdict(int)
  for i in range(len(given)-1):
    last_seen[given[i]] = i+1
    
  previous = given[-1]
  for i in range (len(given),iterations):
    last_seen[previous], previous = i, 0 if previous not in last_seen else i - last_seen[previous]
  return previous

def part1(input):
  return van_eck(input, 2020)

def part2(input):
  return van_eck(input, 30000000)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))