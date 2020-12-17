package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

const input_file string = "./day-17/input.txt"

const ACTIVE = '#'

type Point struct {
	x, y, z, w int
	dimension  int
}

func (p Point) add(d []int) Point {
	// Pad out with zeros if not 4-dimensions
	for i := len(d); i < 4; i++ {
		d = append(d, 0)
	}
	return Point{p.x + d[0], p.y + d[1], p.z + d[2], p.w + d[3], p.dimension}
}

func (p Point) GetNeighbours() map[Point]bool {
	neighbours := make(map[Point]bool)
	for _, delta := range GetDeltas(p.dimension) {
		neighbours[p.add(delta)] = true
	}
	return neighbours
}

func GetRangeOfPoints(dimension int) [][]int {
	deltas := [][]int{}
	if dimension == 1 {
		return [][]int{{0}, {-1}, {1}}
	}
	for _, v := range []int{0, -1, 1} {
		for _, p := range GetRangeOfPoints(dimension - 1) {
			p = append(p, v)
			deltas = append(deltas, p)
		}
	}
	return deltas
}

func GetDeltas(dimension int) [][]int {
	deltas := GetRangeOfPoints(dimension)
	// Ignore all zeros. TODO - do this better
	return deltas[1:]
}

func ParseInputSet(input string, dimension int) map[Point]bool {
	active := make(map[Point]bool)
	for y, line := range strings.Split(strings.TrimSpace(input), "\n") {
		for x, r := range line {
			if r == ACTIVE {
				active[Point{x, y, 0, 0, dimension}] = true
			}
		}
	}
	return active
}

func CountNeighbours(point Point, active map[Point]bool) int {
	neighbourCount := 0
	for neighbour, _ := range point.GetNeighbours() {
		if _, found := active[neighbour]; found {
			neighbourCount++
		}
	}
	return neighbourCount
}

func Evolve(input string, iteration int, dimension int) int {
	active := ParseInputSet(input, dimension)
	for i := 0; i < iteration; i++ {
		pointsToCheck := make(map[Point]bool)
		for point, _ := range active {
			pointsToCheck[point] = true
			for neighbour, _ := range point.GetNeighbours() {
				pointsToCheck[neighbour] = true
			}
		}
		nextGen := make(map[Point]bool)
		for point, _ := range pointsToCheck {
			neighbourCount := CountNeighbours(point, active)
			if _, found := active[point]; found {
				if neighbourCount == 2 {
					nextGen[point] = true
				}
			}
			if neighbourCount == 3 {
				nextGen[point] = true
			}
		}
		active = nextGen
	}
	return len(active)
}

func Part1(input string, iterations int) int {
	return Evolve(input, iterations, 3)
}

func Part2(input string) int {
	return Evolve(input, 6, 4)
}

func main() {
	b, err := ioutil.ReadFile(input_file)
	if err != nil {
		fmt.Print(err)
	}
	data := string(b)

	fmt.Printf("Part 1: %d\n", Part1(data, 6))
	fmt.Printf("Part 2: %d\n", Part2(data))
}
