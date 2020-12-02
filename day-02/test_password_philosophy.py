import password_philosophy, fileinput

def test_part1_example_1():
  data = '''
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''[1:]
  assert password_philosophy.part1(data) == 2

def test_part1():
  with open(password_philosophy.input_file) as f:
    data = f.read()
  expected = 655
  assert password_philosophy.part1(data) == expected

def test_part2_example_1():
  data = '''
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''[1:]
  assert password_philosophy.part2(data) == 1

def test_part2():
  with open(password_philosophy.input_file) as f:
    data = f.read()
  expected = 673
  assert password_philosophy.part2(data) == expected
