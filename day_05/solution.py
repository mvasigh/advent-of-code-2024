import math

def read_input():
  rules = []
  updates = []

  with open("day_05/input.txt", "r") as file:
    raw_rules, raw_updates = file.read().split("\n\n")

    for raw_rule in raw_rules.split("\n"):
      a, b = raw_rule.split("|")
      rules.append((int(a), int(b)))

    for raw_update in raw_updates.split("\n"):
      updates.append([int(pg) for pg in raw_update.split(",")])

  return rules, updates

def create_rule_map(rules):
  rule_map = {}

  for before, after in rules:
    pg_set = rule_map.get(before, set())
    pg_set.add(after)
    rule_map[before] = pg_set

  return rule_map

def is_update_valid(rule_map, update):
  seen = set()

  for pg in update:
    for pg_rule in rule_map.get(pg, set()):
      if pg_rule in seen:
        return False

    seen.add(pg)
  
  return True

def get_rule_hits(rule_map, pg, other_pgs):
  rules = rule_map.get(pg)
  counts = 0

  for other_pg in other_pgs:
    if other_pg == pg:
      continue

    if other_pg in rules:
      counts += 1

  return counts

def fix_update(rule_map, update):
  fixed_update = []

  while len(fixed_update) < len(update):
    remaining = set([pg for pg in update if pg not in fixed_update])

    for pg in remaining:
      count = get_rule_hits(rule_map, pg, remaining)
      if count == (len(update) - len(fixed_update) - 1):
        fixed_update.append(pg)
        break

  return fixed_update

def get_middle_page(update):
  return update[math.floor(len(update) / 2)]

def part_1():
  rules, updates = read_input()
  rule_map = create_rule_map(rules)
  middle_sum = 0

  for update in updates:
    if is_update_valid(rule_map, update):
      middle_sum += get_middle_page(update)

  return middle_sum

def part_2():
  rules, updates = read_input()
  rule_map = create_rule_map(rules)
  invalid_updates = [update for update in updates if not is_update_valid(rule_map, update)]
  fixed_updates = [fix_update(rule_map, update) for update in invalid_updates]
  middle_sum = 0

  for update in fixed_updates:
    middle_sum += get_middle_page(update)

  return middle_sum

if __name__ == "__main__":
  print(f"Part 1: {part_1()}")
  print(f"Part 2: {part_2()}")