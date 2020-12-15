import rambunctious_recitation, fileinput, pytest

def test_part1_example_1():
  data = '0,3,6'
  assert rambunctious_recitation.part1(data) == 436

def test_part1_example_2():
  data = '3,1,2'
  assert rambunctious_recitation.part1(data) == 1836

def test_part1_example_3():
  data = '2,3,1'
  assert rambunctious_recitation.part1(data) == 78

def test_part1():
  with open(rambunctious_recitation.input_file) as f:
    data = f.read()
  expected = 929
  assert rambunctious_recitation.part1(data) == expected

@pytest.mark.skip(reason="takes 10s")
def test_part2_example_1():
  data = '0,3,6'
  assert rambunctious_recitation.part2(data) == 175594

def test_part2():
  with open(rambunctious_recitation.input_file) as f:
    data = f.read()
  expected = 16671510
  assert rambunctious_recitation.part2(data) == expected
