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

func (e edge) flip() edge {
	return edge{normal: e.reverse, reverse: e.normal, id: e.id}
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

//Tile - struct to store info and functions of an image tile
type Tile struct {
	id      int
	grid    []string
	flipped bool
	rotated int
	edges   edges
}

//RotateClockwise - produces a new tile, which is the original rotated by 90 degrees clockwise
func (t Tile) RotateClockwise() Tile {
	rotated := []string{}
	for i := range t.grid {
		rowI := reverse(getColumn(t.grid, i))
		rotated = append(rotated, rowI)
	}
	rotatedEdges := edges{north: t.edges.west.flip(), east: t.edges.north, south: t.edges.east.flip(), west: t.edges.south}
	return Tile{id: t.id, flipped: t.flipped, grid: rotated, rotated: (t.rotated + 1) % 4, edges: rotatedEdges}
}

//FlipVertical - produces a new tile, which is the original mirrored along the vertical axis
func (t Tile) FlipVertical() Tile {
	flipped := []string{}
	for _, row := range t.grid {
		flipped = append(flipped, reverse(row))
	}
	flippedEdges := edges{north: t.edges.north.flip(), east: t.edges.west, south: t.edges.south.flip(), west: t.edges.east}
	return Tile{id: t.id, flipped: !t.flipped, grid: flipped, rotated: t.rotated, edges: flippedEdges}
}

// Rotate until we've done it 3 time, then reset and flip
func (t Tile) getTrimmed() []string {
	border := 1
	tileWidth := len(t.grid[0])
	trimmed := []string{}
	for i := border; i < len(t.grid)-border; i++ {
		trimmed = append(trimmed, t.grid[i][border:tileWidth-border])
	}
	return trimmed
}

func (t Tile) countStrings(search string) int {
	count := 0
	// searchRegex := regexp.MustCompile(search)
	for _, str := range t.grid {
		// matches := searchRegex.FindAllStringIndex(str, -1)
		// count += len(matches)
		count += strings.Count(str, search)
	}
	return count
}

// Rotate until we've done it 3 time, then reset and flip
func (t Tile) getNextArrangement() Tile {
	if t.rotated < 3 {
		return t.RotateClockwise()
	}
	return t.RotateClockwise().FlipVertical()
}

//CreateTile - created a tile object from a string
func CreateTile(tileString string) (int, Tile) {
	lines := strings.Split(strings.TrimSpace(tileString), "\n")
	var id int
	fmt.Sscanf(lines[0], "Tile %d:", &id)
	return id, Tile{id: id, flipped: false, grid: lines[1:], rotated: 0, edges: createEdges(lines[1:])}
}

func processInput(input string) map[int]Tile {
	tiles := make(map[int]Tile)
	tileStrings := strings.Split(strings.TrimSpace(input), "\n\n")
	for _, tileString := range tileStrings {
		id, tile := CreateTile(tileString)
		tiles[id] = tile
	}
	return tiles
}

func createEdgeMap(tiles map[int]Tile) map[string][]int {
	edgeMap := make(map[string][]int)
	for id, tile := range tiles {
		edges := tile.edges
		edgeMap[edges.north.id] = append(edgeMap[edges.north.id], id)
		edgeMap[edges.east.id] = append(edgeMap[edges.east.id], id)
		edgeMap[edges.south.id] = append(edgeMap[edges.south.id], id)
		edgeMap[edges.west.id] = append(edgeMap[edges.west.id], id)
	}
	return edgeMap
}

func identifyCornerIds(edgeMap map[string][]int) (corners []int) {
	openEdgeCount := map[int]int{}
	for _, tiles := range edgeMap {
		if len(tiles) == 1 {
			openEdgeCount[tiles[0]]++
		}
	}

	for id, count := range openEdgeCount {
		if count == 2 {
			corners = append(corners, id)
		}
	}
	return
}

func calculateLayout(tiles map[int]Tile) [][]Tile {
	edgeMap := createEdgeMap(tiles)

	gridLength := int(math.Ceil(math.Sqrt(float64(len(tiles)))))
	layout := [][]Tile{}

	// Pick top_left corner such that it has non-open edge to east and south
	topLeft := tiles[identifyCornerIds(edgeMap)[0]]
	for len(edgeMap[topLeft.edges.east.id]) == 1 || len(edgeMap[topLeft.edges.south.id]) == 1 {
		topLeft = topLeft.getNextArrangement()
	}

	for row := 0; row < gridLength; row++ {
		layout = append(layout, []Tile{})
		if row == 0 {
			layout[row] = append(layout[row], topLeft)
		} else {
			// Do north match to layout[row-1][0].south
			northTile := layout[row-1][0]
			northEdgeID, northID := northTile.edges.south.id, northTile.id

			var currentID int
			for _, currentID = range edgeMap[northEdgeID] {
				if currentID != northID {
					break
				}
			}
			currentTile := tiles[currentID]
			for currentTile.edges.north.normal != northTile.edges.south.normal {
				currentTile = currentTile.getNextArrangement()
			}

			layout[row] = append(layout[row], currentTile)
		}
		for col := 1; col < gridLength; col++ {
			// Do west match to layout[row][col-1].east
			westTile := layout[row][col-1]
			westEdgeID, westID := westTile.edges.east.id, westTile.id

			var currentID int
			for _, currentID = range edgeMap[westEdgeID] {
				if currentID != westID {
					break
				}
			}
			currentTile := tiles[currentID]
			for currentTile.edges.west.normal != westTile.edges.east.normal {
				currentTile = currentTile.getNextArrangement()
			}

			layout[row] = append(layout[row], currentTile)
		}
	}
	return layout
}

func stitchImage(layout [][]Tile) Tile {
	image := []string{}
	for _, row := range layout {
		rowOffset := len(image)
		for i, tile := range row {
			for j, gridLine := range tile.getTrimmed() {
				if i == 0 {
					image = append(image, "")
				}
				image[rowOffset+j] += gridLine
			}
		}
	}
	return Tile{id: 0, flipped: false, grid: image, rotated: 0, edges: createEdges(image)}
}

func countPatterns(image Tile, pattern []string) int {
	maxFound := 0
	for i := 0; i < 8; i++ {
		patterns := 0
		image = image.getNextArrangement()
		imageGrid := image.grid
		for row := 0; row < len(imageGrid)-len(pattern); row++ {
		search:
			for col := 0; col < len(imageGrid[0])-len(pattern[0]); col++ {
				for y := 0; y < len(pattern); y++ {
					for x := 0; x < len(pattern[0]); x++ {
						if pattern[y][x] == '#' {
							if imageGrid[row+y][col+x] != '#' {
								continue search
							}
						}
					}
				}
				patterns++
			}
		}
		if patterns > maxFound {
			maxFound = patterns
		}
	}
	return maxFound
}

//Part1 - Solution to Part 1 of the puzzle
func Part1(input string) int {
	tiles := processInput(input)
	edgeMap := createEdgeMap(tiles)

	product := 1
	for _, id := range identifyCornerIds(edgeMap) {
		product *= id
	}
	return product
}

//Part2 - Solution to Part 2 of the puzzle
func Part2(input string) int {
	tiles := processInput(input)
	layout := calculateLayout(tiles)
	image := stitchImage(layout)

	seaMonster := "..................#.\n#....##....##....###\n.#..#..#..#..#..#..."
	pattern := strings.Split(seaMonster, "\n")
	patternCount := countPatterns(image, pattern)

	return image.countStrings("#") - patternCount*strings.Count(seaMonster, "#")
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
