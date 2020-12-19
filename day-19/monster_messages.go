package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

const inputFile string = "./day-19/input.txt"

type Rule struct {
	processed string
	subRules  [][]int
}

func ParseRules(rulesSection string) map[int]Rule {
	rules := make(map[int]Rule)
	for _, rule := range strings.Split(strings.TrimSpace(rulesSection), "\n") {
		split := strings.SplitN(rule, ": ", 2)
		ruleContents := split[1]
		rule := Rule{}
		if strings.Contains(ruleContents, "\"") {
			rule.processed = strings.Trim(strings.TrimSpace(ruleContents), "\"")
		} else {
			orMatchers := [][]int{}
			for _, ruleSplit := range strings.Split(ruleContents, "|") {
				splitMatcher := []int{}
				for _, numString := range strings.Split(strings.TrimSpace(ruleSplit), " ") {
					num, _ := strconv.Atoi(numString)
					splitMatcher = append(splitMatcher, num)
				}
				orMatchers = append(orMatchers, splitMatcher)
			}
			rule.subRules = orMatchers
		}

		ruleNum, _ := strconv.Atoi(split[0])
		rules[ruleNum] = rule
	}
	return rules
}

//TODO - put function on rule?
func ResolveRule(rules map[int]Rule, ruleNum int, part2 bool) string {
	rule := rules[ruleNum]
	if rule.processed != "" {
		return rule.processed
	}
	if part2 {
		if ruleNum == 8 {
			return ResolveRule(rules, 42, part2) + "+"
		} else if ruleNum == 11 {
			rule42 := ResolveRule(rules, 42, part2)
			rule31 := ResolveRule(rules, 31, part2)
			repeatMatches := []string{}
			for i := 1; i <= 5; i++ {
				repeatMatches = append(repeatMatches, fmt.Sprintf("%s{%d}%s{%d}", rule42, i, rule31, i))
			}
			rule.processed = "(?:" + strings.Join(repeatMatches, "|") + ")"
			return rule.processed
		}
	}
	resolvedParts := []string{}
	for _, orRules := range rule.subRules {
		resolved := []string{}
		for _, linkedRule := range orRules {
			resolved = append(resolved, ResolveRule(rules, linkedRule, part2))
		}
		resolvedParts = append(resolvedParts, strings.Join(resolved, ""))
	}
	rule.processed = "(?:" + strings.Join(resolvedParts, "|") + ")"
	return rule.processed
}

func CountMatches(input string, part2 bool) int {
	sections := strings.Split(input, "\n\n")
	rules := ParseRules(sections[0])
	ruleZero := regexp.MustCompile("^" + ResolveRule(rules, 0, part2) + "$")

	matches := 0
	for _, message := range strings.Split(sections[1], "\n") {
		if ruleZero.MatchString(message) {
			matches++
		}
	}
	return matches
}

func Part1(input string) int {
	return CountMatches(input, false)
}

func Part2(input string) int {
	return CountMatches(input, true)
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
