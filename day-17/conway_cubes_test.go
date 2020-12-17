package main

import (
	"fmt"
	"io/ioutil"
	"reflect"
	"testing"
)

var example_data string = `
.#.
..#
###`[1:]

func TestGetDeltas1(t *testing.T) {
	expected := [][]int{{-1}, {1}}
	actual := GetDeltas(1)
	if !reflect.DeepEqual(expected, actual) {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}

func TestGetDeltas2(t *testing.T) {
	expected := [][]int{
		{-1, 0},
		{1, 0},
		{0, -1},
		{-1, -1},
		{1, -1},
		{0, 1},
		{-1, 1},
		{1, 1}}
	actual := GetDeltas(2)
	if !reflect.DeepEqual(expected, actual) {
		t.Errorf("Expected %v but was %v\n", expected, actual)
	}
}

func TestGetDeltas3(t *testing.T) {
	expected := 26
	actual := len(GetDeltas(3))
	if !reflect.DeepEqual(26, actual) {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}

func TestPart1Example0(t *testing.T) {
	expected := 5
	actual := Part1(example_data, 0)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}

func TestPart1Example1(t *testing.T) {
	expected := 11
	actual := Part1(example_data, 1)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}

func TestPart1Example2(t *testing.T) {
	expected := 112
	actual := Part1(example_data, 6)
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

	expected := 242
	actual := Part1(data, 6)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}

func TestPart2Example1(t *testing.T) {
	expected := 848
	actual := Part2(example_data)
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

	expected := 2292
	actual := Part2(data)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}
