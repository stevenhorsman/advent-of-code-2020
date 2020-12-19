import re

input_file = 'day-19/input.txt'

def parse_rules_section(rule_strings):
  rules = {}
  for rule in rule_strings.splitlines():
    num, rule_string = rule.split(':', 1)
    if '"' in rule_string:
      rules[int(num)] = rule_string.strip().replace('"','')
    else:
      rules[int(num)] = [[int(s) for s in rule_split.split()] for rule_split in rule_string.split('|')]
  return rules

def resolve_rule(rules, rule_no, part2):
  rule = rules[rule_no]
  if isinstance(rule, str):
    return rule
  if part2:
    if rule_no == 8:
      return resolve_rule(rules, 42, part2) + '+'
    elif rule_no == 11:
      rule_42 = resolve_rule(rules, 42, part2)
      rule_31 = resolve_rule(rules, 31, part2)
      repeat_matches = []
      for i in range(1,5):
        repeat_matches.append(rule_42+'{'+str(i) +'}' + rule_31 + '{'+str(i) +'}')
      return '(?:' + '|'.join(repeat_matches) + ')'
  if len(rule) == 1 and len(rule[0]) == 1 and isinstance(rule[0], str):
    rules[rule_no] = rule[0]
  else:
    resolved_parts = []
    for or_rules in rule:
      resolved = []
      for linked_rule in or_rules:
        resolved.append(resolve_rule(rules, linked_rule, part2))
      resolved_parts.append(''.join(resolved))
    rules[rule_no] = '(?:' + '|'.join(resolved_parts) + ')'
  return rules[rule_no]

def count_matches(input, part2 = False):
  sections = input.split('\n\n')

  rules_dict = parse_rules_section(sections[0])
  rule_0 = resolve_rule(rules_dict, 0, part2)
  
  return sum(1 for message in sections[1].splitlines() if re.fullmatch(rule_0, message) != None)

def part1(input):
  return count_matches(input)
  
def part2(input):
  return count_matches(input, True)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))