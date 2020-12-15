package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

const input_file string = "./day-15/input.txt"

func ReadInput(input string) []int {
	numbers := []int{}
	for _, numString := range strings.Split(strings.TrimSpace(input), ",") {
		num, _ := strconv.Atoi(numString)
		numbers = append(numbers, num)
	}
	return numbers
}

func VanEck(input string, iterations int) int {
	last_seen := make(map[int]int)
	previous := 0
	for i, previous := range ReadInput(input) {
		last_seen[previous] = i + 1
	}

	for i := len(last_seen) + 1; i < iterations; i++ {
		next := 0
		if last, found := last_seen[previous]; found {
			next = i - last
		}
		last_seen[previous] = i
		previous = next
	}
	return previous
}

func Part1(input string) int {
	return VanEck(input, 2020)
}

func Part2(input string) int {
	return VanEck(input, 30000000)
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
