import math

input_file = 'day-13/input.txt'

def part1(input):
  timestamp, bus_ids = int(input.split('\n')[0]), input.split('\n')[1]
  bus_ids = [int(id) for id in bus_ids.split(',') if id != 'x']
  print(timestamp, bus_ids)
  best_next_bus = timestamp # replace with big int
  bus_id = -1
  for id in bus_ids:
    next_bus = id - (timestamp % id)
    print(id, next_bus)
    if next_bus < best_next_bus:
      best_next_bus = next_bus
      bus_id = id

  return bus_id * best_next_bus

# Based on https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
def chinese_remainder(n, a):
    N = math.prod(n)
    sum = 0
    for n_i, a_i in zip(n, a):
        p = N // n_i
        sum += a_i * inverse_mod(p, n_i) * p
    return sum % N

def inverse_mod(product, n):
  return pow(product, -1, n)

def part2(input):
  bus_ids = input.split('\n')[1].split(',')
  n = []
  a = []

  for index, id in enumerate(bus_ids):
    if id != 'x':
      id = int(id)
      n.append(id)
      a.append(-index % id)
      # schedule[index] = id
  # print(schedule)

  return chinese_remainder(n, a)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))