import custom_customs, fileinput

def test_part1_example_1():
  data = '''
abc

a
b
c

ab
ac

a
a
a
a

b'''[1:]
  assert custom_customs.part1(data) == 11

def test_part1():
  with open(custom_customs.input_file) as f:
    data = f.read()
  expected = 6782
  assert custom_customs.part1(data) == expected

def test_part2_example_1():
  data = '''
abc

a
b
c

ab
ac

a
a
a
a

b'''[1:]
  assert custom_customs.part2(data) == 6

def test_part2():
  with open(custom_customs.input_file) as f:
    data = f.read()
  expected = 3596
  assert custom_customs.part2(data) == expected
