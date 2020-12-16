import re

input_file = 'day-16/input.txt'

class RuleSet:
  def __init__(self, rule_lines):
    self.length = len(rule_lines)
    self.map = {}
    self.unmapped = []
    for line in rule_lines.splitlines():
      self.unmapped.append(Rule.from_string(line))

  def match(self, order, rule):
    if order in self.map:
      raise ValueError('already matches')
    self.map[order] = rule
    self.unmapped.remove(rule)

  def get_matching_order(self, string_start):
    matching_orders = []
    for order, rule in self.map.items():
      if rule.name.startswith(string_start):
        matching_orders.append(order)
    return matching_orders

class Rule:
  def __init__(self, name, start1, stop1, start2, stop2):
    self.name = name
    self.start1 = start1
    self.stop1 = stop1
    self.start2 = start2
    self.stop2 = stop2

  @classmethod
  def from_string(cls, line):
    name, start1, stop1, start2, stop2 = list(re.match(r"(\w[ \w]*): (\d+)-(\d+) or (\d+)-(\d+)", line).groups())
    return cls(name, *[int(x) for x in [start1, stop1, start2, stop2]])

  def is_valid(self, number):
    return (self.start1 <=number <= self.stop1) or (self.start2 <=number <= self.stop2)

  def __repr__(self):
    return f'{self.name}: ({self.start1}-{self.stop1}), ({self.start2}-{self.stop2})'

def get_sum_invalid_values(tickets, rules):
  return sum(value for ticket in tickets for value in ticket if not any(rule.is_valid(value) for rule in rules))
  # OR
  invalid_total = 0
  for ticket in tickets:
    for value in ticket:
      if not any(rule.is_valid(value) for rule in rules):
        invalid_total += value
  return invalid_total

def part1(input):
  sections = input.split('\n\n')
  rule_set = RuleSet(sections[0])

  other_tickets = [[int(x) for x in other.split(',')] for other in sections[2].splitlines()[1:]]
  return get_sum_invalid_values(other_tickets, rule_set.unmapped)

def get_valid_tickets(tickets, rules):
  return [ticket for ticket in tickets if all(any(rule.is_valid(value) for rule in rules) for value in ticket)]
  # OR 
  valid_tickets = []
  for ticket in tickets:
    valid = True
    for value in ticket:
      valid = valid & any(rule.is_valid(value) for rule in rules)
    if valid:
      valid_tickets.append(ticket)
  return valid_tickets

def calculate_rule_matches(rule_set, tickets):
  while len(rule_set.unmapped) > 0:
    for i in [v for v in range(len(tickets[0])) if v not in rule_set.map]:
      is_rule_valid_for_all_tickets = lambda rule, tickets: all(rule.is_valid(value) for value in [ticket[i] for ticket in tickets])
      matching_rules = [rule for rule in rule_set.unmapped if is_rule_valid_for_all_tickets(rule, tickets)]
      # OR
      # matching_rules = [rule for rule in rule_set.unmapped if all(rule.is_valid(value) for value in [ticket[i] for ticket in tickets])]
      # OR
      # i_values = []
      # for ticket in tickets:
      #   i_values.append(ticket[i])
      # matching_rules = []
      # for rule in rule_set.unmapped:
      #   if all(rule.is_valid(value) for value in i_values):
      #     matching_rules.append(rule)
      if len(matching_rules) == 1:
        rule_set.match(i, matching_rules[0])


def part2(input):
  sections = input.split('\n\n')
  rule_set = RuleSet(sections[0])

  my_ticket = [int(x) for x in sections[1].splitlines()[1].split(',')]

  other_tickets = [[int(x) for x in other.split(',')] for other in sections[2].splitlines()[1:]]
  valid_tickets = get_valid_tickets(other_tickets, rule_set.unmapped)

  calculate_rule_matches(rule_set, valid_tickets)

  product = 1
  for index in rule_set.get_matching_order('departure'):
    product *= my_ticket[index]
  
  return product

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))