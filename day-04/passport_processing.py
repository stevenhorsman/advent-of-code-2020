import re

input_file = 'day-04/input.txt'

class PassportData:

  @staticmethod
  def __is_valid_height(data):
    height, units = list(re.match(r"(\d+)(\w{2})", data).groups())
    return (units == 'cm' and 150 <= int(height) <= 193) or (units == 'in' and 59 <= int(height) <= 76)

  field_validator = {
    'byr': lambda data: 1920 <= int(data) <= 2002,
    'iyr': lambda data: 2010 <= int(data) <= 2020,
    'eyr': lambda data: 2020 <= int(data) <= 2030,
    'hgt': lambda data: PassportData.__is_valid_height(data),
    'hcl': lambda data: re.match('^#(?:[0-9a-fA-F]{1,2}){3}$', data) != None,
    'ecl': lambda data: data in ['amb','blu','brn','gry','grn','hzl','oth'],
    'pid': lambda data: re.match('^^[0-9]{9}$', data)
  }

  def __init__(self, passport_string):
    self.passport_data = dict(field.split(':') for field in passport_string.split())

  def has_all_fields(self):
    return all(key in self.passport_data for key in self.field_validator)

  def is_valid(self):
    return self.has_all_fields() and all(self.field_validator[key](self.passport_data[key]) for key in self.field_validator)

def part1(input):
  return sum(1 for data in [PassportData(passport_string) for passport_string in input.split("\n\n")] if data.has_all_fields())
  # valid = 0
  # for passport_data in passports_data:
  #   if passport_data.has_all_fields():
  #     valid += 1
  # return valid

def part2(input):
  return sum(1 for data in [PassportData(passport_string) for passport_string in input.split("\n\n")] if data.is_valid())
  # valid = 0
  # for passport_string in input.split("\n\n"):
  #   passport_data = PassportData(passport_string)
  #   if passport_data.is_valid():
  #     valid += 1
  # return valid

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))