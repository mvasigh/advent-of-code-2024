import re

def read_reports():
  reports = []
  with open("day_02/input.txt", "r") as file:
    for line in file:
      levels = [int(num_str) for num_str in re.findall(r"\d+", line.strip())]
      reports.append(levels)

  return reports

def is_safe(report):
  if not (report == sorted(report) or report == sorted(report, reverse=True)):
    return False
  
  for i in range(len(report)):
    if i == 0:
      continue
    diff = abs(report[i] - report[i - 1])

    if not (diff >= 1 and diff <= 3):
      return False

  return True

def part_1():
  reports = read_reports()
  safe_reports = 0

  for report in reports:
    if is_safe(report):
      safe_reports += 1

  return safe_reports

def part_2():
  reports = read_reports()
  safe_reports = 0

  for report in reports:
    if is_safe(report):
      safe_reports += 1
      continue

    for i in range(len(report)):
      report_cp = report.copy()
      report_cp.pop(i)

      if is_safe(report_cp):
        safe_reports += 1
        break
  
  return safe_reports

if __name__ == "__main__":
  print(f"Part 1: {part_1()}")
  print(f"Part 2: {part_2()}")