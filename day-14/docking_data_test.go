package main

import (
	"fmt"
	"io/ioutil"
	"testing"
)

func TestPart1Example1(t *testing.T) {
	data := `
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0`[1:]
	expected := 165
	actual := Part1(data)
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

	expected := 18630548206046
	actual := Part1(data)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}

func TestPart2Example1(t *testing.T) {
	data := `
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1`[1:]
	expected := 208
	actual := Part2(data)
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

	expected := 4254673508445
	actual := Part2(data)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}
