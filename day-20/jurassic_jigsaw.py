import re, copy, itertools, random

input_file = 'day-20/input.txt'

directions = ['N','E','S','W']
deltas = dict(zip(['E','W','N','S'], [(1, 0), (-1, 0), (0, 1), (0, -1)]))

class Grid:
  def __init__(self, id, grid, flipped = False, rotated = 0):
    self.id = id
    self.flipped = flipped
    self.rotated = rotated
    self.grid = grid
    self.height = len(grid)
    self.width = len(grid[0])

  @classmethod
  def from_string(cls, input_string):
    lines = input_string.splitlines()
    id = re.match(r'Tile (\d+):', lines.pop(0))[1]
    grid = [[char for char in line] for line in lines]
    return cls(int(id), grid)

  def get_all_variants(self):
    variants = []
    variants.append(self)
    variants.append(variants[-1].rotate_90())
    variants.append(variants[-1].rotate_90())
    variants.append(variants[-1].rotate_90())
    variants.append(self.flip())
    variants.append(variants[-1].rotate_90())
    variants.append(variants[-1].rotate_90())
    variants.append(variants[-1].rotate_90())
    return variants

  def rotate_90(self):
    rotate = copy.deepcopy(self.grid)
    rotate = list(zip(*rotate[::-1]))  
    return Grid(self.id, rotate, self.flipped, self.rotated+1)

  def flip(self):
    return Grid(self.id, copy.deepcopy(self.grid[::-1]), not self.flipped, self.rotated)

  def get_matches(self, other):
    return [(alt, dir) for alt, dir in itertools.product(other.get_all_variants(), ['N','E','S','W']) if self.does_match(alt, dir)]

  def get_matches(self, other, dir):
    return [(alt, dir) for alt in other.get_all_variants() if self.does_match(alt, dir)]

  def does_match(self, other, direction):
    if direction == 'N':
      return ''.join(self.grid[0]) == ''.join(other.grid[-1])
    elif direction == 'E':
      return self.rotate_90().does_match(other.rotate_90(), 'S')
    elif direction == 'S':
      return ''.join(self.grid[-1]) == ''.join(other.grid[0])
    elif direction == 'W':
      return self.rotate_90().does_match(other.rotate_90(), 'N')

  def get_trim(self, border = 1):
    new_rows = []
    for i in range(border, len(self.grid)-border):
      new_rows.append(self.grid[i][border:len(self.grid[i])-border])
    return new_rows

  def count(self, char):
    count = 0
    for line in self.grid:
      count += ''.join(line).count(char)
    return count

  def __repr__(self):
    output = 'id: ' + str(self.id) + '\n'
    output += 'Flipped: ' + str(self.flipped) + '\n'
    output += 'Rotated: ' + str(self.rotated) + '\n'
    for y in range(self.height):
      for x in range(self.width):
        output += self.grid[y][x]
      output += '\n'
    return output

def calculate_layout(tiles):
  grid = {}
  x, y = 0, 0
  directions = ['N','E','S','W']

  grid[(x,y)] = tiles.pop(list(tiles.keys())[0])
  direction = directions[0]

  while direction != None and len(tiles) > 0: #All directions visited - done
    matches = []
    current_tile = grid[(x,y)]
    for tile in tiles.values():
      matches += current_tile.get_matches(tile, direction)
    if len(matches) == 0:
      new_x = x + deltas[dir][0]
      new_y = y + deltas[dir][1]
      if (new_x,new_y) in grid and grid[(new_x,new_y)] != None:
        x,y = new_x, new_y
        #must be back tracking?
      else:
        grid[(new_x,new_y)] = None
    elif len(matches) == 1:
      tile, dir = matches[0]
      x += deltas[direction][0]
      y += deltas[direction][1]
      grid[(x,y)] = tile
      tiles.pop(tile.id)
    else:
      print('mulitple matches!')
      return -10001    

    # Find a direction we haven't been in yet
    direction = None
    for dir in directions:
      new_x = x + deltas[dir][0]
      new_y = y + deltas[dir][1]
      if (new_x, new_y) not in grid:
        direction = dir
        break
    
    if direction == None: # All directions already explored - need to backtrack
      real_tiles = []
      for dir in directions:
        new_x = x + deltas[dir][0]
        new_y = y + deltas[dir][1]
        if grid[(new_x, new_y)] != None:
          real_tiles.append(dir)
      direction = random.choice(real_tiles)
      # Go to furtherest not None point in direction
      new_x = x + deltas[direction][0]
      new_y = y + deltas[direction][1]
      while (new_x, new_y) in grid and grid[(new_x, new_y)] != None:
        x = new_x
        y = new_y
        new_x = x + deltas[direction][0]
        new_y = y + deltas[direction][1]

  # trim Nones from grid
  grid = {key:val for key, val in grid.items() if val != None}
  return grid

def part1(input):
  tile_strings = input.split('\n\n')
  tiles = {}
  for string in tile_strings:
    tile = Grid.from_string(string)
    tiles[tile.id] = tile
  grid = calculate_layout(tiles)
   # find corners
  max_x = max(pos[0] for pos in grid.keys())
  min_x = min(pos[0] for pos in grid.keys())
  max_y = max(pos[1] for pos in grid.keys())
  min_y = min(pos[1] for pos in grid.keys())

  for (pos, tile) in grid.items():
    print('(' + ','.join([str(x) for x in pos]) + '):' + str(tile.id))
  return grid[(max_x, max_y)].id * grid[(min_x, max_y)].id * grid[(max_x, min_y)].id * grid[(min_x, min_y)].id

def part2(input):
  tile_strings = input.split('\n\n')
  tiles = {}
  for string in tile_strings:
    tile = Grid.from_string(string)
    tiles[tile.id] = tile
  grid = calculate_layout(tiles)

  max_x = max(pos[0] for pos in grid.keys())
  min_x = min(pos[0] for pos in grid.keys())
  max_y = max(pos[1] for pos in grid.keys())
  min_y = min(pos[1] for pos in grid.keys())

  tile_height = len(grid[(max_x, max_y)].grid)
  tile_width = len(grid[(max_x, max_y)].grid[0])
  
  print('\nlayout ids:')
  for y in range(max_y, min_y-1, -1):
    output = ''
    for x in range(min_x, max_x+1):
      output += str(grid[(x,y)].id)+ ' '
    print(output)

  print('\nlayout:')
  for y in range(max_y, min_y-1, -1):
    for r in range(0,tile_height): # Trims the row
      output = ''
      for x in range(min_x, max_x+1):
        output += ''.join(grid[(x,y)].grid[r])+ ' '
      print(output)
    print()

  print('\nstitched:')
  stitched = []
  for y in range(max_y, min_y-1, -1):
    for r in range(1,tile_height-1): # Trims the row
      row = []
      for x in range(min_x, max_x+1):
        row += grid[(x,y)].grid[r][1:tile_width-1]
      stitched.append(row)
  
  total = Grid(0, stitched)

  pattern = '''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''[1:].splitlines()

  patterns_found = max([count_patterns(alts.grid, pattern) for alts in total.get_all_variants()])

  return total.count('#') - (''.join(pattern).count('#') * patterns_found)

def count_patterns(grid, pattern):
  patterns = 0
  for row in range(len(grid) - len(pattern)):
    for col in range(len(grid[0]) - len(pattern[0])):
      found = True
      for y in range(len(pattern)):
        for x in range(len(pattern[0])):
          if pattern[y][x] == '#':
            found = found and grid[row+y][col+x] == '#'
      if found:
        patterns +=1
  return patterns

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))