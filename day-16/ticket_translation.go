package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

const input_file string = "./day-16/input.txt"

type Rule struct {
	name   string
	start1 int
	stop1  int
	start2 int
	stop2  int
}

func (r Rule) IsValid(value int) bool {
	return (r.start1 <= value && value <= r.stop1) || (r.start2 <= value && value <= r.stop2)
}

func ParseRules(rulesSection string) []Rule {
	rules := []Rule{}
	for _, line := range strings.Split(strings.TrimSpace(rulesSection), "\n") {
		rule := Rule{}
		split := strings.Split(line, ": ")
		rule.name = split[0]
		fmt.Sscanf(split[1], "%d-%d or %d-%d", &rule.start1, &rule.stop1, &rule.start2, &rule.stop2)
		rules = append(rules, rule)
	}
	return rules
}

func ParseTickets(ticketsSection string) [][]int {
	tickets := [][]int{}
	// First line of section is descriptor string
	for _, line := range strings.Split(strings.TrimSpace(ticketsSection), "\n")[1:] {
		ticket := []int{}
		for _, s := range strings.Split(line, ",") {
			n, _ := strconv.Atoi(s)
			ticket = append(ticket, n)
		}
		tickets = append(tickets, ticket)
	}
	return tickets
}

func SumInvalidValues(rules []Rule, tickets [][]int) int {
	total := 0
	for _, ticket := range tickets {
		for _, value := range ticket {
			valid := false
			for _, rule := range rules {
				valid = valid || rule.IsValid(value)
			}
			if valid == false {
				total += value
			}
		}
	}
	return total
}

func FilterValidTickets(rules []Rule, tickets [][]int) [][]int {
	valid_tickets := [][]int{}
	for _, ticket := range tickets {
		ticket_valid := true
		for _, value := range ticket {
			any_rule_valid := false
			for _, rule := range rules {
				any_rule_valid = any_rule_valid || rule.IsValid(value)
			}
			ticket_valid = ticket_valid && any_rule_valid
		}
		if ticket_valid {
			valid_tickets = append(valid_tickets, ticket)
		}
	}
	return valid_tickets
}

func CalculateRuleOrder(rules []Rule, tickets [][]int) map[string]int {
	rule_order := make(map[string]int)
	for len(rule_order) < len(rules) {
		for i := 0; i < len(tickets[0]); i++ {
			i_values := []int{}
			for _, ticket := range tickets {
				i_values = append(i_values, ticket[i])
			}
			matching_rules := []string{}
			for _, rule := range rules {
				if _, found := rule_order[rule.name]; !found {
					rule_valid := true
					for _, value := range i_values {
						rule_valid = rule_valid && rule.IsValid(value)
					}
					if rule_valid {
						matching_rules = append(matching_rules, rule.name)
					}
				}
			}
			if len(matching_rules) == 1 {
				rule_order[matching_rules[0]] = i
			}
		}
	}
	return rule_order
}

func Part1(input string) int {
	sections := strings.Split(input, "\n\n")
	rules := ParseRules(sections[0])
	tickets := ParseTickets(sections[2])
	return SumInvalidValues(rules, tickets)
}

func Part2(input string) int {
	sections := strings.Split(input, "\n\n")
	rules := ParseRules(sections[0])
	my_ticket := ParseTickets(sections[1])[0]
	tickets := ParseTickets(sections[2])
	tickets = FilterValidTickets(rules, tickets)

	rule_order := CalculateRuleOrder(rules, tickets)

	product := 1
	for k, v := range rule_order {
		if strings.HasPrefix(k, "departure") {
			product *= my_ticket[v]
		}
	}
	return product
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
