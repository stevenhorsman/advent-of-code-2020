import itertools

input_file = 'day-17/input.txt'

class Point:
  def __init__(self, *args):
    self.coords = tuple(args)
    self.dimension = len(self.coords)
  
  def get_neighbours(self):
    neighbours = set()
    for delta in itertools.product([-1,0,1], repeat = self.dimension):
      neighbour = []
      for i in range(self.dimension):
        neighbour.append(self.coords[i] + delta[i])
      if tuple(neighbour) != self.coords:  
        neighbours.add(Point(*neighbour))
    return neighbours

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.coords == other.coords

  def __ne__(self, other):
    return not self.__eq__(other)

  def __hash__(self):
    return hash(self.coords)

  def __repr__(self):
    return f'{self.coords}'

def create_input_set(input, dimensions):
  active = set()
  lines = input.splitlines()
  for y in range(len(lines)):
    for x in range(len(lines[y])):
      if lines[y][x] == '#':
        active.add(Point(x,y,*([0] * (dimensions - 2))))
  return active

def count_neighbours(active, point):
  neighbour_count = 0
  for neighbour in point.get_neighbours():
    if neighbour in active:
      neighbour_count += 1
  return neighbour_count

def evolve(input, iterations, dimensions):
  active = create_input_set(input, dimensions)
  for i in range(iterations):
    points_to_check = set()
    for point in active:
      points_to_check = points_to_check.union({point})
      points_to_check = points_to_check.union(point.get_neighbours())
    next_gen = set()
    neighbour_cache = {}
    for point in points_to_check:
      neighbour_count = count_neighbours(active, point)
      if point in active and neighbour_count in [2,3]:
        next_gen.add(point)
      elif point not in active and neighbour_count == 3:
        next_gen.add(point)
    active = next_gen
  return len(active)

def part1(input, iterations = 6):
  return evolve(input, iterations, 3)

def part2(input, iterations = 6):
  return evolve(input, iterations, 4)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))