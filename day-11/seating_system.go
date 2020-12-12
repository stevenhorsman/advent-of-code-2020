package main

import (
	"fmt"
	"io/ioutil"
	"reflect"
	"strings"
)

const input_file string = "./day-11/input.txt"

type point struct {
	x, y int
}

func (p point) add(d point) point {
	return point{p.x + d.x, p.y + d.y}
}

func (p point) String() string {
	return fmt.Sprintf("(%d, %d)", p.x, p.y)
}

const (
	FLOOR    = '.'
	EMPTY    = 'L'
	OCCUPIED = '#'
)

func ReadInput(input string) map[point]rune {
	grid := map[point]rune{}
	for y, line := range strings.Split(strings.TrimSpace(input), "\n") {
		for x, char := range line {
			grid[point{x, y}] = char
		}
	}
	return grid
}

func CountOccupied(grid map[point]rune) int {
	count := 0
	for _, v := range grid {
		if v == OCCUPIED {
			count++
		}
	}
	return count
}

var deltas = []point{
	{-1, -1},
	{-1, 0},
	{-1, 1},
	{0, -1},
	{0, 1},
	{1, -1},
	{1, 0},
	{1, 1}}

func Converge(grid map[point]rune, part2 bool) int {
	crowded := 4
	if part2 {
		crowded = 5
	}
	for {
		next := map[point]rune{}
		// Run round rules
		for point, seat := range grid {
			neighbours := 0
			for _, d := range deltas {
				adj := point.add(d)
				if part2 {
					for grid[adj] == EMPTY {
						adj = adj.add(d)
					}
				}
				if grid[adj] == OCCUPIED {
					neighbours++
				}
			}
			if seat == OCCUPIED && neighbours >= crowded {
				next[point] = EMPTY
			} else if seat == EMPTY && neighbours == 0 {
				next[point] = OCCUPIED
			} else {
				next[point] = seat
			}
		}
		if reflect.DeepEqual(grid, next) {
			return CountOccupied(grid)
		}
		grid = next
	}
}

func Part1(input string) int {
	grid := ReadInput(input)
	return Converge(grid, false)
}

func Part2(input string) int {
	grid := ReadInput(input)
	return Converge(grid, true)
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
