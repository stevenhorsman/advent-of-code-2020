package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strconv"
	"strings"
)

const input_file string = "./day-05/input.txt"

func ParseInput(input string) []int {
	seat_ids := []int{}
	replacer := strings.NewReplacer("F", "0", "B", "1", "L", "0", "R", "1")
	lines := strings.Split(strings.TrimSpace(input), "\n")
	for _, line := range lines {
		seat_id, _ := strconv.ParseInt(replacer.Replace(line), 2, 0)
		seat_ids = append(seat_ids, int(seat_id))
	}
	sort.Ints(seat_ids)
	return seat_ids
}

func Part1(input string) int {
	seat_ids := ParseInput(input)
	return seat_ids[len(seat_ids)-1]
}

func Part2(input string) int {
	seat_ids := ParseInput(input)
	for i, value := range seat_ids {
		if seat_ids[i+1] != value+1 {
			return value + 1
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
