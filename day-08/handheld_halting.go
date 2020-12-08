package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

const input_file string = "./day-08/input.txt"

type Instruction struct {
	opCode   string
	argument int
}

type Computer struct {
	program []Instruction
	ip      int
	acc     int
}

func (c *Computer) run() bool {
	executed := make(map[int]bool)
	for {
		if c.ip >= len(c.program) {
			return true // finished execution
		}

		if _, found := executed[c.ip]; found {
			return false // In infinite loop
		} else {
			executed[c.ip] = true
		}
		c.tick()
	}
}

func (c *Computer) tick() {
	instruction := c.program[c.ip]
	switch instruction.opCode {
	case "acc":
		c.acc += instruction.argument
	case "jmp":
		c.ip += instruction.argument
		return //skip ip increment
	}
	c.ip++
}

func ReadProgram(input string) []Instruction {
	instructions := []Instruction{}
	lines := strings.Split(strings.TrimSpace(input), "\n")
	for _, line := range lines {
		instruction_parts := strings.Split(line, " ")
		arg, err := strconv.Atoi(instruction_parts[1])
		if err != nil {
			panic(err)
		}
		instruction := Instruction{
			opCode:   instruction_parts[0],
			argument: arg,
		}
		instructions = append(instructions, instruction)
	}
	return instructions
}

func Part1(input string) int {
	instructions := ReadProgram(input)
	computer := Computer{
		program: instructions,
		ip:      0,
		acc:     0,
	}
	computer.run()
	return computer.acc
}

func Part2(input string) int {
	instructions := ReadProgram(input)
	replacer := strings.NewReplacer("jmp", "nop", "nop", "jmp")
	for i := 0; i < len(instructions); i++ {
		lineCopy := make([]Instruction, len(instructions))
		copy(lineCopy, instructions)
		lineCopy[i].opCode = replacer.Replace(lineCopy[i].opCode)
		computer := Computer{
			program: lineCopy,
			ip:      0,
			acc:     0,
		}
		if computer.run() {
			return computer.acc
		}
	}
	return -1
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
