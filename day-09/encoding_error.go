package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strconv"
	"strings"
)

const input_file string = "./day-09/input.txt"

func GetInts(input string) []int {
	var numbers []int
	split := strings.Split(strings.TrimSpace(input), "\n")
	for _, num := range split {
		float, _ := strconv.Atoi(num)
		numbers = append(numbers, float)
	}
	return numbers
}

func FindFirstNonSum(numbers []int, window int) int {
	for i := window; i < len(numbers); i++ {
		foundSum := false
		for j := i - window; j < i; j++ {
			for k := j + 1; k < i; k++ {
				if numbers[j]+numbers[k] == numbers[i] {
					foundSum = true
				}
			}
		}
		if !foundSum {
			return numbers[i]
		}
	}
	return -1
}

func Part1(input string, window int) int {
	entries := GetInts(input)
	return FindFirstNonSum(entries, window)
}

func Part2(input string, window int) int {
	entries := GetInts(input)
	target := FindFirstNonSum(entries, window)

	low := 0
	high := 1
	for high < len(entries) {
		sum := 0
		for _, v := range entries[low : high+1] {
			sum += v
		}
		if sum == target {
			sort.Ints(entries[low : high+1])
			return entries[low] + entries[high]
		} else if sum < target {
			high++
		} else {
			low++
		}
	}

	return -1
}

func main() {
	b, err := ioutil.ReadFile(input_file)
	if err != nil {
		fmt.Print(err)
	}
	data := string(b)

	fmt.Printf("Part 1: %d\n", Part1(data, 25))
	fmt.Printf("Part 2: %d\n", Part2(data, 25))
}
