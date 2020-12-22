package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

const inputFile string = "./day-22/input.txt"

type deck []int

func (d deck) getScore() int {
	score := 0
	length := len(d)
	for i, v := range d {
		score += v * (length - i)
	}
	return score
}

func (d deck) copy(start int, end int) deck {
	return append(deck(nil), d[start:end]...)
}

func processDeck(input string) deck {
	var numbers deck
	for _, num := range strings.Split(strings.TrimSpace(input), "\n")[1:] {
		n, _ := strconv.Atoi(num)
		numbers = append(numbers, n)
	}
	return numbers
}

func processInput(input string) (deck, deck) {
	players := strings.Split(strings.TrimSpace(input), "\n\n")
	return processDeck(players[0]), processDeck(players[1])
}

type hash struct {
	hash1, hash2 int
}

func playRound(player1 deck, player2 deck, part2 bool) ([]int, []int) {
	previousRounds := make(map[hash]bool)

	for len(player1) > 0 && len(player2) > 0 {

		if part2 {
			roundHash := hash{player1.getScore(), player2.getScore()}
			if _, found := previousRounds[roundHash]; found {
				return player1, deck{}
			}
			previousRounds[roundHash] = true
		}

		var p1, p2 int
		p1, player1 = player1[0], player1[1:]
		p2, player2 = player2[0], player2[1:]

		var p1Win bool
		if part2 && len(player1) >= p1 && len(player2) >= p2 {
			copy1, copy2 := player1.copy(0, p1), player2.copy(0, p2)
			_, rec2 := playRound(copy1, copy2, true)
			p1Win = len(rec2) == 0
		} else {
			p1Win = p1 > p2
		}

		if p1Win {
			player1 = append(player1, p1, p2)
		} else {
			player2 = append(player2, p2, p1)
		}
	}
	return player1, player2
}

func playGame(input string, part2 bool) int {
	player1, player2 := processInput(input)

	player1, player2 = playRound(player1, player2, part2)

	if len(player1) > 0 {
		return player1.getScore()
	}
	return player2.getScore()
}

//Part1 - Solution to Part 1 of the puzzle
func Part1(input string) int {
	return playGame(input, false)
}

//Part2 - Solution to Part 2 of the puzzle
func Part2(input string) int {
	return playGame(input, true)
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
