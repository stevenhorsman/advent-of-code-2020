import itertools

input_file = 'day-09/input.txt'

def find_first_non_sum(numbers, window):
  for i in range(window, len(numbers)):
    window_combs = [combo for combo in itertools.combinations(numbers[i-window:i], 2) if sum(combo) == numbers[i]]
    if len(window_combs) == 0:
      return numbers[i]

def part1(input, window = 25):
  numbers = list(map(int, input.splitlines()))
  return find_first_non_sum(numbers, window)

def part2(input, window = 25):
  numbers = list(map(int, input.splitlines()))
  target = find_first_non_sum(numbers, window)

# Sliding window
  low = 0
  high = 1
  while high < len(numbers): 
    sum_size = sum(numbers[low:high+1])
    if sum_size == target:
      return min(numbers[low:high+1]) + max(numbers[low:high+1])
    elif sum_size < target:
      high += 1
    else:
      low += 1

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))