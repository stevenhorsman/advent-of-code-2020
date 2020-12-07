import handy_haversacks, fileinput

def test_part1_example_1():
  data = '''
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''[1:]
  assert handy_haversacks.part1(data) == 4

def test_part1():
  with open(handy_haversacks.input_file) as f:
    data = f.read()
  expected = 355
  assert handy_haversacks.part1(data) == expected

def test_part2_example_1():
  data = '''
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''[1:]
  assert handy_haversacks.part2(data) == 32

def test_part2_example_2():
  data = '''
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''[1:]
  assert handy_haversacks.part2(data) == 126

def test_part2():
  with open(handy_haversacks.input_file) as f:
    data = f.read()
  expected = 5312
  assert handy_haversacks.part2(data) == expected
