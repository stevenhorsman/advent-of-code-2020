package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

const inputFile string = "./day-25/input.txt"

func getInts(input string) []int {
	var numbers []int
	split := strings.Split(strings.TrimSpace(input), "\n")
	for _, num := range split {
		float, _ := strconv.Atoi(num)
		numbers = append(numbers, float)
	}
	return numbers
}

func getSecret(publicKey int) int {
	secret, calc := 0, 1
	for calc != publicKey {
		secret++
		calc *= 7
		calc %= 20201227
	}
	return secret
}

func transformKey(public, private int) int {
	key := 1
	for i := 0; i < private; i++ {
		key *= public
		key %= 20201227
	}
	return key
}

//Part1 - Solution to Part 1 of the puzzle
func Part1(input string) int {
	publicKeys := getInts(input)
	secretKeys := []int{}
	for _, public := range publicKeys {
		secretKeys = append(secretKeys, getSecret(public))
	}

	encryptionKeys := []int{}
	encryptionKeys = append(encryptionKeys, transformKey(publicKeys[1], secretKeys[0]))
	// encryptionKeys = append(encryptionKeys, transformKey(publicKeys[0], secretKeys[1]))

	return encryptionKeys[0]
}

func main() {
	b, err := ioutil.ReadFile(inputFile)
	if err != nil {
		fmt.Print(err)
	}
	data := string(b)

	fmt.Printf("Part 1: %d\n", Part1(data))
}
