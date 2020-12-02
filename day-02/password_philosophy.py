import re

input_file = 'day-02/input.txt'

def count_valid_passwords(input, is_valid):
  total_valid = 0
  for line in input.splitlines():
    min, max, char, pattern = list(re.match(r"(\d+)-(\d+) (\w): (\w+)", line).groups())
    if is_valid(pattern, char, int(min), int(max)):
      total_valid += 1
  return total_valid

def part1(input):
  is_valid = lambda pattern, char, min, max: min <= pattern.count(char) <= max
  return count_valid_passwords(input, is_valid)

def part2(input):
  is_valid = lambda pattern, char, min, max: (pattern[min-1] == char) ^ (pattern[max-1] == char) # Not zero indexed
  return count_valid_passwords(input, is_valid)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))