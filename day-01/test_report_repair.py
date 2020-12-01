import report_repair, fileinput

def test_part1_example_1():
  data = '''
1721
979
366
299
675
1456'''[1:]
  assert report_repair.part1(data) == 514579

def test_part1():
  with open(report_repair.input_file) as f:
    data = f.read()
  expected = 445536
  assert report_repair.part1(data) == expected

def test_part2_example_1():
  data = '''
1721
979
366
299
675
1456'''[1:]
  assert report_repair.part2(data) == 241861950

def test_part2():
  with open(report_repair.input_file) as f:
    data = f.read()
  expected = 138688160
  assert report_repair.part2(data) == expected
