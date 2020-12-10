import collections

input_file = 'day-10/input.txt'

def part1(input):
  voltages = [0] + list(map(int, input.splitlines()))
  voltages.sort()
  voltages.append(max(voltages)+3)

  diffs = collections.defaultdict(int)
  for i in range(len(voltages)-1):
    diffs[(voltages[i+1] - voltages[i])] += 1
  return diffs[1] * diffs[3]

def part2(input):
  voltages = [0] + list(map(int, input.splitlines()))
  voltages.sort()
  voltages.append(max(voltages)+3)

  # alternatives = [1] + [0]*(len(voltages)-1)
  # for i in range(len(voltages)-1):
  #   for j in range(i+1,len(voltages)):
  #     if voltages[j] - voltages[i] <= 3:
  #       alternatives[j] += alternatives[i]
  #     else:
  #       break
  # return alternatives[-1]

  # From https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gf934sg/
  arrange = [1]+[0]*voltages[-1]
  for i in voltages[1:]:
    arrange[i] = arrange[i-3] + arrange[i-2] + arrange[i-1]
  return arrange[-1]

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))