import argparse
from datetime import date
import os
import requests

def download_input(year, day, filename):
  input_url='https://adventofcode.com/'+str(year)+'/day/'+str(int(day))+'/input'
  session_id = open('session_id', 'r').read()
  cookies = {"session": session_id}
  headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0"}

  response = requests.get(url=input_url, cookies=cookies, headers=headers)
  response.raise_for_status() # ensure we notice bad responses
  file = open(filename, "w")
  file.write(response.text.rstrip("\r\n"))
  file.close()

def create_py(directory, name, day):
  create_py_contents(directory + os.path.sep + name + ".py", day.zfill(2))
  create_test_contents(directory + os.path.sep + 'test_' + name + ".py", name)

def create_go(directory, name, day):
  create_go_contents(directory + os.path.sep + name + ".go", day.zfill(2))
  create_go_test_contents(directory + os.path.sep + name + "_test.go")

def main():
  parser = argparse.ArgumentParser(description='An advent of code setup script')
  parser.add_argument("-name")
  parser.add_argument("-day", default = date.today().strftime("%d"))
  parser.add_argument("-year", default = date.today().strftime("%Y"))
  parser.add_argument("-go", action='store_true')

  args = parser.parse_args()
  name = args.name
  day = args.day
  year = args.year
  is_go = args.go

  day_string = 'day_' + day.zfill(2)
  if not is_go:
    print("Creating day %s with name %s" % (day, name))

    os.mkdir(day_string)
    create_py(day_string, name, day)
    download_input(year, day, day_string+os.path.sep+"input.txt")
  else:
    create_go(day_string, name, day)

PY_FILE = """INPUT_FILE = 'day_{{day}}/input.txt'

def part1(input_string):
  return 0

def part2(input_string):
  return 0

if __name__ == "__main__":
  with open(INPUT_FILE) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))"""
def create_py_contents(filename, day_no):
  create_file_contents(filename, PY_FILE, '{{day}}', day_no)

TEST_FILE = """import {{name}}
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
  with open({{name}}.INPUT_FILE) as f:
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
  with open({{name}}.INPUT_FILE) as f:
    data = f.read()
  expected = -1
  assert {{name}}.part2(data) == expected
"""
def create_test_contents(filename, name):
  create_file_contents(filename, TEST_FILE, '{{name}}', name)

GO_FILE = """package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

const inputFile string = "./day_{{day}}/input.txt"

//Part1 - Solution to Part 1 of the puzzle
func Part1(input string) int {
	return 0
}

//Part2 - Solution to Part 2 of the puzzle
func Part2(input string) int {
	return 0
}

func main() {
	b, err := ioutil.ReadFile(inputFile)
	if err != nil {
		fmt.Print(err)
	}
	data := string(b)

	fmt.Printf("Part 1: %d\\n", Part1(data))
	fmt.Printf("Part 2: %d\\n", Part2(data))
}"""

def create_go_contents(filename, day_no):
  create_file_contents(filename, GO_FILE, '{{day}}', day_no)

GO_TEST_FILE = """package main

import (
	"fmt"
	"io/ioutil"
	"testing"
)

func TestPart1Example1(t *testing.T) {
	data := `
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc`[1:]
	expected := -1
	actual := Part1(data)
	if actual != expected {
		t.Errorf("Expected %d but was %d\\n", expected, actual)
	}
}

func TestPart1(t *testing.T) {
	bytes, err := ioutil.ReadFile("./input.txt")
	if err != nil {
		fmt.Print(err)
	}
	data := string(bytes)

	expected := -1
	actual := Part1(data)
	if actual != expected {
		t.Errorf("Expected %d but was %d\\n", expected, actual)
	}
}

func TestPart2Example1(t *testing.T) {
	data := `
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc`[1:]
	expected := -1
	actual := Part2(data)
	if actual != expected {
		t.Errorf("Expected %d but was %d\\n", expected, actual)
	}
}

func TestPart2(t *testing.T) {
	bytes, err := ioutil.ReadFile("./input.txt")
	if err != nil {
		fmt.Print(err)
	}
	data := string(bytes)

	expected := -1
	actual := Part2(data)
	if actual != expected {
		t.Errorf("Expected %d but was %d\\n", expected, actual)
	}
}

func BenchmarkPart2(b *testing.B) {
	bytes, err := ioutil.ReadFile("./input.txt")
	if err != nil {
		fmt.Print(err)
	}
	data := string(bytes)
	b.ResetTimer()
	for n := 0; n < b.N; n++ {
		Part2(data)
	}
}"""

def create_go_test_contents(filename):
  create_file_contents(filename, GO_TEST_FILE, "<none>", "<none>")

def create_file_contents(filename, contents, replaced, replace):
  # Replace the target string
  filedata = contents.replace(replaced, replace)

  # Write the file out again
  with open(filename, 'w') as file:
    file.write(filedata)

if __name__ == '__main__':
  main()
