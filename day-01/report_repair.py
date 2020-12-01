import itertools, math

input_file = 'day-01/input.txt'

def find_product_of_sum_combination(input, size, target = 2020):
  entries = list(map(int, input.splitlines()))
  for combo in [combo for combo in itertools.combinations(entries, size) if sum(combo) == target]:
    return math.prod(combo)

def part1(input):
  return find_product_of_sum_combination(input, 2)

def part2(input):
  return find_product_of_sum_combination(input, 3)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))