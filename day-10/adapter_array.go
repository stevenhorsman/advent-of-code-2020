package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strconv"
	"strings"
)

const input_file string = "./day-10/input.txt"

func GetInts(input string) []int {
	var numbers []int
	split := strings.Split(strings.TrimSpace(input), "\n")
	for _, num := range split {
		float, _ := strconv.Atoi(num)
		numbers = append(numbers, float)
	}
	return numbers
}

func GetJolts(input string) []int {
	jolts := GetInts(input)
	jolts = append(jolts, 0)
	sort.Ints(jolts)
	return append(jolts, jolts[len(jolts)-1]+3)
}

func Part1(input string) int {
	jolts := GetJolts(input)
	diffs := make(map[int]int)
	for i := 0; i < len(jolts)-1; i++ {
		diffs[jolts[i+1]-jolts[i]]++
	}
	return diffs[1] * diffs[3]
}

func Part2(input string) int {
	jolts := GetJolts(input)
	paths_so_far := map[int]int{0: 1} // Initialise first value to have single path
	for _, j := range jolts[1:] {
		// jolts[j] can be got to from any value within 3 below it
		paths_so_far[j] = paths_so_far[j-1] + paths_so_far[j-2] + paths_so_far[j-3]
	}
	max := jolts[len(jolts)-1]
	return paths_so_far[max]
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
