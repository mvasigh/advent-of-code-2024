from itertools import combinations

def read_input():
  grid = []
  freq_map = {}

  with open("day_08/input.txt", "r") as file:
    raw_txt = file.read()
    lines = raw_txt.strip().split('\n')
    
    for r in range(len(lines)):
      line = lines[r]
      chars = list(line.strip())
      grid.append(chars)

      for c in range(len(chars)):
        char = chars[c]

        if char != ".":
          coord_set = freq_map.get(char, set())
          coord_set.add((r, c))
          freq_map[char] = coord_set          

  return grid, freq_map

def diff_pts(a, b):
  return (b[0] - a[0], b[1] - a[1])

def add_pts(a, b):
  return (a[0] + b[0], a[1] + b[1])

def is_inbounds(pt, max_r, max_c):
    return pt[0] >= 0 and pt[0] < max_r and pt[1] >= 0 and pt[1] < max_c

def get_line_pts(start, increment, max_r, max_c, max_len):
  pts = []
  curr = add_pts(start, increment)

  while is_inbounds(curr, max_r, max_c) and len(pts) < max_len:
    pts.append(curr)
    curr = add_pts(curr, increment)

  return pts

def get_antinodes(grid, freq_map, max_len = 1):
  antinodes = set()
  rows = len(grid)
  cols = len(grid[0])

  for nodes in freq_map.values():
    for node_a, node_b in combinations(nodes, 2):
      pts = (
        get_line_pts(node_b, diff_pts(node_a, node_b), rows, cols, max_len) 
        + get_line_pts(node_a, diff_pts(node_b, node_a), rows, cols, max_len)
      )
      for pt in pts:
        antinodes.add(pt)

  return antinodes


def part_1():
  grid, freq_map = read_input()
  antinodes = get_antinodes(grid, freq_map)

  return len(antinodes)

def part_2():
  grid, freq_map = read_input()
  antinodes = list(get_antinodes(grid, freq_map, float("inf")))
  antennae = [pt for hits in freq_map.values() for pt in hits]

  return len(set(antinodes + antennae))

if __name__ == "__main__":
  print(f"Part 1: {part_1()}")
  print(f"Part 2: {part_2()}")