from sys import stdin
from collections import defaultdict

n = int(input())

lines = [line.split() for line in stdin]
problems = defaultdict(list)
for k, m, p, t in lines:
    problems[k].append((m, int(p), int(t)))
problems = list(problems.values())

# Sort asc by least time then by most points
problems = list(map(lambda ms: max(ms, key=lambda m: (-m[2], m[1])), problems))
problems.sort()

points = 0
time = 0
for m, p, t in problems:
    if time + t > 100:
        break
    points += p

print(points)

