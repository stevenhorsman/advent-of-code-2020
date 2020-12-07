package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

const input_file string = "./day-07/input.txt"

type Bag struct {
	name     string
	contents map[*Bag]int
}

func (b Bag) Find(target string) bool {
	for c := range b.contents {
		if c.name == target || c.Find(target) {
			return true
		}
	}
	return false
}

func (b Bag) Count() int {
	count := 0
	for c, quantity := range b.contents {
		count += quantity + (quantity * c.Count())
	}
	return count
}

func ParseInput(input string) map[string]*Bag {
	bags := make(map[string]*Bag)

	parentMatcher := regexp.MustCompile(`^(\w+ \w+) bags contain (.*)$`)
	childMatcher := regexp.MustCompile(`^(\d+) (\w+ \w+) bag[s]?[.]?$`)

	lines := strings.Split(strings.TrimSpace(input), "\n")
	for _, line := range lines {
		matches := parentMatcher.FindStringSubmatch(line)
		bagName := matches[1]
		bag, ok := bags[bagName]
		if !ok {
			bag = &Bag{name: bagName, contents: make(map[*Bag]int)}
			bags[bagName] = bag
		}

		for _, contents_string := range strings.Split(strings.TrimRight(matches[2], "."), ", ") {
			// fmt.Printf("Contents %s\n", contents_string)
			if contents_string == "no other bags" {
				continue
			}
			contents := childMatcher.FindStringSubmatch(contents_string)
			quantity, err := strconv.Atoi(contents[1])
			if err != nil {
				panic(err)
			}
			childBagName := contents[2]
			childBag, ok := bags[childBagName]
			if !ok {
				childBag = &Bag{name: childBagName, contents: make(map[*Bag]int)}
				bags[childBagName] = childBag
			}
			bag.contents[childBag] = quantity
		}
	}

	return bags
}

func Part1(input string) int {
	count := 0
	bags := ParseInput(input)
	for _, b := range bags {
		if b.Find("shiny gold") {
			count++
		}
	}
	return count
}

func Part2(input string) int {
	bags := ParseInput(input)
	return bags["shiny gold"].Count()
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
