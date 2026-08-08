

import matplotlib.pyplot as plt
import numpy as np

print("My challenge 1: Create a comprehensive multi-plot visualization using Matplotlib that tells a story about data.")
print("-" * 70)

fig, axes = plt.subplots(2,2, figsize=(14,10))

# Line plot
# top - left 
axes[0,0].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'b-o')
axes[0,0].set_title("Daily Website Traffic") 
axes[0,0].set_xlabel("Days", fontsize=12)
axes[0,0].set_ylabel("Noise", fontsize=12)
axes[0,0].grid(True, alpha=0.3) 

# Scatter plot
# top - right
axes[0,1].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'b-o')
axes[0,1].set_title("Marketing Spend vs Revenue")
axes[0,1].set_xlabel("Spend", fontsize=12)
axes[0,1].set_ylabel("Revenue", fontsize=12)
axes[0,1].grid(True, alpha=0.3)


# Histogram plot
# bottom - left
test_scores = np.random.normal(100, 30, 1000)
mean_score = test_scores.mean()
std_score = test_scores.std()

data = np.random.normal(1000)
axes[1, 0].hist(data, bins=30, color='green', alpha=0.7)
axes[1, 0].set_title("Distribution of Purchase Amounts")
axes[1, 0].axvline(mean_score, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_score:.1f}')
axes[1, 0].axvline(mean_score - std_score, color='orange', linestyle=':', linewidth=2, label=f'±1 Std Dev: {std_score:.1f}')
axes[1, 0].axvline(mean_score + std_score, color='orange', linestyle=':', linewidth=2)
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3, axis='y')
 
 
# Bar chart
# bottom - right
products = ['Python', 'JavaScript', 'Java', 'C++', 'Go', 'Rust']
quarters = ['Q1', 'Q2', 'Q3']
bars = axes[1, 1].bar(products, quarters, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F'])

for i, (bar, sale) in enumerate(zip(bars, quarters)):
    axes[1, 1].text(bar.get_x() + bar.get_width()/2, sale + 10,
            str(sale), ha='center', va='bottom', fontweight='bold') 
    
axes[1, 1].set_xlabel("Programming Language", fontsize=12)
axes[1, 1].set_ylabel("Quarters", fontsize=12)
axes[1, 1].set_title("Quarterly Revenue by Product")
axes[1, 1].grid(True, alpha=0.3, axis='y')



plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/my_plot_challenge_subplots.png')
plt.close()
