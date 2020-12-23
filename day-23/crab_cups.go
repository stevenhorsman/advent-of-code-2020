package main

import (
	"container/ring"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

const inputFile string = "./day-23/input.txt"

func processInput(input string) (numbers []int) {
	for _, c := range strings.TrimSpace(input) {
		n, _ := strconv.Atoi(string(c))
		numbers = append(numbers, n)
	}
	return
}

// Heavy inspiration from https://github.com/mnml/aoc/blob/master/2020/23/2.go
func playCrabCups(input []int, noCups int, noMoves int) map[int]*ring.Ring {
	cups := ring.New(noCups)
	lookUp := make(map[int]*ring.Ring, noCups)

	//TODO - merge two loops?
	for _, i := range input {
		cups.Value = i
		lookUp[i] = cups
		cups = cups.Next()
	}

	for i := len(input) + 1; i <= noCups; i++ {
		cups.Value = i
		lookUp[i] = cups
		cups = cups.Next()
	}

	for i := 0; i < noMoves; i++ {
		currentValue := cups.Value.(int)

		// Remove 3 cups left (including wrapping) of the index
		removed := cups.Unlink(3)

		// Destination cup is index_value-1 until it can be found (including wrapping)
		destination := currentValue - 1
		if destination == 0 {
			destination = noCups
		}

		removedValues := map[int]bool{}
		for j := 0; j < 3; j++ {
			removedValues[removed.Value.(int)] = true
			removed = removed.Next()
		}

		for removedValues[destination] {
			destination--
			if destination == 0 {
				destination = noCups
			}
		}

		// Place 3 cups back on the right of the destination
		lookUp[destination].Link(removed)

		// index is right of the old index
		cups = cups.Next()
	}
	return lookUp
}

//Part1 - Solution to Part 1 of the puzzle
func Part1(input string) int {
	numbers := processInput(input)
	lookUp := playCrabCups(numbers, len(numbers), 100)

	out := 0
	lookUp[1].Do(func(v interface{}) {
		val := v.(int)
		if val == 1 {
			return
		}
		out = out*10 + val
	})
	return out
}

//Part2 - Solution to Part 2 of the puzzle
func Part2(input string) int {
	numbers := processInput(input)
	lookUp := playCrabCups(numbers, 1_000_000, 10_000_000)
	return lookUp[1].Next().Value.(int) * lookUp[1].Next().Next().Value.(int)
}

func main() {
	b, err := ioutil.ReadFile(inputFile)
	if err != nil {
		fmt.Print(err)
	}
	data := string(b)

	fmt.Printf("Part 1: %d\n", Part1(data))
	fmt.Printf("Part 2: %d\n", Part2(data))
}
