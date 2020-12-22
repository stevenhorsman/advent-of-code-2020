package main

import (
	"fmt"
	"io/ioutil"
	"testing"
)

func TestPart1Example1(t *testing.T) {
	data := `
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10`[1:]
	expected := 306
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

	expected := 32401
	actual := Part1(data)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}

func TestPart2Example1(t *testing.T) {
	data := `
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10`[1:]
	expected := 291
	actual := Part2(data)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}

func TestPart2ExampleInfinite(t *testing.T) {
	data := `
Player 1:
43
19

Player 2:
2
29
14`[1:]
	expected := 105
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

	expected := 31436
	actual := Part2(data)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}
