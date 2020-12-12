import rain_risk, fileinput

def test_part1_example_1():
  data = '''
F10
N3
F7
R90
F11'''[1:]
  assert rain_risk.part1(data) == 25

def test_part1():
  with open(rain_risk.input_file) as f:
    data = f.read()
  expected = 1010
  assert rain_risk.part1(data) == expected

def test_part2_example_1():
  data = '''
F10
N3
F7
R90
F11'''[1:]
  assert rain_risk.part2(data) == 286

def test_part2():
  with open(rain_risk.input_file) as f:
    data = f.read()
  expected = 52742
  assert rain_risk.part2(data) == expected
