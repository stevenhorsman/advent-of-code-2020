package main

import (
	"fmt"
	"io/ioutil"
	"testing"
)

func TestPart1Example1(t *testing.T) {
	data := `
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc`[1:]
	expected := 2
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

	expected := 655
	actual := Part1(data)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}

func TestPart2Example1(t *testing.T) {
	data := `
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc`[1:]
	expected := 1
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

	expected := 673
	actual := Part2(data)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}
