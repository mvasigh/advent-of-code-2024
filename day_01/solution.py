import re

def read_lists():
  list_a = []
  list_b = []

  with open("day_01/input.txt", "r") as file:
    for line in file:
      num_a, num_b = [int(num_str) for num_str in re.findall(r"\d+", line.strip())]
      list_a.append(num_a)
      list_b.append(num_b)

  list_a.sort()
  list_b.sort()

  return list_a, list_b

def part_1():
  list_a, list_b = read_lists()
  diff = 0
  
  for i in range(len(list_a)):
    diff += abs(list_a[i] - list_b[i])

  return diff

def part_2():
  list_a, list_b = read_lists()
  
  b_counts = {num: 0 for num in (list_a + list_b)}
  for num in list_b:
    b_counts[num] += 1

  sim_score = 0
  for num in list_a:
    sim_score += num * b_counts[num]

  return sim_score

if __name__ == "__main__":
  print(f"Part 1: {part_1()}")
  print(f"Part 2: {part_2()}")