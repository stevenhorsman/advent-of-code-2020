package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strconv"
	"strings"
)

const input_file string = "./day-13/input.txt"

func ReadInput(input string) (int, map[int]int) {
	lines := strings.Split(strings.TrimSpace(input), "\n")
	timestamp, _ := strconv.Atoi(lines[0])
	schedule := make(map[int]int)
	for i, id := range strings.Split(strings.TrimSpace(lines[1]), ",") {
		if id != "x" {
			bus_id, _ := strconv.Atoi(id)
			schedule[i] = bus_id
		}
	}

	return timestamp, schedule
}

func Part1(input string) int {
	timestamp, schedule := ReadInput(input)

	next_bus_time := math.MaxInt64
	bus_id := -1
	for _, id := range schedule {
		next_bus := id - (timestamp % id)
		if next_bus < next_bus_time {
			next_bus_time = next_bus
			bus_id = id
		}
	}
	return bus_id * next_bus_time
}

// Based on comment https://www.reddit.com/r/adventofcode/comments/kc4njx/2020_day_13_solutions/gfo9bgb/
func Part2(input string) int {
	_, schedule := ReadInput(input)
	time, lcm := 0, 1
	for i, bus_id := range schedule {
		for (time+i)%bus_id != 0 {
			time += lcm
		}
		lcm *= bus_id
	}
	return time
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
