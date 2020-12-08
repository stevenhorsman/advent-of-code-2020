from collections import defaultdict

input_file = 'day-08/input.txt'

class Program:
  def __init__(self, lines):
    self.lines = lines
    self.pc = 0
    self.regs = defaultdict(int)
    self.executed = set()

  def run(self):
    while self.tick():
      pass
    return self.pc >= len(self.lines)

  def tick(self):
    if not (0 <= self.pc < len(self.lines)):
      return False

    # Stop allowing lines to run twice
    if self.pc in self.executed:
      return False
    else:
      self.executed.add(self.pc)

    instruction, parameter = self.lines[self.pc].split(' ', 1)
    parameter = int(parameter)

    if instruction == 'nop':
      pass
    elif instruction == 'acc':
      self.regs['acc'] += parameter
    elif instruction == 'jmp':
      self.pc += parameter
      return True # skip the pc += 1
    self.pc += 1
    return True

def part1(input):
  program = Program([line.split('#')[0] for line in input.splitlines()])
  program.run()
  return program.get('acc')

def part2(input):
  instructions = [line.split('#')[0] for line in input.splitlines()]

  instruction_change = {'jmp': 'nop', 'nop': 'jmp'}
  for i in range(len(instructions)):
    copy = instructions.copy()
    line_operation = copy[i].split(' ')[0]
    if line_operation in instruction_change:
      copy[i] = copy[i].replace(line_operation, instruction_change[line_operation])
    program = Program(copy)
    if program.run():
      return program.get('acc') 

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))

if __name__ == "__main__":
  with open(input_file) as f:
    data = f.read()
  print("Part 1: ", part1(data))
  print("Part 2: ", part2(data))