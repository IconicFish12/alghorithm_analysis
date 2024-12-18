import time
import matplotlib.pyplot as plt
import random

def find_highest_bid(bids):
    if len(bids) == 0:
        raise ValueError("No bids available")

    highest_bid = bids[0]
    for bid in bids:
        if bid > highest_bid:
            highest_bid = bid

    return highest_bid

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
