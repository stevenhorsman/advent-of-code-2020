import collections, re

input_file = 'day-07/input.txt'

def calculate_answer(input, answer_func):
  parents = collections.defaultdict(set)
  children = collections.defaultdict(list)
  for line in input.splitlines():
    parent_colour = re.match(r'(\w+ \w+) bags contain', line)[1]
    for quantity, colour in re.findall(r'(\d+) (\w+ \w+) bags?[,.]', line):
      parents[colour].add(parent_colour)
      children[parent_colour].append((int(quantity), colour))
  return answer_func(parents, children)

def find_ancestors(node, parents):
  ancestors = set()
  for parent in parents[node]:
    ancestors.add(parent)
    ancestors = ancestors.union(find_ancestors(parent, parents))
  return ancestors

def part1(input):
  gold_ancestors = lambda parents, children: len(find_ancestors('shiny gold', parents))
  return calculate_answer(input, gold_ancestors)

def count_children(node, children):
  descendants = 0
  for quantity, child in children[node]:
    descendants += quantity
    descendants += (quantity * count_children(child, children))
  return descendants

def part2(input):
  gold_contents = lambda parents, children: count_children('shiny gold', children)
  return calculate_answer(input, gold_contents)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))