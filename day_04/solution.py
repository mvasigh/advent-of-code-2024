# values are (dr, dc) and using 0-based index
directions = {
  "n": (-1, 0),
  "ne": (-1, 1),
  "e": (0, 1),
  "se": (1, 1),
  "s": (1, 0),
  "sw": (1, -1),
  "w": (0, -1),
  "nw": (-1, -1)
}

def read_input():
  grid = []
  with open("day_04/input.txt", "r") as file:
    for line in file:
      grid.append(line.strip())

  return grid

def create_coords(grid):
  return set((r, c) for r in range(len(grid)) for c in range(len(grid[r])))

def get_letter(grid, coords):
  if coords[0] < 0 or coords[0] >= len(grid):
    return "."
  if coords[1] < 0 or coords[1] >= len(grid[0]):
    return "."
  
  return grid[coords[0]][coords[1]]

def add_elements(tuple_a, tuple_b):
  return tuple(a + b for a, b in zip(tuple_a, tuple_b))

def construct_word(grid, pt, diff, len):
  word = ""
  curr = pt

  for _ in range(len):
    word += get_letter(grid, curr)
    curr = add_elements(curr, diff)

  return word

def part_1():
  grid = read_input()
  coords = create_coords(grid)
  count = 0

  for pt in coords:
    for diff in directions.values():
      word = construct_word(grid, pt, diff, 4)
      if word == "XMAS":
        count += 1

  return count

def part_2():
  grid = read_input()
  coords = create_coords(grid)
  count = 0

  for pt in coords:
    nw_pt = add_elements(pt, directions["nw"])
    nw_word = construct_word(grid, nw_pt, directions["se"], 3)
    sw_pt = add_elements(pt, directions["sw"])
    sw_word = construct_word(grid, sw_pt, directions["ne"], 3)

    if (nw_word == "MAS" or nw_word == "SAM") and (sw_word == "MAS" or sw_word == "SAM"):
      count += 1

  return count

if __name__ == "__main__":
  print(f"Part 1: {part_1()}")
  print(f"Part 2: {part_2()}")