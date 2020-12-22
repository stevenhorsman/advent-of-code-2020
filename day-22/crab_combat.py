import itertools
from collections import deque

input_file = 'day-22/input.txt'

def process_input(input):
  split = input.split('\n\n')
  player1 = deque([int(x) for x in split[0].splitlines()[1:]])
  player2 = deque([int(x) for x in split[1].splitlines()[1:]])
  return player1, player2

def play_round(player1, player2, part2 = False):
  previous_rounds = set() #TODO - tidy up cache
  p1_cache, p2_cache = set(), set()

  while player1 and player2:

    if part2:
      hash = (tuple(player1), tuple(player2))
      if hash in previous_rounds:
        return player1, []
      else:
        previous_rounds.add(hash)
  
    p1, p2 = player1.popleft(), player2.popleft()

    if part2 and (len(player1) >= p1 and len(player2) >= p2):
      player1_copy = list(itertools.islice(player1, 0, p1))
      player2_copy = list(itertools.islice(player2, 0, p2))

      rec1, rec2 = play_round(deque(player1_copy), deque(player2_copy), True)
      p1_win = len(rec2) == 0
    else:
      p1_win = p1 > p2

    if p1_win:
      player1 += [p1, p2]
    else:
      player2 += [p2, p1]

  return player1, player2

def get_score(queue):
  score = 0
  length = len(queue)
  for i, v in enumerate(queue):
    score += v * (length-i)
  return score

def play_game(input, part2 = False):
  player1, player2 = play_round(*process_input(input), part2)

  if len(player1) > 0:
    return get_score(player1)
  return get_score(player2)

def part1(input):
  return play_game(input)

def part2(input):
  return play_game(input, True)

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))