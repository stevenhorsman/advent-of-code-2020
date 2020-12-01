package main

import (
	"fmt"
	"io/ioutil"
	"sort"
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

func FindProductOfPair(entries []int, target int) int {
	product := -1

	// Brute force method:
	// for i, e1 := range entries {
	// 	for _, e2 := range entries[i:] {
	// 		if e1+e2 == target {
	// 			product = e1 * e2
	// 		}
	// 	}
	// }

	// Better implementation from https://github.com/crshnburn/adventofcode2020/blob/main/day1/day1.go
	sort.Ints(entries)
	for _, e := range entries {
		remainder := target - e
		index := sort.SearchInts(entries, remainder)
		if index < len(entries) && entries[index] == remainder {
			product = remainder * e
			break
		}
	}
	return product
}

func Part1(input string) int {
	entries := GetInts(input)
	return FindProductOfPair(entries, 2020)
}

func Part2(input string) int {
	entries := GetInts(input)
	product := -1
	for _, e := range entries {
		pairProduct := FindProductOfPair(entries, 2020-e)
		if pairProduct != -1 {
			product = e * pairProduct
			break
		}
	}
	return product
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
