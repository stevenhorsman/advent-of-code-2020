package main

import (
	"fmt"
	"io/ioutil"
	"testing"
)

func TestPart1Example1(t *testing.T) {
	data := `
5764801
17807724`[1:]
	expected := 14897079
	actual := Part1(data)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}

func TestPart1(t *testing.T) {
	bytes, err := ioutil.ReadFile("./input.txt")
	if err != nil {
		fmt.Print(err)
	}
	data := string(bytes)

	expected := 1478097
	actual := Part1(data)
	if actual != expected {
		t.Errorf("Expected %d but was %d\n", expected, actual)
	}
}

func BenchmarkPart1(b *testing.B) {
	bytes, err := ioutil.ReadFile("./input.txt")
	if err != nil {
		fmt.Print(err)
	}
	data := string(bytes)
	b.ResetTimer()
	for n := 0; n < b.N; n++ {
		Part1(data)
	}
}
