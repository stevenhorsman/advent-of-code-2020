import binary_boarding, fileinput

def test_part1_example_1():
  data = 'FBFBBFFRLR'
  assert binary_boarding.part1(data) == 357

def test_part1_example_2():
  data = '''
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL'''[1:]
  assert binary_boarding.part1(data) == 820

def test_part1():
  with open(binary_boarding.input_file) as f:
    data = f.read()
  expected = 858
  assert binary_boarding.part1(data) == expected

def test_part2():
  with open(binary_boarding.input_file) as f:
    data = f.read()
  expected = 557
  assert binary_boarding.part2(data) == expected
