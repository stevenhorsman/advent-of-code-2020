package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

const input_file string = "./day-14/input.txt"

var (
	or_replacer  = strings.NewReplacer("X", "0")
	and_replacer = strings.NewReplacer("X", "1")
)

type updateMemory func(map[int]int, string, int, int)

func UpdateMemory1(mem map[int]int, mask string, address int, value int) {
	or_mask, _ := strconv.ParseInt(or_replacer.Replace(mask), 2, 0)
	value |= int(or_mask)
	and_mask, _ := strconv.ParseInt(and_replacer.Replace(mask), 2, 0)
	value &= int(and_mask)
	mem[address] = value
}

func DecoderChip(input string, updateFunc updateMemory) int {
	mem := make(map[int]int)
	curr_mask := ""
	// or_replacer := strings.NewReplacer("X", "0")
	// and_replacer := strings.NewReplacer("X", "1")
	for _, line := range strings.Split(strings.TrimSpace(input), "\n") {
		if strings.HasPrefix(line, "mask") {
			curr_mask = strings.Split(line, " = ")[1]
		} else {
			var address int
			var value int
			fmt.Sscanf(line, "mem[%d] = %d", &address, &value)
			updateFunc(mem, curr_mask, address, value)
			// or_mask, _ := strconv.ParseInt(or_replacer.Replace(curr_mask), 2, 0)
			// value |= int(or_mask)
			// and_mask, _ := strconv.ParseInt(and_replacer.Replace(curr_mask), 2, 0)
			// value &= int(and_mask)
			// mem[address] = value
		}
	}

	total := 0
	for _, v := range mem {
		total += v
	}
	return total
}

func Part1(input string) int {
	return DecoderChip(input, UpdateMemory1)
}

// Mostly copied from https://github.com/mxschmitt/golang-combinations/blob/master/combinations.go just adding empty set in
func PowerSet(set []int) [][]int {
	subsets := [][]int{[]int{}}
	length := uint(len(set))

	// Go through all possible combinations of objects from 1 to 2^length (all objects in subset)
	for subsetBits := 1; subsetBits < (1 << length); subsetBits++ {
		var subset []int

		for object := uint(0); object < length; object++ {
			// checks if object is contained in subset by checking if bit 'object' is set in subsetBits
			if (subsetBits>>object)&1 == 1 {
				subset = append(subset, set[object])
			}
		}
		// add subset to subsets
		subsets = append(subsets, subset)
	}
	return subsets
}

func UpdateMemory2(mem map[int]int, mask string, address int, value int) {
	floating_values := []int{}
	for i := 0; i < 36; i++ {
		bit := mask[35-i]
		address_bit := address & (1 << i)
		if bit == '1' && address_bit == 0 {
			address += (1 << i)
		} else if bit == 'X' {
			if (address_bit) != 0 {
				// Remove bit for wildcards
				address -= address_bit
			}
			floating_values = append(floating_values, 1<<i)
		}
	}

	for _, set := range PowerSet(floating_values) {
		sum := 0
		for _, v := range set {
			sum += v
		}
		mem[address+sum] = value
	}
}

func Part2(input string) int {
	return DecoderChip(input, UpdateMemory2)
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
