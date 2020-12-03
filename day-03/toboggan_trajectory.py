import math

input_file = 'day-03/input.txt'

def count_trees(lines, right, down):
  width = len(lines[0])
  trees = 0
  col = 0
  for i in range(0, len(lines), down):
    if lines[i][col] == '#':
      trees += 1
    col = (col + right) % width
  return trees

def part1(input):
  lines = input.splitlines()
  return count_trees(lines, 3, 1)

def part2(input):
  lines = input.splitlines()
  slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
  return math.prod([count_trees(lines, right, down) for (right, down) in slopes])

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))