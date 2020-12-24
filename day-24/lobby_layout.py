import re


input_file = 'day-24/input.txt'

#Use cube co-ordinates system:https://www.redblobgames.com/grids/hexagons/ CF 2017:11
deltas = dict(zip(['e','ne','nw','w','se','sw'], [(1, -1, 0), (1, 0, -1), (0, 1, -1), (-1, 1, 0), (0, -1, 1), (-1, 0, 1)]))

def convert_line(line):
  return re.findall('('+'|'.join(deltas.keys())+')',line)

def get_initial_flipped(input):
  flipped_tiles = set()
  for line in input.splitlines():
    x,y,z = 0,0,0
    directions = convert_line(line)
    for dir in directions:
      x += deltas[dir][0]
      y += deltas[dir][1]
      z += deltas[dir][2]
    if (x,y,z) in flipped_tiles:
      flipped_tiles.remove((x,y,z))
    else:
      flipped_tiles.add((x,y,z))
  return flipped_tiles

def part1(input):
  flipped_tiles = get_initial_flipped(input)
  return len(flipped_tiles)

def get_neighbours(point):
  neighbours = set()
  for dir,delta in deltas.items():
    # Do with zip?
    x = point[0] + delta[0]
    y = point[1] + delta[1]
    z = point[2] + delta[2]
    neighbours.add((x,y,z))
  return neighbours

def count_neighbours(flipped, point):
  neighbour_count = 0
  for neighbour in get_neighbours(point):
    if neighbour in flipped:
      neighbour_count += 1
  return neighbour_count

def part2(input):
  flipped = get_initial_flipped(input)
  for i in range(100):
    points_to_check = set()
    for point in flipped:
      points_to_check.add(point)
      for neighbour in get_neighbours(point):
        points_to_check.add(neighbour)
    next_gen = set()
    for point in points_to_check:
      neighbour_count = count_neighbours(flipped, point)
      if point in flipped and neighbour_count in [1,2]:
        next_gen.add(point)
      elif point not in flipped and neighbour_count == 2:
        next_gen.add(point)
    print(i, len(flipped))
    flipped = next_gen

  return len(flipped)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))