import toboggan_trajectory, fileinput

def test_part1_example_1():
  data = '''
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''[1:]
  assert toboggan_trajectory.part1(data) == 7

def test_part1():
  with open(toboggan_trajectory.input_file) as f:
    data = f.read()
  expected = 284
  assert toboggan_trajectory.part1(data) == expected

def test_part2_example_1():
  data = '''
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''[1:]
  assert toboggan_trajectory.part2(data) == 336


def test_part2():
  with open(toboggan_trajectory.input_file) as f:
    data = f.read()
  expected = 3510149120
  assert toboggan_trajectory.part2(data) == expected
