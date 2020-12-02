package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

const input_file string = "./day-02/input.txt"

type is_valid func(int, int, byte, string) bool

func CountValidPasswords(input string, valid_fn is_valid) int {
	totalValid := 0
	lines := strings.Split(strings.TrimSpace(input), "\n")
	lineMatcher := regexp.MustCompile(`^(\d+)-(\d+) (\w): (\w+)$`)
	for _, line := range lines {
		matches := lineMatcher.FindStringSubmatch(line)
		min, err := strconv.Atoi(matches[1])
		if err != nil {
			panic(err)
		}
		max, err := strconv.Atoi(matches[2])
		if err != nil {
			panic(err)
		}
		if valid_fn(min, max, matches[3][0], matches[4]) {
			totalValid++
		}
	}
	return totalValid
}

func IsValidPart1(min int, max int, char byte, pattern string) bool {
	charCount := 0
	for i := range pattern {
		if pattern[i] == char {
			charCount++
		}
	}
	return charCount >= min && charCount <= max
}

func Part1(input string) int {
	return CountValidPasswords(input, IsValidPart1)
}

func IsValidPart2(min int, max int, char byte, pattern string) bool {
	return (pattern[min-1] == char) != (pattern[max-1] == char)
}

func Part2(input string) int {
	return CountValidPasswords(input, IsValidPart2)
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
