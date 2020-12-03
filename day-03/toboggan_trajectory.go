package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

const input_file string = "./day-03/input.txt"

func CountTrees(lines []string, right int, down int) int {
	width := len(lines[0])
	trees := 0
	col := 0
	for i := 0; i < len(lines); i += down {
		if lines[i][col] == '#' {
			trees++
		}
		col = (col + right) % width
	}
	return trees
}

func Part1(input string) int {
	lines := strings.Split(strings.TrimSpace(input), "\n")
	return CountTrees(lines, 3, 1)
}

func Part2(input string) int {
	lines := strings.Split(strings.TrimSpace(input), "\n")
	product := 1
	slopes := [][]int{
		{1, 1},
		{3, 1},
		{5, 1},
		{7, 1},
		{1, 2},
	}
	for _, slope := range slopes {
		product *= CountTrees(lines, slope[0], slope[1])
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
