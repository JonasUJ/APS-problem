import sys

def main():
    input_data = iter(sys.stdin.read().splitlines())

    while True:
        try:
            C, n = map(int, next(input_data).split())

            values = []
            weights = []

            for _ in range(n):
                value, weight = map(int, next(input_data).split())
                values.append(value)
                weights.append(weight)

            indices = knapsack(values, weights, C, n)

            print(len(indices))
            print(" ".join(map(str, indices)))

        except StopIteration:
            break

def backtrack_memo(memo, weights, capacity, n):
    indices = []
    remaining_capacity = capacity

    for i in range(n, 0, -1):
        if memo[i][remaining_capacity] != memo[i-1][remaining_capacity]:
            indices.append(i-1)
            remaining_capacity -= weights[i-1]

    return indices

def knapsack(values, weights, C, n):
    memo = [[0] * (C+1) for _ in range(n+1)] 

    for i in range(1, n+1):
        
        value = values[i-1]
        weight = weights[i-1]

        # 0 for all rows and columns of index 0
        for capacity in range(1, C+1):

            if weight > capacity:
                memo[i][capacity] = memo[i-1][capacity]

            else:
                memo[i][capacity] = max(
                    memo[i-1][capacity],
                    memo[i-1][capacity-weight] + value
                )
            
            # Could also do this:
            # memo[i][capacity] = memo[i-1][capacity]

            # if weight <= capacity and memo[i-1][capacity-weight] + value > memo[i][capacity]:
            #     memo[i][capacity] = memo[i-1][capacity-weight] + value

    return backtrack_memo(memo, weights, C, n)
    

def knapsack_rec(values, weights, c, n):
    memo = [[-1] * (c+1) for _ in range(n+1)]

    def go(i, w):
        if i == 0 or w == 0:
            return 0
        if memo[i][w] != -1:
            return memo[i][w]


        if weights[i-1] > w:
            memo[i-1][w] = go(i-1, w)
        else:
            memo[i][w] = max(
                go(i-1, w), # Dont take item
                go(i-1, w-weights[i-1]) + values[i-1] # Take item
            )

        return memo[i][w]

    _ = go(n, c)

    return backtrack_memo(memo, weights, c, n) 

if __name__ == "__main__":
    main()
