import adapter_array, fileinput

def test_part1_example_1():
  data = '''
16
10
15
5
1
11
7
19
6
12
4'''[1:]
  assert adapter_array.part1(data) == 35

def test_part1_example_2():
  data = '''
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''[1:]
  assert adapter_array.part1(data) == 220

def test_part1():
  with open(adapter_array.input_file) as f:
    data = f.read()
  expected = 2201
  assert adapter_array.part1(data) == expected

def test_part2_example_1():
  data = '''
16
10
15
5
1
11
7
19
6
12
4'''[1:]
  assert adapter_array.part2(data) == 8

def test_part2_example_2():
  data = '''
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''[1:]
  assert adapter_array.part2(data) == 19208

def test_part2():
  with open(adapter_array.input_file) as f:
    data = f.read()
  expected = 169255295254528
  assert adapter_array.part2(data) == expected
