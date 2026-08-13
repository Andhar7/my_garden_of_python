

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Example 1: Create a normal distribution
print("=" * 72)
print("Example 1: Normal Distribution (Bell Curve)")
print("=" * 72)

# Generate 10,000 random numbers from normal distribution
# mean = 100 (center), std=15 (spread)
data = np.random.normal(loc=100, scale=15, size=10000)

print(f"\nData created: {len(data)} random numbers")
print(f"Mean: {np.mean(data):.2f}")
print(f"Median: {np.median(data):.2f}")
print(f"Std Dev: {np.std(data):.2f}")
print(f"Min: {np.min(data):.2f}")
print(f"Max: {np.max(data):.2f}")

# Visualize the distribution
plt.figure(figsize=(10, 6))
plt.hist(data, bins=50, density=True, alpha=0.7, color='blue', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Normal Distribution (Bell Curve)')
plt.grid(True, alpha=0.3)
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_4_statistics/dist_1_normal.png')
plt.close()

print("\nVisualization saved!")

# NUMBER : 1
# Mean (Average)
# Sum all values, divide by count
print("What is the mean of your generated data?")
data = [70, 80, 90, 100, 110]
result_mean = mean = sum(data) / len(data) 
print("Mean mean sum of data / on len of data: ")
print(f"Result of mean: {result_mean}")
# Or with NumPy 
result_numpy = mean = np.mean(data)
print(f"Result of mean with numpy: {result_numpy}")


# NUMBER : 2
print("\nWhat is the median?")
# Median (Middle Value)
# Sort data, take middle value
data = [70, 80, 90, 100, 110]
median_result = np.median(data)
print(f"Here middle of all data: {median_result}")
# if even count, average of two middle values


# NUMBER : 3
# Mode (Most Frequent)
# The value that appears most offen
data = [70, 80, 80, 80, 80, 90, 100, 110]
# Mode  = 80 - (appears 3 times)
from scipy import stats
result_of_mode = stats.mode(data, keepdims=True)[0][0]
print(f"Result of mode: {result_of_mode}") # 80 

# NUMBER : 4
# Standard Deviation (Spread)
# How far values spread from the mean
data = [70, 80, 90, 100, 110]
result_of_std = np.std(data) # = 14.14
print(result_of_std) # 14.142135623730951 - it mean that std function has round(2)
# Higher std = more spread out
# Lower std = tighter around mean

# NUMBER : 6
# Variance
# Standard Deviation squared
result_of_variance = np.var(data) # = std ** 2

print("What does the bell curve look like?")
print("Bell curve look like distribution of data...")

# Challenge 2: Prove the 68% rule
print("=" * 72)
print("Challenge 2: Prove the 68-95-99.7 Rule")
print("=" * 72)

mean = np.mean(data)
std = np.std(data)

# Count how many values fall within 1 standard deviation
within_1std = np.sum((data >= mean - std) & (data <= mean + std))
percent_1std = (within_1std / len(data)) * 100

print(f"\nMean: {mean:.2f}")
print(f"Std Dev: {std:.2f}")
print(f"\nRange for 1 Std Dev: {mean - std:.2f} to {mean + std:.2f}")
print(f"Expected within 1 Std Dev: {within_1std} out of {len(data)}")
print(f"Percentage: {percent_1std:.2f}%")
print(f"Expected: 68% (theory) vs {percent_1std:.2f}% (actual)")

# Count within 2 standard deviations
within_2std = np.sum((data >= mean - 2 * std) & (data <= mean + 2 * std))
percent_2std = (within_2std / len(data)) * 100

print(f"\nRange for 2 Std Dev: {mean - 2 * std:.2f} to {mean + 2 * std:.2f}")
print(f"Values within 2 Std Dev: {within_2std} out of {len(data)}")
print(f"Percentage: {percent_2std:.2f}%")
print(f"Expected: 95% (theory) vs {percent_2std:.2f}% (actual)")

# Count within 3 standard deviations
within_3std = np.sum((data >= mean - 3 * std) & (data <= mean + 3 * std))
percent_3std = (within_3std / len(data)) * 100

print(f"\nRange for 3 Std Dev: {mean - 3 * std:.2f} to {mean + 3 * std:.2f}")
print(f"Values within 3 Std Dev: {within_3std} out of {len(data)}")
print(f"Percentage: {percent_3std:.2f}%")
print(f"Expected: 99.7% (theory) vs {percent_3std:.2f}% (actual)")
print("\nThe 68-95-99.7 rule PROVEN with real data!")

















