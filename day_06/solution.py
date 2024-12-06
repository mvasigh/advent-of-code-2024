import re

directions = {
  "^": (-1, 0),
  "v": (1, 0),
  ">": (0, 1),
  "<": (0, -1),
}

def read_input():
  guard = None
  heading = None
  grid = []

  with open("day_06/input.txt", "r") as file:
    for l in file:
      line = l.strip()
      r = len(grid)
      match = re.search(r"[\^v<>]", line)

      if match:
        heading = match.group()
        c = match.start()
        guard = (r, c)

      grid.append(line)


  return grid, guard, heading

def turn_right(heading):
  if heading == "^":
    return ">"
  elif heading == ">":
    return "v"
  elif heading == "v":
    return "<"
  elif heading == "<":
    return "^"
  else:
    raise ValueError("Invalid heading")
  
def get_coords(grid, coords):
  if coords[0] < 0 or coords[0] >= len(grid):
    return None
  if coords[1] < 0 or coords[1] >= len(grid[0]):
    return None
  return grid[coords[0]][coords[1]]

def replace_coords(grid, coords, new_ch):
  new_grid = grid.copy()
  row = new_grid[coords[0]]
  new_grid[coords[0]] = row[:coords[1]] + new_ch + row[coords[1] + 1:]

  return new_grid

def add_elements(tuple_a, tuple_b):
  return tuple(a + b for a, b in zip(tuple_a, tuple_b))

def map_route(grid, init_guard, init_heading):
  seen = set()
  guard = init_guard
  heading = init_heading
  loop = False

  while True:
    if (guard, heading) in seen:
      loop = True
      break

    seen.add((guard, heading))
    next_tile = get_coords(grid, add_elements(guard, directions[heading]))

    if next_tile == "#":
      heading = turn_right(heading)
    elif next_tile:
      guard = add_elements(guard, directions[heading])
    else:
      break

  return seen, loop

def part_1():
  grid, guard, heading = read_input()
  route = set([seen[0] for seen in map_route(grid, guard, heading)[0]])
  

  return len(route)

def part_2():
  grid, guard, heading = read_input()
  init_route = set([seen[0] for seen in map_route(grid, guard, heading)[0]])
  loop_ct = 0

  for pt in init_route:
    if pt == guard:
      continue
    new_grid = replace_coords(grid, pt, "#")
    route, loop = map_route(new_grid, guard, heading)

    if loop:
      loop_ct += 1

  return loop_ct

if __name__ == "__main__":
  print(f"Part 1: {part_1()}")
  print(f"Part 2: {part_2()}")