import re

input_file = 'day-04/input.txt'

def is_valid_height(data):
  height, units = list(re.match(r"(\d+)(\w{2})", data).groups())
  return (units == 'cm' and 150 <= int(height) <= 193) or (units == 'in' and 59 <= int(height) <= 76)

field_validator = {
    'byr': lambda data: 1920 <= int(data) <= 2002,
    'iyr': lambda data: 2010 <= int(data) <= 2020,
    'eyr': lambda data: 2020 <= int(data) <= 2030,
    'hgt': lambda data: is_valid_height(data),
    'hcl': lambda data: re.match('^#(?:[0-9a-fA-F]{1,2}){3}$', data) != None,
    'ecl': lambda data: data in ['amb','blu','brn','gry','grn','hzl','oth'],
    'pid': lambda data: re.match('^^[0-9]{9}$', data)
}

def has_all_fields(passport_data):
  return all(key in passport_data for key in field_validator)

def part1(input):
  valid = 0
  for passport_string in input.split("\n\n"):
    passport_data = dict(field.split(':') for field in passport_string.split())
    if has_all_fields(passport_data):
      valid += 1
  return valid

def is_valid(passport_data):
  return has_all_fields(passport_data) and all(field_validator[key](passport_data[key]) for key in field_validator)

def part2(input):
  valid = 0
  for passport_string in input.split("\n\n"):
    passport_data = dict(field.split(':') for field in passport_string.split())
    if is_valid(passport_data):
      valid += 1
  return valid

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))