package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strings"
)

const inputFile string = "./day-24/input.txt"

type point struct {
	x, y, z int
}

func (p point) add(d point) point {
	return point{p.x + d.x, p.y + d.y, p.z + d.z}
}

func (p point) getNeighbours() map[point]bool {
	neighbours := make(map[point]bool)
	for _, delta := range deltas {
		neighbours[p.add(delta)] = true
	}
	return neighbours
}

var deltas = map[string]point{
	"e":  {1, -1, 0},
	"ne": {1, 0, -1},
	"nw": {0, 1, -1},
	"w":  {-1, 1, 0},
	"se": {0, -1, 1},
	"sw": {-1, 0, 1},
}

var dirRegex = regexp.MustCompile("(ne|nw|se|sw|e|w)")

func processLine(line string) []string {
	return dirRegex.FindAllString(line, -1)
}

func getFlipped(input string) map[point]bool {
	flipped := make(map[point]bool)
	for _, line := range strings.Split(strings.TrimSpace(input), "\n") {
		point := point{0, 0, 0}
		directions := processLine(line)
		for _, dir := range directions {
			point = point.add(deltas[dir])
		}
		if _, found := flipped[point]; found {
			delete(flipped, point)
		} else {
			flipped[point] = true
		}
	}
	return flipped
}

func countNeighbours(p point, active map[point]bool) int {
	neighbourCount := 0
	for neighbour := range p.getNeighbours() {
		if _, found := active[neighbour]; found {
			neighbourCount++
		}
	}
	return neighbourCount
}

//Part1 - Solution to Part 1 of the puzzle
func Part1(input string) int {
	flipped := getFlipped(input)
	return len(flipped)
}

//Part2 - Solution to Part 2 of the puzzle
func Part2(input string) int {
	flipped := getFlipped(input)
	for i := 0; i < 100; i++ {
		pointsToCheck := make(map[point]bool)
		for point := range flipped {
			pointsToCheck[point] = true
			for neighbour := range point.getNeighbours() {
				pointsToCheck[neighbour] = true
			}
		}
		nextGen := make(map[point]bool)
		for point := range pointsToCheck {
			neighbourCount := countNeighbours(point, flipped)
			if _, found := flipped[point]; found {
				if neighbourCount == 1 {
					nextGen[point] = true
				}
			}
			if neighbourCount == 2 {
				nextGen[point] = true
			}
		}
		flipped = nextGen
	}
	return len(flipped)
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
