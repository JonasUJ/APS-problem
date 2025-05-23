timelimit = 100
n = int(input())

values = []  # happy-points
weights = []  # time

for _ in range(n):
    k, m, p, t = input().split()
    p = int(p)
    t = int(t)
    values.append(p)
    weights.append(t)

memo = [[0] * (timelimit + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    value = values[i - 1]
    weight = weights[i - 1]

    for w in range(1, timelimit + 1):
        if weight > w:
            memo[i][w] = memo[i - 1][w]
        else:
            memo[i][w] = max(
                memo[i - 1][w],
                memo[i - 1][w - weight] + value
            )

print(memo[n][timelimit])


