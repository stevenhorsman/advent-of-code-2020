import crab_combat, fileinput

def test_part1_example_1():
  data = '''
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''[1:]
  assert crab_combat.part1(data) == 306

def test_part1():
  with open(crab_combat.input_file) as f:
    data = f.read()
  expected = 32401
  assert crab_combat.part1(data) == expected

def test_part2_example_1():
  data = '''
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''[1:]
  assert crab_combat.part2(data) == 291

# TODO - recursive test
def test_part2_example_2():
  data = '''
Player 1:
43
19

Player 2:
2
29
14'''[1:]
  assert crab_combat.part2(data) == 105

def test_part2():
  with open(crab_combat.input_file) as f:
    data = f.read()
  expected = 31436
  assert crab_combat.part2(data) == expected
