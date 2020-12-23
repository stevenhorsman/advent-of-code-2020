from collections import deque

input_file = 'day-23/input.txt'

# Note - removed back pointers, so not a general linkedlist, but faster for this problem
class LinkedList:
  def __init__(self):
    self.lookup = {}
    self.current = None

  def add_node(self, data):
    self.lookup[data] = Node(data)

  def set_node_next(self, node_data, next_data):
    self.find(node_data).next = self.find(next_data)
    
  def set_current(self, new_current):
    self.current = new_current

  def slice_out(self, size):
    slice_item = self.current
    slice = []
    for _ in range(size):
      slice_item = slice_item.next
      slice.append(slice_item)
    self.current.next = slice[-1].next
    return slice

  def slice_in(self, after, slice):
    slice[-1].next = after.next
    after.next = slice[0]

  def find(self, data):
    return self.lookup[data]

  def get_string(self, start):
    start_node = self.find(start)
    node = start_node.next
    nodes = []
    while node is not start_node:
      nodes.append(str(node.data))
      node = node.next
    return "".join(nodes)

  def __repr__(self):
    nodes = [str(self.current.data)]
    node = self.current.next
    while node is not self.current:
      nodes.append(str(node.data))
      node = node.next
    nodes.append("")
    return " -> ".join(nodes)

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# Faster code based on https://raw.githubusercontent.com/arknave/advent-of-code-2020/main/day23/day23.py
def play_crab_cups(input, part2 = False):
  input = [int(c) for c in input]
  N = 1_000_000 if part2 else len(input)

  cups = LinkedList()
  for i in range(1, N +1):
    cups.add_node(i)

  for current, next in zip(input, input[1:]):
    cups.set_node_next(current, next)
  if part2:
    cups.set_node_next(input[-1], len(input)+1)
    for i in range(len(input)+1, N):
      cups.set_node_next(i, i+1)
    cups.set_node_next(N, input[0])
  else:
    cups.set_node_next(input[-1], input[0])

  cups.set_current(cups.find(input[0]))

  moves = 10_000_000 if part2 else 100
  for i in range(moves):
    current_value = cups.current.data
    # print(current_value, cups)

    # Remove 3 cups left (including wrapping) of the index
    removed = cups.slice_out(3)

    # Destination cup is index_value-1 until it can be found (including wrapping)
    destination = current_value - 1 if current_value != 1 else N
    while destination in [r.data for r in  removed]:
      destination = destination - 1 if destination != 1 else N

    # Place 3 cups back on the right of the destination 
    dest = cups.find(destination)
    cups.slice_in(dest, removed)

    # index is right of the old index
    cups.set_current(cups.current.next)
  return cups

def part1(input):
  cups = deque([int(c) for c in input])
  for _ in range(100):
    current_value = cups[0]
    cups.rotate(-1)

    # Remove 3 cups left (including wrapping) of the index
    removed = [cups.popleft(),cups.popleft(),cups.popleft()]

    # Destination cup is index_value-1 until it can be found (including wrapping)
    destination = current_value - 1 if current_value != 1 else len(cups) + 3
    while destination in removed:
      destination = destination - 1 if destination != 1 else len(cups) + 3

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

def part1a(input):
  cups = play_crab_cups(input)
  return int(cups.get_string(1))

def part2(input):
  cups =  play_crab_cups(input, True)
  node1 = cups.find(1)
  return node1.next.data * node1.next.next.data

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))