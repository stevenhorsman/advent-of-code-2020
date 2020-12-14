import docking_data, fileinput

def test_part1_example_1():
  data = '''
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''[1:]
  assert docking_data.part1(data) == 165

def test_part1():
  with open(docking_data.input_file) as f:
    data = f.read()
  expected = 18630548206046
  assert docking_data.part1(data) == expected

def test_part2_example_1():
  data = '''
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''[1:]
  assert docking_data.part2(data) == 208

def test_part2():
  with open(docking_data.input_file) as f:
    data = f.read()
  expected = 4254673508445
  assert docking_data.part2(data) == expected
