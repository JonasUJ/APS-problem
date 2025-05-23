from sys import stdin
from collections import defaultdict

n = int(input())

lines = [line.split() for line in stdin]
problems = defaultdict(list)
for k, m, p, t in lines:
    problems[k].append((m, int(p), int(t)))
problems = list(problems.values())

# Sort asc by most points then by least time
problems = list(map(lambda ms: max(ms, key=lambda m: (m[1], -m[2])), problems))
problems.sort()

points = 0
time = 0
for m, p, t in problems:
    if time + t > 100:
        break
    points += p

print(points)
