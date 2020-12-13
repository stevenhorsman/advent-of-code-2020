import shuttle_search, fileinput

def test_part1_example_1():
  data = '''
939
7,13,x,x,59,x,31,19'''[1:]
  assert shuttle_search.part1(data) == 295

def test_part1():
  with open(shuttle_search.input_file) as f:
    data = f.read()
  expected = 2845
  assert shuttle_search.part1(data) == expected

def test_part2_example_1():
  data = '''
939
7,13,x,x,59,x,31,19'''[1:]
  assert shuttle_search.part2(data) == 1068781

def test_part2_example_2():
  data = '''
939
1789,37,47,1889'''[1:]
  assert shuttle_search.part2(data) == 1202161486

def test_part2():
  with open(shuttle_search.input_file) as f:
    data = f.read()
  expected = 487905974205117
  assert shuttle_search.part2(data) == expected
