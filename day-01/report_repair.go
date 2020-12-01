package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

const input_file string = "./day-01/input.txt"

func GetInts(input string) []int {
	var numbers []int
	split := strings.Split(strings.TrimSpace(input), "\n")
	for _, num := range split {
		float, _ := strconv.Atoi(num)
		numbers = append(numbers, float)
	}
	return numbers
}

func Part1(input string) int {
	entries := GetInts(input)

	for i, e1 := range entries {
		for _, e2 := range entries[i:] {
			if e1+e2 == 2020 {
				return e1 * e2
			}
		}
	}
	return 0
}

func Part2(input string) int {
	entries := GetInts(input)

	for i, e1 := range entries {
		for j, e2 := range entries[i:] {
			for _, e3 := range entries[j:] {
				if e1+e2+e3 == 2020 {
					return e1 * e2 * e3
				}
			}
		}
	}
	return 0
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
