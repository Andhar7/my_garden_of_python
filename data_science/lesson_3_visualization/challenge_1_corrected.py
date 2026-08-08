# ============================================================================
# CHALLENGE 1: MATPLOTLIB FUNDAMENTALS — CORRECTED VERSION
# ============================================================================
#
# This shows the proper way to create each of the 4 plots
# Study the differences from your attempt!
#

import matplotlib.pyplot as plt
import numpy as np

print("=" * 70)
print("CHALLENGE 1: Comprehensive Multi-Plot Visualization")
print("=" * 70)
print()

# Create 2x2 subplot grid
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# ============================================================================
# PLOT 1: LINE PLOT (Top-Left) — Daily Website Traffic
# ============================================================================
print("Plot 1: Daily Website Traffic (Line Plot)")
print("-" * 70)

# Create 30 days of data with increasing trend + noise
days = np.arange(1, 31)  # 30 days
# Traffic increases from 100 to 500 with random noise
base_traffic = np.linspace(100, 500, 30)
noise = np.random.randn(30) * 20  # Add realistic noise
traffic = base_traffic + noise

# Plot
axes[0, 0].plot(days, traffic, 'b-o', linewidth=2, markersize=6)
axes[0, 0].set_title("Daily Website Traffic", fontsize=14, fontweight='bold')
axes[0, 0].set_xlabel("Days", fontsize=12)
axes[0, 0].set_ylabel("Visitors (thousands)", fontsize=12)  # Changed from "Noise"
axes[0, 0].grid(True, alpha=0.3)

print("✅ Created line plot with:")
print("   - 30 days of data")
print("   - Trend from 100 to 500 visitors")
print("   - Random noise added (realistic)")
print()


# ============================================================================
# PLOT 2: SCATTER PLOT (Top-Right) — Marketing Spend vs Revenue
# ============================================================================
print("Plot 2: Marketing Spend vs Revenue (Scatter + Trend Line)")
print("-" * 70)

# Create realistic data: more spending → more revenue
np.random.seed(42)
marketing_spend = np.random.uniform(1000, 20000, 50)  # $1K to $20K
# Revenue correlates with spending: revenue = 10 * spend + noise
revenue = 10 * marketing_spend + np.random.randn(50) * 50000

# Scatter plot
axes[0, 1].scatter(marketing_spend, revenue, alpha=0.6, s=80, color='green')

# Add trend line (regression line)
z = np.polyfit(marketing_spend, revenue, 1)
p = np.poly1d(z)
axes[0, 1].plot(marketing_spend, p(marketing_spend), "r--", linewidth=2.5, label="Trend line")

axes[0, 1].set_title("Marketing Spend vs Revenue", fontsize=14, fontweight='bold')
axes[0, 1].set_xlabel("Marketing Spend ($)", fontsize=12)
axes[0, 1].set_ylabel("Revenue ($)", fontsize=12)
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

print("✅ Created scatter plot with:")
print("   - Real data: marketing spend (X) vs revenue (Y)")
print("   - 50 data points")
print("   - Regression line showing trend")
print()


# ============================================================================
# PLOT 3: HISTOGRAM (Bottom-Left) — Distribution of Purchase Amounts
# ============================================================================
print("Plot 3: Distribution of Purchase Amounts (Histogram)")
print("-" * 70)

# Create customer purchase amounts: mean=$100, std_dev=$30, 1000 customers
purchase_amounts = np.random.normal(100, 30, 1000)  # FIXED: was np.random.normal(1000)

# Create histogram
axes[1, 0].hist(purchase_amounts, bins=30, color='skyblue',
                edgecolor='black', alpha=0.7)

# Calculate statistics
mean_amount = purchase_amounts.mean()
std_amount = purchase_amounts.std()

# Add mean line
axes[1, 0].axvline(mean_amount, color='red', linestyle='--',
                   linewidth=2.5, label=f'Mean: ${mean_amount:.2f}')

# Add ±1 standard deviation lines
axes[1, 0].axvline(mean_amount - std_amount, color='orange',
                   linestyle=':', linewidth=2,
                   label=f'±1 Std Dev: ${std_amount:.2f}')
axes[1, 0].axvline(mean_amount + std_amount, color='orange',
                   linestyle=':', linewidth=2)

axes[1, 0].set_title("Distribution of Purchase Amounts", fontsize=14, fontweight='bold')
axes[1, 0].set_xlabel("Purchase Amount ($)", fontsize=12)
axes[1, 0].set_ylabel("Number of Customers", fontsize=12)
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3, axis='y')

print("✅ Created histogram with:")
print("   - 1000 customer purchases")
print("   - Mean = ${:.2f}".format(mean_amount))
print("   - Std Dev = ${:.2f}".format(std_amount))
print("   - Mean and ±1 std dev lines shown")
print()


# ============================================================================
# PLOT 4: BAR CHART (Bottom-Right) — Quarterly Revenue by Product
# ============================================================================
print("Plot 4: Quarterly Revenue by Product (Grouped Bar Chart)")
print("-" * 70)

# Create quarterly revenue data for 5 products
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
Q1_revenue = [50000, 45000, 60000, 55000, 40000]
Q2_revenue = [60000, 52000, 65000, 62000, 48000]
Q3_revenue = [75000, 68000, 80000, 75000, 62000]

# Create grouped bar chart
x = np.arange(len(products))
width = 0.25  # Width of bars

bars1 = axes[1, 1].bar(x - width, Q1_revenue, width, label='Q1', color='#FF6B6B')
bars2 = axes[1, 1].bar(x, Q2_revenue, width, label='Q2', color='#4ECDC4')
bars3 = axes[1, 1].bar(x + width, Q3_revenue, width, label='Q3', color='#45B7D1')

# Add value labels on bars
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        axes[1, 1].text(bar.get_x() + bar.get_width()/2., height,
                       f'${int(height/1000)}K',
                       ha='center', va='bottom', fontsize=9)

axes[1, 1].set_title("Quarterly Revenue by Product", fontsize=14, fontweight='bold')
axes[1, 1].set_xlabel("Product", fontsize=12)
axes[1, 1].set_ylabel("Revenue ($)", fontsize=12)
axes[1, 1].set_xticks(x)
axes[1, 1].set_xticklabels(products, rotation=15, ha='right')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3, axis='y')

print("✅ Created grouped bar chart with:")
print("   - 5 products")
print("   - 3 quarters (Q1, Q2, Q3)")
print("   - Grouped bars for comparison")
print("   - Value labels on each bar")
print()


# ============================================================================
# FINALIZE AND SAVE
# ============================================================================

plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/challenge_1_solution.png',
            dpi=300, bbox_inches='tight')
plt.close()

print("=" * 70)
print("✅ CHALLENGE 1 COMPLETE!")
print("=" * 70)
print()
print("Plots created and saved as: challenge_1_solution.png")
print()
print("Summary of what each plot shows:")
print("  1. LINE PLOT (top-left):")
print("     Shows website traffic trend over 30 days")
print("     Pattern: Increasing traffic with daily fluctuations")
print()
print("  2. SCATTER + TREND LINE (top-right):")
print("     Shows relationship between marketing spend and revenue")
print("     Pattern: More spending → More revenue (positive correlation)")
print()
print("  3. HISTOGRAM (bottom-left):")
print("     Shows distribution of customer purchase amounts")
print("     Pattern: Normal distribution centered around $100")
print()
print("  4. GROUPED BAR CHART (bottom-right):")
print("     Shows quarterly revenue comparison across products")
print("     Pattern: Revenue increasing Q1→Q2→Q3 for all products")
print()
print("🙏 Key Insights from This Challenge:")
print("  - Figure/axes model for subplots")
print("  - Different plot types for different data stories")
print("  - Proper data generation (realistic data)")
print("  - Styling for readability (labels, grid, colors)")
print("  - Grouped bars for multi-dimensional comparison")
print()
