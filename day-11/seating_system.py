from copy import deepcopy
from collections import Counter

input_file = 'day-11/input.txt'

def get_deltas():
  return[
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
  ]

class Grid:
  def __init__(self, grid):
    self.grid = grid
    self.height = len(grid)
    self.width = len(grid[0])

  @classmethod
  def from_string(cls, input_string):
    grid = [[char for char in line] for line in input_string.splitlines()]
    return cls(grid)

  def count_neighbours(self, x, y):
    adjacents = [(x+dx,y+dy) for (dx,dy) in get_deltas()]
    adjacents_in_range = [(x,y) for (x,y) in adjacents if (x in range(self.width) and y in range(self.height))]
    return sum(1 for (x, y) in adjacents_in_range if self.grid[y][x] == '#')

  def does_empty_get_occupied(self, x, y):
    return self.count_neighbours(x, y) == 0

  def does_occupied_empty(self, x, y):
    return self.count_neighbours(x, y) >= 4

  def round(self):
    next_grid = deepcopy(self.grid) # deepcopy needed?
    for y in range(self.height):
      for x in range(self.width):
        current = self.grid[y][x]
        if (current == 'L') and self.does_empty_get_occupied(x, y):
          next_grid[y][x] = '#'
        elif (current == '#') and self.does_occupied_empty(x,y):
          next_grid[y][x] = 'L'
    return self.get_next_grid(next_grid)

  def get_next_grid(self, grid):
    return Grid(grid)

  def get_occupied(self):
    return sum(Counter(line)['#'] for line in self.grid)

  def __repr__(self):
    output = ''
    for y in range(self.height):
      for x in range(self.width):
        output += self.grid[y][x]
      output += '\n'
    output += 'Total:' + self.get_occupied() + '\n'
    return output

class Grid2(Grid):
  def does_empty_get_occupied(self, x, y):
    return self.count_seen_seats(x, y) == 0

  def does_occupied_empty(self, x, y):
    return self.count_seen_seats(x, y) >= 5

  def does_see_seat(self,x,y, dx, dy):
    y_ = y+dy
    x_ = x+dx
    while (x_ in range(self.width) and y_ in range(self.height)):
      if self.grid[y_][x_] == '#':
        return True
      elif self.grid[y_][x_] == 'L':
        return False
      y_ += dy
      x_ += dx
    return False

  def count_seen_seats(self, x, y):
    return sum(1 for (dx,dy) in get_deltas() if self.does_see_seat(x, y, dx, dy))

  def get_next_grid(self, grid):
    return Grid2(grid)

def round_until_stable(grid):
  next = grid.round()
  while next.grid != grid.grid:
    # print_grid(grid)
    grid = next
    next = grid.round()
  return grid.get_occupied()

def part1(input):
  grid = Grid.from_string(input)
  return round_until_stable(grid)

def part2(input):
  grid = Grid2.from_string(input)
  return round_until_stable(grid)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))