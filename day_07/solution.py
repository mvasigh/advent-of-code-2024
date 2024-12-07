def read_input():
  equations = []

  with open("day_07/input.txt", "r") as file:
    for line in file:
      total, parts = line.strip().split(": ")
      equations.append((int(total), [int(part) for part in parts.split(" ")]))

  return equations

add = lambda a, b: a + b
mul = lambda a, b: a * b
conc = lambda a, b: int(str(a) + str(b))

def is_possible(total, parts, ops):
  def evaluate(_current, _total, _parts):
    if _current == _total and not _parts:
      return True
    
    if _current > _total:
      return False
    
    if not _parts and _current < _total:
      return False

    return any(
      [evaluate(op(_current, _parts[0]), _total, _parts[1:]) for op in ops]
    )

  return evaluate(parts[0], total, parts[1:])
  
def part_1():
  equations = read_input()
  sum = 0

  for eq in equations:
    total, parts = eq
    if is_possible(total, parts, [add, mul]):
      sum += total
  
  return sum

def part_2():
  equations = read_input()
  sum = 0

  for eq in equations:
    total, parts = eq
    if is_possible(total, parts, [add, mul, conc]):
      sum += total
  
  return sum

if __name__ == "__main__":
  print(f"Part 1: {part_1()}")
  print(f"Part 2: {part_2()}")