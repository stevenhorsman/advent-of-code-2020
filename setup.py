import sys
import shutil
import os
import requests
import argparse
from datetime import date

year = 2015

def main():
    parser = argparse.ArgumentParser(description='An advent of code setup script')
    parser.add_argument("-name")
    parser.add_argument("-day", default = date.today().strftime("%d"))

    args = parser.parse_args()
    name = args.name
    day = args.day

    day_string = 'day-' + day.zfill(2)

    print("Creating day %s with name %s" % (day, name))
    
    os.mkdir(day_string)
    create_py_contents(day_string + os.path.sep + name + ".py", day.zfill(2))
    create_test_contents(day_string + os.path.sep + 'test_' + name + ".py", name)

    input_url='https://adventofcode.com/'+str(year)+'/day/'+str(int(day))+'/input'
    session_id = open('session_id', 'r').read()
    cookies = {"session": session_id}
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0"}

    response = requests.get(url=input_url, cookies=cookies, headers=headers)
    response.raise_for_status() # ensure we notice bad responses
    file = open(day_string+os.path.sep+"input.txt", "w")
    file.write(response.text.rstrip("\r\n"))
    file.close()

py_file = """input_file = 'day-{{day}}/input.txt'

def part1(input):
  return 0

def part2(input):
  return 0

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))"""
def create_py_contents(filename, day_no):
    create_file_contents(filename, py_file, '{{day}}', day_no)

test_file = """import {{name}}
import fileinput

def test_part1_example_1():
  data = '''
1122
1232'''[1:]
  assert {{name}}.part1(data) == -1

def test_part1_example_2():
  data = '1111'
  assert {{name}}.part1(data) == -1

def test_part1():
  with open({{name}}.input_file) as f:
    data = f.read()
  expected = -1
  assert {{name}}.part1(data) == expected

def test_part2_example_1():
  data = '''
1122
1232'''[1:]
  assert {{name}}.part2(data) == -1

def test_part2_example_2():
  data = '1221'
  assert {{name}}.part2(data) == -1

def test_part2():
  with open({{name}}.input_file) as f:
    data = f.read()
  expected = -1
  assert {{name}}.part2(data) == expected
"""
def create_test_contents(filename, name):
    create_file_contents(filename, test_file, '{{name}}', name)

def create_file_contents(filename, contents, replaced, replace):
    # Replace the target string
    filedata = contents.replace(replaced, replace)

    # Write the file out again
    with open(filename, 'w') as file:
        file.write(filedata)

if __name__ == '__main__':
    main()