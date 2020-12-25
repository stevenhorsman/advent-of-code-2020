input_file = 'day-25/input.txt'

def get_secret(public_key):
  secret, calc = 0,1
  while public_key != calc:
    secret += 1
    calc *= 7
    calc %= 20201227
    # calc = pow(7, secret, 20201227) # Doing the above is much faster than pow
  return secret

def part1(input):
  public_keys = [int(line) for line in input.splitlines()]
  secret_keys = [get_secret(key) for key in public_keys]
  encryption_keys = [pow(public_keys[1], secret_keys[0], 20201227), pow(public_keys[0], secret_keys[1], 20201227)]
  # print(public_keys, secret_keys, encryption_keys)
  assert encryption_keys[0] == encryption_keys[1]
  return encryption_keys[0]

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))