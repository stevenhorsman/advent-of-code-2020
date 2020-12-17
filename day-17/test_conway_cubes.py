import conway_cubes, fileinput

example_data = '''
.#.
..#
###'''[1:]

def test_part1_example_0():
  assert conway_cubes.part1(example_data,0) == 5

def test_part1_example_1():
  assert conway_cubes.part1(example_data,1) == 11

def test_part1_example_2():
  assert conway_cubes.part1(example_data,3) == 38

def test_part1_example_3():
  assert conway_cubes.part1(example_data,6) == 112

def test_part1():
  with open(conway_cubes.input_file) as f:
    data = f.read()
  expected = 242
  assert conway_cubes.part1(data) == expected

def test_part2_example_1():
  assert conway_cubes.part2(example_data) == 848

def test_part2():
  with open(conway_cubes.input_file) as f:
    data = f.read()
  expected = 2292
  assert conway_cubes.part2(data) == expected
