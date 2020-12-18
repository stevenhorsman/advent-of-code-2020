package main

import (
	"fmt"
	"io/ioutil"
	"testing"
)

func TestPart1Example1(t *testing.T) {
	data := "1 + 2 * 3 + 4 * 5 + 6"
	expected := 71
	actual := Part1(data)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}

func TestPart1Example2(t *testing.T) {
	data := "1 + (2 * 3) + (4 * (5 + 6))"
	expected := 51
	actual := Part1(data)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}

func TestPart1Example3(t *testing.T) {
	data := `
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2`[1:]
	expected := 26 + 437 + 12240 + 13632
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

	expected := 14006719520523
	actual := Part1(data)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}

func TestPart2Example1(t *testing.T) {
	data := "1 + 2 * 3 + 4 * 5 + 6"
	expected := 231
	actual := Part2(data)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}

func TestPart2Example2(t *testing.T) {
	data := "1 + (2 * 3) + (4 * (5 + 6))"
	expected := 51
	actual := Part2(data)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}

func TestPart2Example3(t *testing.T) {
	data := `
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2`[1:]
	expected := 46 + 1445 + 669060 + 23340
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

	expected := 545115449981968
	actual := Part2(data)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}
