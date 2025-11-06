def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]

# Taking input from the user
n = int(input("Enter the number of items: "))

values = []
weights = []

print("Enter the values of the items:")
for i in range(n):
    val = int(input(f"Value of item {i+1}: "))
    values.append(val)

print("Enter the weights of the items:")
for i in range(n):
    wt = int(input(f"Weight of item {i+1}: "))
    weights.append(wt)

capacity = int(input("Enter the capacity of the knapsack: "))

max_value = knapsack_01(values, weights, capacity)
print(f"Maximum value that can be put in the knapsack: {max_value}")
