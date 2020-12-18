import operation_order, fileinput

def test_part1_example_1():
  data = '1 + 2 * 3 + 4 * 5 + 6'
  assert operation_order.part1(data) == 71

def test_part1_example_2():
  data = '1 + (2 * 3) + (4 * (5 + 6))'
  assert operation_order.part1(data) == 51

def test_part1_example_3():
  data = '''
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
'''[1:]
  assert operation_order.part1(data) == 26 + 437 + 12240 + 13632

def test_part1():
  with open(operation_order.input_file) as f:
    data = f.read()
  expected = 14006719520523
  assert operation_order.part1(data) == expected

def test_part2_example_1():
  data = '1 + 2 * 3 + 4 * 5 + 6'
  assert operation_order.part2(data) == 231

def test_part2_example_2():
  data = '1 + (2 * 3) + (4 * (5 + 6))'
  assert operation_order.part2(data) == 51

def test_part2_example_3():
  data = '''
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
'''[1:]
  assert operation_order.part2(data) == 46 + 1445 + 669060 + 23340


def test_part2():
  with open(operation_order.input_file) as f:
    data = f.read()
  expected = 545115449981968
  assert operation_order.part2(data) == expected
