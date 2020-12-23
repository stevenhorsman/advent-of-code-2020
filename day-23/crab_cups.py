from collections import deque

input_file = 'day-23/input.txt'

def part1(input):
  cups = deque([int(c) for c in input])
  print(cups)
  for _ in range(100):
    current_value = cups[0]
    cups.rotate(-1)

    # Remove 3 cups left (including wrapping) of the index
    removed = [cups.popleft(),cups.popleft(),cups.popleft()]

    # Destination cup is index_value-1 until it can be found (including wrapping)
    destination = current_value - 1 if current_value != 1 else 9
    while destination in removed:
      destination = destination - 1 if destination != 1 else 9

    while cups[len(cups)-1] != destination:
      cups.rotate(-1)

    # Place 3 cups back on the right of the destination 
    cups.extendleft(removed[::-1])

    # index is right of the old index
    while cups[len(cups)-1] != current_value:
      cups.rotate(-1)

  # produce result string of cups from 1
  while cups[len(cups)-1] != 1:
    cups.rotate(-1)
  cups.pop()

  return int(''.join([str(i) for i in cups]))

def part2(input):
  return 0

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))