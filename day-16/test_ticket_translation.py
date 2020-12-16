import ticket_translation, fileinput

def test_part1_example_1():
  data = '''
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''[1:]
  assert ticket_translation.part1(data) == 71

def test_part1():
  with open(ticket_translation.input_file) as f:
    data = f.read()
  expected = 20058
  assert ticket_translation.part1(data) == expected

def test_part2_example_1():
  data = '''
departure class: 0-1 or 4-19
row: 0-5 or 8-19
departure seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
7,3,47
15,1,5
5,14,9'''[1:]
  assert ticket_translation.part2(data) == (12 * 13)

def test_part2():
  with open(ticket_translation.input_file) as f:
    data = f.read()
  expected = 366871907221
  assert ticket_translation.part2(data) == expected
