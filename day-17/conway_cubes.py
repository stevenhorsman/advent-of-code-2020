input_file = 'day-17/input.txt'

def create_input_set(input):
  active = set()
  lines = input.splitlines()

  z = 0
  for y in range(len(lines)):
    for x in range(len(lines[y])):
      if lines[y][x] == '#':
        active.add((x,y,z))
  return active

def count_neighbours(active, x, y, z):
  neighbours = 0
  for dx in [-1,0,1]:
    for dy in [-1,0,1]:
      for dz in [-1,0,1]:
        if not (dx==0 and  dy==0 and dz==0) and (x+dx, y+dy, z+dz) in active:
            neighbours += 1
  return neighbours

def part1(input, iterations = 6):
  active = create_input_set(input)
  for i in range(iterations):
    bounds = i+8 # todo - work out min and max of sample
    next_gen = set()
    for x in range(-bounds, bounds+1):
      for y in range(-bounds, bounds+1):
        for z in range(-bounds, bounds+1):
          neighbours = count_neighbours(active, x, y, z)
          if (x,y,z) in active and neighbours in [2,3]:
            next_gen.add((x,y,z))
          elif (x,y,z) not in active and neighbours == 3:
            next_gen.add((x,y,z))
    active = next_gen
  return len(active)

def create_input_set4(input):
  active = set()
  lines = input.splitlines()

  z = 0
  w = 0
  for y in range(len(lines)):
    for x in range(len(lines[y])):
      if lines[y][x] == '#':
        active.add((x,y,z,w))
  return active

def count_neighbours4(active, x, y, z, w):
  neighbours = 0
  for dx in [-1,0,1]:
    for dy in [-1,0,1]:
      for dz in [-1,0,1]:
        for dw in [-1,0,1]:
          if not (dx == 0 and  dy == 0 and dz == 0 and dw == 0) and (x + dx, y + dy, z + dz, w + dw) in active:
            neighbours += 1
  return neighbours

def part2(input, iterations = 6):
  active = create_input_set4(input)
  for i in range(iterations):
    bounds = i+3 # todo - work out min and max of sample
    next_gen = set()
    for x in range(-bounds-8, bounds+9):
      for y in range(-bounds-8, bounds+9):
        for z in range(-bounds, bounds+1):
          for w in range(-bounds, bounds+1):
            neighbours = count_neighbours4(active, x, y, z, w)
            if (x,y,z,w) in active and neighbours in [2,3]:
              next_gen.add((x,y,z,w))
            elif (x,y,z,w) not in active and neighbours == 3:
              next_gen.add((x,y,z, w))
    active = next_gen
  return len(active)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))