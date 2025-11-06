import time

def fibonacci_iterative(n):
    steps = 0  # Step counter

    start_time = time.time()  # Start timer

    if n == 0:
        steps += 1
        end_time = time.time()
        return 0, steps, end_time - start_time
    elif n == 1:
        steps += 1
        end_time = time.time()
        return 1, steps, end_time - start_time

    a, b = 0, 1
    steps += 2  # Initialization of a and b

    for i in range(2, n + 1):
        steps += 1  # Loop iteration step
        a, b = b, a + b
        steps += 1  # Assignment step

    end_time = time.time()  # End timer
    return b, steps, end_time - start_time


def fibonacci_recursive(n, steps=0):
    steps += 1  # Count this function call as a step

    if n == 0:
        return 0, steps, 0
    elif n == 1:
        return 1, steps, 0
    else:
        # Measure time for recursive calls separately (not total time directly)
        fib1, steps, _ = fibonacci_recursive(n - 1, steps)
        fib2, steps, _ = fibonacci_recursive(n - 2, steps)
        return fib1 + fib2, steps, 0


def fibonacci_recursive_with_timer(n):
    steps = 0
    start_time = time.time()
    fib, steps, _ = fibonacci_recursive(n, steps)
    end_time = time.time()
    return fib, steps, end_time - start_time


# Example run
n = 20

fib_iter, steps_iter, time_iter = fibonacci_iterative(n)
fib_recur, steps_recur, time_recur = fibonacci_recursive_with_timer(n)

print(f"Iterative Fibonacci({n}) = {fib_iter}, Steps = {steps_iter}, Time = {time_iter:.6f} seconds")
print(f"Recursive Fibonacci({n}) = {fib_recur}, Steps = {steps_recur}, Time = {time_recur:.6f} seconds")

