package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

const input_file string = "./day-04/input.txt"

type passportData map[string]string

func CreatePassport(passport_string string) passportData {
	data := passportData{}
	// fmt.Printf("string: %s\n", passport_string)
	fields := strings.Fields(passport_string)
	// fmt.Printf("fields: %s\n", fields)
	for _, field := range fields {
		key_value := strings.Split(field, ":")
		data[key_value[0]] = key_value[1]
	}
	return data
}

func HasAllFields(passport_data passportData) bool {
	required := []string{"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
	for _, field := range required {
		if _, found := passport_data[field]; !found {
			return false
		}
	}
	return true
}

func Part1(input string) int {
	valid := 0
	passport_strings := strings.Split(strings.TrimSpace(input), "\n\n")
	for _, passport_string := range passport_strings {
		if HasAllFields(CreatePassport(passport_string)) {
			valid++
		}
	}

	return valid
}

func IsValid(passport_data passportData) bool {
	if !HasAllFields(passport_data) {
		return false
	}
	birth_year, err := strconv.Atoi(passport_data["byr"])
	if err != nil || !(birth_year >= 1920 && birth_year <= 2002) {
		return false
	}

	issue_year, err := strconv.Atoi(passport_data["iyr"])
	if err != nil || !(issue_year >= 2010 && issue_year <= 2020) {
		return false
	}

	expiration_year, err := strconv.Atoi(passport_data["eyr"])
	if err != nil || !(expiration_year >= 2020 && expiration_year <= 2030) {
		return false
	}

	var height int
	var units string
	fmt.Sscanf(passport_data["hgt"], "%d%s", &height, &units)
	if !((units == "cm" && (height >= 150 && height <= 193)) || (units == "in" && (height >= 59 && height <= 76))) {
		return false
	}

	match, _ := regexp.MatchString(`^#(?:[0-9a-fA-F]{1,2}){3}$`, passport_data["hcl"])
	if !match {
		return false
	}

	valid_eye_colours := []string{"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
	valid_eye_colour := false
	for _, v := range valid_eye_colours {
		if v == passport_data["ecl"] {
			valid_eye_colour = true
		}
	}
	if !valid_eye_colour {
		return valid_eye_colour
	}

	match, _ = regexp.MatchString(`^[0-9]{9}$`, passport_data["pid"])
	if !match {
		return false
	}

	return true
}

func Part2(input string) int {
	valid := 0
	passport_strings := strings.Split(strings.TrimSpace(input), "\n\n")
	for _, passport_string := range passport_strings {
		if IsValid(CreatePassport(passport_string)) {
			valid++
		}
	}
	return valid
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
