import time
import matplotlib.pyplot as plt
import random

# Iteratif

def find_highest_bid(bids):
    i = 0
    if len(bids) == 0:
        raise ValueError("Tidak ada tawaran yang tersedia")

    highest_bid = bids[0]
    for i in range(len(bids)):  
        if bids[i] > highest_bid:
            highest_bid = bids[i]

    return highest_bid

#recursive

def find_max_recursive(prices, index=0):
    if index == len(prices) - 1:
        return prices[index]
    max_rest = find_max_recursive(prices, index + 1)
    if prices[index] > max_rest:
        return prices[index]
    else:
        return max_rest

input_sizes = [10, 100, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
execution_times = []

for size in input_sizes:
    bids = [random.randint(1, 10000000) for _ in range(size)]

    start_time = time.time()
    find_highest_bid(bids)
    end_time = time.time()

    execution_times.append(end_time - start_time)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, execution_times, marker='o', linestyle='-', color='b', label='Execution Time')
plt.title('Time Complexity Analysis of find_highest_bid')
plt.xlabel('Input Size (Number of Bids)')
plt.ylabel('Execution Time (Seconds)')
plt.grid(True)
plt.legend()
plt.show()
