import re

def read_input():
  with open("day_03/input.txt", "r") as file:
    return re.sub("\n", "", file.read())
  
def add_all_muls(input):
  mul_re = r"mul\((?P<arg_a>\d+),(?P<arg_b>\d+)\)"

  total = 0
  for match in re.finditer(mul_re, input):
    total += int(match.group("arg_a")) * int(match.group("arg_b"))
  
  return total

def part_1():
  input = read_input()

  return add_all_muls(input)

def part_2():
  input = re.sub(r"don't\(\).*?(do\(\)|$)", "", read_input())

  return add_all_muls(input)

if __name__ == "__main__":
  print(f"Part 1: {part_1()}")
  print(f"Part 2: {part_2()}")