package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strings"
)

const input_file string = "./day-12/input.txt"

const (
	NORTH   = 'N'
	EAST    = 'E'
	SOUTH   = 'S'
	WEST    = 'W'
	FORWARD = 'F'
	LEFT    = 'L'
	RIGHT   = 'R'
)

type action struct {
	direction rune
	length    int
}

type point struct {
	x, y int
}

func (p point) Add(d point) point {
	return point{p.x + d.x, p.y + d.y}
}

func (p point) Scale(scale int) point {
	return point{p.x * scale, p.y * scale}
}

func (p point) Rotate(r point) point {
	return point{p.y * r.y, p.x * r.x}
}

func (p point) GetManhatten() int {
	return int(math.Abs(float64(p.x))) + int(math.Abs(float64(p.y)))
}

func ReadInput(input string) []action {
	actions := []action{}
	for _, line := range strings.Split(strings.TrimSpace(input), "\n") {
		curr_action := action{}
		fmt.Sscanf(line, "%c%d", &curr_action.direction, &curr_action.length)
		actions = append(actions, curr_action)
	}
	return actions
}

var directions = map[rune]point{
	NORTH: {0, 1},
	EAST:  {1, 0},
	SOUTH: {0, -1},
	WEST:  {-1, 0}}

var rotations = map[rune]point{
	LEFT:  {1, -1},
	RIGHT: {-1, 1}}

func Part1(input string) int {
	ship := point{0, 0}
	heading := directions[EAST]

	for _, action := range ReadInput(input) {
		switch action.direction {
		case FORWARD:
			ship = ship.Add(heading.Scale(action.length))
		case LEFT, RIGHT:
			for r := action.length; r > 0; r -= 90 {
				heading = heading.Rotate(rotations[action.direction])
			}
		case NORTH, EAST, SOUTH, WEST:
			course_change := directions[action.direction].Scale(action.length)
			ship = ship.Add(course_change)
		}
	}
	return ship.GetManhatten()
}

func Part2(input string) int {
	ship := point{0, 0}
	waypoint := point{10, 1}

	for _, action := range ReadInput(input) {
		switch action.direction {
		case FORWARD:
			ship = ship.Add(waypoint.Scale(action.length))
		case LEFT, RIGHT:
			for r := action.length; r > 0; r -= 90 {
				waypoint = waypoint.Rotate(rotations[action.direction])
			}
		case NORTH, EAST, SOUTH, WEST:
			course_change := directions[action.direction].Scale(action.length)
			waypoint = waypoint.Add(course_change)
		}
	}
	return ship.GetManhatten()
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
