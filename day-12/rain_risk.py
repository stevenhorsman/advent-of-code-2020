input_file = 'day-12/input.txt'

#Complex numbers trick from https://www.reddit.com/r/adventofcode/comments/kbj5me/2020_day_12_solutions/gfhsuai/

directions = dict(zip('NESW', [1j, 1, -1j, -1]))


def get_heading(curr, change):
  direction_string = 'NESW'
  return direction_string[(direction_string.index(curr) + change) % len(direction_string)]

def part1(input):
  deltas = dict(zip('NESW', [(0, 1), (1, 0), (0, -1), (-1, 0)]))

  x = y = 0
  heading = 'E'
  for path in input.splitlines():
    # print(x,y,heading, path)
    direction = path[:1]
    length = int(path [1:])
    if direction == 'F':
      x += (deltas[heading][0] * length)
      y += (deltas[heading][1] * length)
    elif direction == 'L':
      range = length // 90
      heading = get_heading(heading, -range)
    elif direction == 'R':
      range = length // 90
      heading = get_heading(heading, range)
    else:
      x += (deltas[direction][0] * length)
      y += (deltas[direction][1] * length)


  return abs(x)+abs(y)

def part2(input):
  deltas = dict(zip('NESW', [(0, 1), (1, 0), (0, -1), (-1, 0)]))

  waypoint_x = 10
  waypoint_y = 1

  x = y = 0
  for path in input.splitlines():
    # print(x,y,waypoint_x, waypoint_y, path)
    direction = path[:1]
    length = int(path [1:])
    if direction == 'F':
      x += (waypoint_x * length)
      y += (waypoint_y * length)
    elif direction == 'L':
      range = length // 90
      while range > 0:
        waypoint_x, waypoint_y = -waypoint_y, waypoint_x
        range -= 1
    elif direction == 'R':
      range = length // 90
      while range > 0:
        waypoint_x, waypoint_y = waypoint_y, -waypoint_x
        range -= 1
    else:
      waypoint_x += (deltas[direction][0] * length)
      waypoint_y += (deltas[direction][1] * length)


  return abs(x)+abs(y)

  return 0

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))