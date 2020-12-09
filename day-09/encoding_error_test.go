package main

import (
	"fmt"
	"io/ioutil"
	"testing"
)

func TestPart1Example1(t *testing.T) {
	data := `
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576`[1:]
	expected := 127
	actual := Part1(data, 5)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}

func TestPart1(t *testing.T) {
	b, err := ioutil.ReadFile("./input.txt")
	if err != nil {
		fmt.Print(err)
	}
	data := string(b)

	expected := 70639851
	actual := Part1(data, 25)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}

func TestPart2Example1(t *testing.T) {
	data := `
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576`[1:]
	expected := 62
	actual := Part2(data, 5)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}

func TestPart2(t *testing.T) {
	b, err := ioutil.ReadFile("./input.txt")
	if err != nil {
		fmt.Print(err)
	}
	data := string(b)

	expected := 8249240
	actual := Part2(data, 25)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}
