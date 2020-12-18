package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

const input_file string = "./day-18/input.txt"

var bracketRegex = regexp.MustCompile(`\(([^()]+)\)`)

func Calculate(line string, precedence [][]rune) int {
	for strings.Contains(line, "(") {
		indexes := bracketRegex.FindStringIndex(line)
		line = line[:indexes[0]] + strconv.Itoa(Calculate(line[indexes[0]+1:indexes[1]-1], precedence)) + line[indexes[1]:]
	}
	for _, operators := range precedence {
		opStrings := []string{}
		for _, r := range operators {
			opStrings = append(opStrings, string(r))
		}
		var opRegex = regexp.MustCompile(`(\d+ [` + strings.Join(opStrings, "|") + `] \d+)`)
		for opRegex.MatchString(line) {
			indexes := opRegex.FindStringIndex(line)
			line = line[:indexes[0]] + strconv.Itoa(Eval(line[indexes[0]:indexes[1]])) + line[indexes[1]:]
		}
	}
	answer, _ := strconv.Atoi(line)
	return answer
}

func Eval(expression string) int {
	fields := strings.Fields(expression)

	total, _ := strconv.Atoi((fields[0]))
	num2, _ := strconv.Atoi((fields[2]))

	if fields[1] == "+" {
		total += num2
	} else if fields[1] == "*" {
		total *= num2
	}
	return total
}

func Part1(input string) int {
	precedence := [][]rune{{'*', '+'}}
	sum := 0
	for _, line := range strings.Split(strings.TrimSpace(input), "\n") {
		sum += Calculate(line, precedence)
	}
	return sum
}

func Part2(input string) int {
	precedence := [][]rune{{'+'}, {'*'}}
	sum := 0
	for _, line := range strings.Split(strings.TrimSpace(input), "\n") {
		sum += Calculate(line, precedence)
	}
	return sum
}

func main() {
	b, err := ioutil.ReadFile(input_file)
	if err != nil {
		fmt.Print(err)
	}
	data := string(b)

	fmt.Printf("Part 1: %d\n", Part1(data))
	fmt.Printf("Part 2: %d\n", Part2(data))
}
