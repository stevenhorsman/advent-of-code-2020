input_file = 'day-12/input.txt'

#Complex numbers trick from https://www.reddit.com/r/adventofcode/comments/kbj5me/2020_day_12_solutions/gfhsuai/
directions = dict(zip('NESW', [1j, 1, -1j, -1]))
rotate = dict(zip('LR', [1j, -1j]))

def get_heading(curr, change):
  direction_string = 'NESW'
  return direction_string[(direction_string.index(curr) + change) % len(direction_string)]

def part1(input):
  curr, heading = 0+0j, 1+0j
  for direction, length in [(line[:1], int(line[1:])) for line in input.splitlines()]:
    if direction == 'F':
      curr += heading * length
    elif direction in 'LR':
      range = length // 90
      heading *= rotate[direction] ** range
    else:
      curr += length * directions[direction]

  return abs(curr.real) + abs(curr.imag)

def part2(input):
  curr, waypoint = 0+0j, 10+1j
  for direction, length in [(line[:1], int(line[1:])) for line in input.splitlines()]:
    if direction == 'F':
      curr += waypoint * length
    elif direction in 'LR':
      range = length // 90
      waypoint *= rotate[direction] ** range
    else:
      waypoint += length * directions[direction]

  return abs(curr.real) + abs(curr.imag)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))