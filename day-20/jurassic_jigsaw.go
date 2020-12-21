package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strings"
)

const inputFile string = "./day-20/input.txt"

type edge struct {
	normal, reverse, id string
}

type edges struct {
	north, east, south, west edge
}

func reverse(input string) (result string) {
	for _, v := range input {
		result = string(v) + result
	}
	return
}

func createEdge(normal string) edge {
	reverse := reverse(normal)
	id := normal
	if reverse < id {
		id = reverse
	}
	return edge{normal: normal, reverse: reverse, id: id}
}

func getColumn(grid []string, col int) (column string) {
	for _, row := range grid {
		column += string(row[col])
	}
	return
}

func createEdges(grid []string) (edges edges) {
	edges.north = createEdge(grid[0])
	edges.east = createEdge(getColumn(grid, len(grid[0])-1))
	edges.south = createEdge(grid[len(grid)-1])
	edges.west = createEdge(getColumn(grid, 0))
	return
}

type tile struct {
	id      int
	grid    []string
	flipped bool
	rotated int
	edges   edges
}

func (t tile) rotateClockwise() tile {
	rotated := []string{}
	for i := range t.grid {
		rowI := reverse(getColumn(t.grid, i))
		rotated = append(rotated, rowI)
	}
	rotatedEdges := edges{north: t.edges.west, east: t.edges.north, south: t.edges.east, west: t.edges.south}
	return tile{id: t.id, flipped: t.flipped, grid: rotated, rotated: (t.rotated + 1) % 4, edges: rotatedEdges}
}

func (t tile) flipHorizontal() tile {
	flipped := []string{}
	for _, row := range t.grid {
		flipped = append(flipped, reverse(row))
	}
	flippedEdges := edges{north: t.edges.north, east: t.edges.west, south: t.edges.south, west: t.edges.east}
	return tile{id: t.id, flipped: !t.flipped, grid: flipped, rotated: t.rotated, edges: flippedEdges}
}

// Rotate until we've done it 3 time, then reset and flip
func (t tile) getNextArrangement() tile {
	if t.rotated < 3 {
		return t.rotateClockwise()
	}
	return t.rotateClockwise().flipHorizontal()
}

func createTile(tileString string) (int, tile) {
	lines := strings.Split(strings.TrimSpace(tileString), "\n")
	var id int
	fmt.Sscanf(lines[0], "Tile %d:", &id)
	return id, tile{id: id, flipped: false, grid: lines[1:], rotated: 0, edges: createEdges(lines[1:])}
}

func processInput(input string) map[int]tile {
	tiles := make(map[int]tile)
	tileStrings := strings.Split(strings.TrimSpace(input), "\n\n")
	for _, tileString := range tileStrings {
		id, tile := createTile(tileString)
		tiles[id] = tile
	}
	return tiles
}

//Part1 - Solution to Part 1 of the puzzle
func Part1(input string) int {
	tiles := processInput(input)
	edgeMap := make(map[string][]int)
	for id, tile := range tiles {
		edges := tile.edges
		edgeMap[edges.north.id] = append(edgeMap[edges.north.id], id)
		edgeMap[edges.east.id] = append(edgeMap[edges.east.id], id)
		edgeMap[edges.south.id] = append(edgeMap[edges.south.id], id)
		edgeMap[edges.west.id] = append(edgeMap[edges.west.id], id)
	}

	openEdgeCount := map[int]int{}
	for _, tiles := range edgeMap {
		if len(tiles) == 1 {
			openEdgeCount[tiles[0]]++
		}
	}

	product := 1
	for id, count := range openEdgeCount {
		if count == 2 {
			product *= id
		}
	}
	return product
}

//Part2 - Solution to Part 2 of the puzzle
func Part2(input string) int {
	tiles := processInput(input)
	edgeMap := make(map[string][]int)
	for id, tile := range tiles {
		edges := tile.edges
		edgeMap[edges.north.id] = append(edgeMap[edges.north.id], id)
		edgeMap[edges.east.id] = append(edgeMap[edges.east.id], id)
		edgeMap[edges.south.id] = append(edgeMap[edges.south.id], id)
		edgeMap[edges.west.id] = append(edgeMap[edges.west.id], id)
	}

	openEdgeCount := map[int]int{}
	for _, tiles := range edgeMap {
		if len(tiles) == 1 {
			openEdgeCount[tiles[0]]++
		}
	}

	corners := []int{}
	edges := []int{}
	for id, count := range openEdgeCount {
		switch count {
		case 1:
			edges = append(edges, id)
		case 2:
			corners = append(corners, id)
		}
	}

	gridLength := int(math.Ceil(math.Sqrt(float64(len(tiles)))))
	layout := [][]tile{}

	// Pick top_left corner such that it has non-open edge to east and south
	topLeft := tiles[corners[0]]
	for len(edgeMap[topLeft.edges.east.id]) == 1 || len(edgeMap[topLeft.edges.south.id]) == 1 {
		topLeft = topLeft.getNextArrangement()
	}

	for row := 0; row < gridLength; row++ {
		layout = append(layout, []tile{})
		for col := 0; col < gridLength; col++ {
			if row == 0 && col == 0 {
				layout[row] = append(layout[row], topLeft)
				delete(tiles, topLeft.id)
			}
		}
	}

	return 0
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
