import re

input_file = 'day-18/input.txt'

# Refactor improvements inspired by https://github.com/sophiebits/adventofcode/blob/main/2020/day18.py
def calculate_no_brackets(line, precedence):
  for operators in precedence:
    while any(op in line for op in operators):
      op_search = '|'.join(operators)
      line = re.sub(r'(\d+) ['+op_search+'] (\d+)', lambda match: str(eval(match.group(0))), line, count=1)
  return int(line)

def calculate(line, precedence):
  while '(' in line:
    line = re.sub(r'\(([^()]+)\)', lambda match: str(calculate(match.group(1), precedence)), line)
  return calculate_no_brackets(line, precedence)

def part1(input):
  precedence = [['*', '+']]
  return sum(calculate(line, precedence) for line in input.splitlines())

def part2(input):
  precedence = [['+'], ['*']]
  return sum(calculate(line, precedence) for line in input.splitlines())

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))