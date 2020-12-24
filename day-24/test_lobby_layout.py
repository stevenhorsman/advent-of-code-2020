import lobby_layout, fileinput

example_data = '''
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew'''[1:]
def test_part1_example_1():
  assert lobby_layout.part1(example_data) == 10

def test_part1():
  with open(lobby_layout.input_file) as f:
    data = f.read()
  expected = 289
  assert lobby_layout.part1(data) == expected

def test_part2_example_1():
  assert lobby_layout.part2(example_data) == 2208

def test_part2():
  with open(lobby_layout.input_file) as f:
    data = f.read()
  expected = 3551
  assert lobby_layout.part2(data) == expected
