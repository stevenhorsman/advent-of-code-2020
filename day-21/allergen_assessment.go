package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strings"
)

const inputFile string = "./day-21/input.txt"

func ParseInput(input string) (map[string]map[string]bool, map[string]int) {
	allergenMatches := make(map[string]map[string]bool)
	ingredientCounts := make(map[string]int)

	for _, line := range strings.Split(strings.TrimSpace(input), "\n") {
		splits := strings.SplitN(line, " (contains ", 2)
		ingredients := strings.Split(splits[0], " ")
		allergensString := splits[1][:len(splits[1])-1]
		allergens := strings.Split(allergensString, ", ")

		for _, allergen := range allergens {
			if _, found := allergenMatches[allergen]; !found {
				allergenMatches[allergen] = make(map[string]bool)
				for _, ingredient := range ingredients {
					allergenMatches[allergen][ingredient] = true
				}
			} else {
				// set intersection
				for i := range allergenMatches[allergen] {
					contains := false
					for _, ingredient := range ingredients {
						if i == ingredient {
							contains = true
						}
					}
					if contains == false {
						delete(allergenMatches[allergen], i)
					}
				}
			}
		}
		for _, ingredient := range ingredients {
			if _, found := ingredientCounts[ingredient]; !found {
				ingredientCounts[ingredient] = 0
			}
			ingredientCounts[ingredient]++
		}
	}
	return allergenMatches, ingredientCounts
}

func Part1(input string) int {
	allergenMatches, ingredientCounts := ParseInput(input)

	count := 0
	for i, c := range ingredientCounts {
		candidateAllergen := false
		for _, is := range allergenMatches {
			if _, found := is[i]; found {
				candidateAllergen = true
			}
		}
		if !candidateAllergen {
			count += c
		}
	}
	return count
}

func Part2(input string) string {
	allergenMatches, _ := ParseInput(input)

	matchedAllergens := make(map[string]string)
	for len(allergenMatches) > 0 {
		for a, is := range allergenMatches {
			if len(is) == 1 {
				var ingredient string
				for i := range is {
					ingredient = i
				}
				matchedAllergens[a] = ingredient
				delete(allergenMatches, a)
				//Remove ingredient from other allergen sets
				for otherAl, _ := range allergenMatches {
					delete(allergenMatches[otherAl], ingredient)
				}
			}
		}
	}

	//Get list of ingredients, sorted by allergen
	allergens := make([]string, 0, len(matchedAllergens))
	for a := range matchedAllergens {
		allergens = append(allergens, a)
	}
	sort.Strings(allergens)

	ingredients := make([]string, 0, len(allergens))
	for _, a := range allergens {
		ingredients = append(ingredients, matchedAllergens[a])
	}

	return strings.Join(ingredients, ",")
}

func main() {
	b, err := ioutil.ReadFile(inputFile)
	if err != nil {
		fmt.Print(err)
	}
	data := string(b)

	fmt.Printf("Part 1: %d\n", Part1(data))
	fmt.Printf("Part 2: %s\n", Part2(data))
}
