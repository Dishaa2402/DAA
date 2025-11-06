import time

def fractional_knapsack(values, weights, capacity):
    ratio = sorted([(v/w, v, w, i) for i, (v, w) in enumerate(zip(values, weights))], reverse=True)
    total_value, fractions, details = 0, [0]*len(values), []

    for r, v, w, i in ratio:
        if capacity <= 0: break
        take = min(w, capacity)
        f = take / w
        total_value += v * f
        fractions[i] = f
        capacity -= take
        details.append({'item': i+1, 'profit': v, 'weight': w, 'ratio': round(r,2),
                        'fraction': round(f,2), 'value_added': round(v*f,2)})
    return total_value, details

# Input
n = int(input("Enter number of items: "))
values, weights = [], []
for i in range(n):
    values.append(float(input(f"Value of item {i+1}: ")))
    weights.append(float(input(f"Weight of item {i+1}: ")))
capacity = float(input("Enter knapsack capacity: "))

# Execution
start = time.perf_counter()
max_val, data = fractional_knapsack(values, weights, capacity)
end = time.perf_counter()

# Output
print("\n--- Fractional Knapsack Selection Table ---")
print(f"{'Item':<6}{'Profit':<10}{'Weight':<10}{'Ratio':<10}{'Fraction Taken':<16}{'Value Added':<15}")
for d in data:
    print(f"{d['item']:<6}{d['profit']:<10}{d['weight']:<10}{d['ratio']:<10}{d['fraction']:<16}{d['value_added']:<15}")

print(f"\nTotal Cost / Maximum Profit = {max_val:.2f}")
print(f"Actual Execution Time: {end - start:.6f} seconds")
print("Time Complexity (theoretical): O(n log n)")


'''for loop logic:
if capacity <= 0: → 50 <= 0? No.
take = min(w, capacity) = min(10, 50) = 10
f = take / w = 10 / 10 = 1.0 (whole item)
total_value += v * f = 0 + 60 * 1.0 = 60.0
fractions[0] = 1.0 → fractions = [1.0, 0, 0]
capacity -= take = 50 - 10 = 40'''
