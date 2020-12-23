import crab_cups, fileinput, pytest

def test_part1_example_1():
  data = '389125467'
  assert crab_cups.part1(data) == 67384529

def test_part1():
  with open(crab_cups.input_file) as f:
    data = f.read()
  expected = 97342568
  assert crab_cups.part1(data) == expected

def test_part1a_example_1():
  data = '389125467'
  assert crab_cups.part1a(data) == 67384529

def test_part1a():
  with open(crab_cups.input_file) as f:
    data = f.read()
  expected = 97342568
  assert crab_cups.part1a(data) == expected

@pytest.mark.skip(reason = 'Takes too long')
def test_part2_example_1():
  data = '389125467'
  assert crab_cups.part2(data) == 149245887792

def test_part2():
  with open(crab_cups.input_file) as f:
    data = f.read()
  expected = 902208073192
  assert crab_cups.part2(data) == expected
