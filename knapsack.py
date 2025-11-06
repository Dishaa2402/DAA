import time

def fractional_knapsack(values, weights, capacity):
    ratio = [(v / w, v, w, i) for i, (v, w) in enumerate(zip(values, weights))]
    ratio.sort(key=lambda x: x[0], reverse=True)

    total_value = 0.0
    fractions = [0] * len(values)
    detailed_info = []

    for r, v, w, i in ratio:
        if capacity == 0:
            break
        amount = min(w, capacity)
        fraction_taken = amount / w
        value_added = amount * r
        total_value += value_added
        fractions[i] = fraction_taken
        capacity -= amount

        detailed_info.append({
            'item': i + 1,
            'profit': v,
            'weight': w,
            'ratio': round(r, 2),
            'fraction': round(fraction_taken, 2),
            'value_added': round(value_added, 2)
        })

    return total_value, detailed_info

# Input from user
n = int(input("Enter number of items: "))
values = []
weights = []

for i in range(n):
    v = float(input(f"Enter profit/value of item {i+1}: "))
    w = float(input(f"Enter weight of item {i+1}: "))
    values.append(v)
    weights.append(w)

capacity = float(input("Enter total weight capacity of the knapsack: "))

# Measure execution time
start_time = time.perf_counter()
max_value, table_data = fractional_knapsack(values, weights, capacity)
end_time = time.perf_counter()
elapsed_time = end_time - start_time

# Output table
print("\n--- Fractional Knapsack Selection Table ---")
print(f"{'Item':<6}{'Profit':<10}{'Weight':<10}{'Ratio':<10}{'Fraction Taken':<16}{'Value Added':<15}")
for row in table_data:
    print(f"{row['item']:<6}{row['profit']:<10}{row['weight']:<10}{row['ratio']:<10}"
          f"{row['fraction']:<16}{row['value_added']:<15}")

print(f"\nTotal Cost / Maximum Profit = {max_value:.2f}")

# Print actual execution time
print(f"\nActual Execution Time: {elapsed_time:.6f} seconds")
print("Time Complexity (theoretical): O(n log n)")

