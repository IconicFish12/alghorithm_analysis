import random
import time
import matplotlib.pyplot as plt
import sys

# Set recursion limit
sys.setrecursionlimit(20000)

# Iterative function to find the maximum price
def find_max_iterative(prices):
    max_price = prices[0]
    for price in prices:
        if price > max_price:
            max_price = price
    return max_price

# Recursive function without max()
def find_max_recursive(prices, index=0):
    if index == len(prices) - 1:
        return prices[index]
    max_rest = find_max_recursive(prices, index + 1)
    if prices[index] > max_rest:
        return prices[index]
    else:
        return max_rest

# Generate random data and measure execution time
def measure_execution_times():
    sizes = [10, 100, 1000, 10000]  # Updated sizes
    iterative_times = []
    recursive_times = []

    for size in sizes:
        data = [random.randint(1, 1000000) for _ in range(size)]
        
        # Measure iterative time
        start_time = time.time()
        find_max_iterative(data)
        end_time = time.time()
        iterative_times.append(end_time - start_time)

        # Measure recursive time
        start_time = time.time()
        find_max_recursive(data)
        end_time = time.time()
        recursive_times.append(end_time - start_time)
    
    return sizes, iterative_times, recursive_times

# Visualize execution times
def visualize_execution_times(sizes, iterative_times, recursive_times):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, iterative_times, label="Iterative", marker='o')
    plt.plot(sizes, recursive_times, label="Recursive", marker='x')
    plt.xlabel("Input Size (number of elements)")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time: Iterative vs Recursive Sequential Search")
    plt.legend()
    plt.grid(True)
    plt.show()

# Main execution
sizes, iterative_times, recursive_times = measure_execution_times()
visualize_execution_times(sizes, iterative_times, recursive_times)

# Print times for reference
for size, iter_time, rec_time in zip(sizes, iterative_times, recursive_times):
    print(f"Size: {size}, Iterative Time: {iter_time:.6f} s, Recursive Time: {rec_time:.6f} s")