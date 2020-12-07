package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

const input_file string = "./day-06/input.txt"

func ParseGroups(input string) [][]string {
	groups := [][]string{}
	groups_string := strings.Split(strings.TrimSpace(input), "\n\n")
	for _, group_string := range groups_string {
		group := strings.Split(group_string, "\n")
		groups = append(groups, group)
	}
	return groups
}

func Part1(input string) int {
	union_count := 0
	groups := ParseGroups(input)
	for _, group := range groups {
		character_count := make(map[rune]int)
		for _, person := range group {
			for _, char := range person {
				character_count[char]++
			}
		}
		union_count += len(character_count)
	}
	return union_count
}

func Part2(input string) int {
	intersection_count := 0
	groups := ParseGroups(input)
	for _, group := range groups {
		character_count := make(map[rune]int)
		for _, person := range group {
			for _, char := range person {
				character_count[char]++
			}
		}
		for _, count := range character_count {
			if count == len(group) {
				intersection_count++
			}
		}
	}
	return intersection_count
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
