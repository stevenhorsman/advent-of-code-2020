import seating_system, fileinput

def test_part1_example_1():
  data = '''
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''[1:]
  assert seating_system.part1(data) == 37

def test_part1():
  with open(seating_system.input_file) as f:
    data = f.read()
  expected = 2178
  assert seating_system.part1(data) == expected

def test_part2_example_1():
  data = '''
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''[1:]
  assert seating_system.part2(data) == 26

def test_part2():
  with open(seating_system.input_file) as f:
    data = f.read()
  expected = 1978
  assert seating_system.part2(data) == expected
