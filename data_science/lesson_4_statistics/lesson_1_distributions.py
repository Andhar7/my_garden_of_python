

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
