import handheld_halting, fileinput

def test_part1_example_1():
  data = '''
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''[1:]
  assert handheld_halting.part1(data) == 5  

def test_part1():
  with open(handheld_halting.input_file) as f:
    data = f.read()
  expected = 1200
  assert handheld_halting.part1(data) == expected

def test_part2_example_1():
  data = '''
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''[1:]
  assert handheld_halting.part2(data) == 8

def test_part2():
  with open(handheld_halting.input_file) as f:
    data = f.read()
  expected = 1023
  assert handheld_halting.part2(data) == expected
