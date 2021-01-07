import combo_breaker, fileinput

def test_part1_example_1():
  data = '''
5764801
17807724
'''[1:]
  assert combo_breaker.part1(data) == 14897079

def test_part1():
  with open(combo_breaker.input_file) as f:
    data = f.read()
  expected = 1478097
  assert combo_breaker.part1(data) == expected

def test_part1_benchmark(benchmark):
  with open(combo_breaker.input_file) as f:
    data = f.read()
  benchmark(combo_breaker.part1, data)
