import encoding_error, fileinput

def test_part1_example_1():
  data = '''
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''[1:]
  assert encoding_error.part1(data, 5) == 127

def test_part1():
  with open(encoding_error.input_file) as f:
    data = f.read()
  expected = 70639851
  assert encoding_error.part1(data) == expected

def test_part2_example_1():
  data = '''
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''[1:]
  assert encoding_error.part2(data, 5) == 62

def test_part2():
  with open(encoding_error.input_file) as f:
    data = f.read()
  expected = 8249240
  assert encoding_error.part2(data) == expected
