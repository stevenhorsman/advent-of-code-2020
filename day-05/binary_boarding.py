input_file = 'day-05/input.txt'

trans = str.maketrans('FBLR', '0101')
def get_seat_id(boarding_string):
  return int(boarding_string.translate(trans), 2)

def part1(input):
  seat_ids = sorted([get_seat_id(boarding_string) for boarding_string in input.splitlines()])
  return max(seat_ids)

def part2(input):
  seat_ids = sorted([get_seat_id(boarding_string) for boarding_string in input.splitlines()])
  for i in seat_ids:
    if ((i + 1) not in seat_ids) and ((i + 2) in seat_ids):
      return i + 1

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))