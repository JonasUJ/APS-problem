from collections import defaultdict

n = int(input())
problems = defaultdict(list)

for _ in range(n):
    k, m, p, t = input().split()
    problems[k].append((int(p), int(t)))

problem_options = list(problems.values())
combinations = [(0, 0)]

for options in problem_options:
    new_combinations = []
    for current_points, current_time in combinations:
        for p, t in options:
            new_time = current_time + t
            if new_time <= 100:
                new_combinations.append((current_points + p, new_time))
    combinations.extend(new_combinations)

max_points = max(p for p, t in combinations if t <= 100)
print(max_points)
