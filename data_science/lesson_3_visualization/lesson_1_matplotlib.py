# ============================================================================
# PHASE 2.2 — LESSON 1: MATPLOTLIB FUNDAMENTALS
# ============================================================================
#
# "Data without visualization is like a garden without eyes to see it."
#
# Visualization is not decoration. It is REVELATION.
# It shows patterns that numbers cannot whisper.
#
# ============================================================================


import matplotlib.pyplot as plt
import numpy as np

# try:
#     import numpy as np  # pyright: ignore[reportMissingImports]
# except ImportError:
#     numpy = None

# ============================================================================
# PART 1: THE CORE CONCEPT — Figure and Axes
# ============================================================================
#
# matplotlib works like a painter:
#   - Figure = The canvas
#   - Axes = The area where you draw
#   - Plot = The art on the canvas
#

print("=" * 70)
print("MATPLOTLIB FUNDAMENTALS - LESSON 1")
print("=" * 70)
print()

# --- Example 1: Simplest Plot ---
print("EXAMPLE 1: Simplest Line Plot")
print("-" * 70)

# Create figure and axes (the canvas and drawing area)
fig, ax = plt.subplots()
print(fig, ax)

# Data
x = [122, 233, 333, 433, 5333]
y = [23, 43, 65, 85, 105]

# Plot (draw on the axes)
result_ax = ax.plot(x, y)
print(f"Result_ax: {result_ax}")

# Labels (tell the story)
time = ax.set_xlabel("Time (days)")
grow = ax.set_ylabel("Growth (units)")
linear = ax.set_title("Simple Linear Growth")
print(time)
print(grow)
print(linear)

# Save instead of showing (for learning purposes)
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_1_simple.png')
plt.close()

print("✅ Created simple line plot")
print("   - x = [1, 2, 3, 4, 5]")
print("   - y = [2, 4, 6, 8, 10]")
print("   - Result: Linear growth visualization")
print()


# ============================================================================
# PART 2: LINE PLOTS — Following Trends
# ============================================================================

print("EXAMPLE 2: Line Plot with Multiple Lines")
print("-" * 70)

fig, ax = plt.subplots(figsize=(10, 6))

# Two time series (imagine: temperature and humidity over days)
days = np.arange(1, 31)
temperature = 20 + 5 * np.sin(days / 5) + np.random.randn(30) * 0.5
humidity = 60 + 10 * np.cos(days / 4) + np.random.randn(30) * 1

# Plot both on same axes
ax.plot(days, temperature, label="Temperature (°C)", marker='o', linewidth=2)
ax.plot(days, humidity, label="Humidity (%)", marker='s', linewidth=2)

# Styling
ax.set_xlabel("Days", fontsize=12)
ax.set_ylabel("Values", fontsize=12)
ax.set_title("Temperature and Humidity Over 30 Days", fontsize=14, fontweight='bold')
ax.legend()  # Show labels
ax.grid(True, alpha=0.3)  # Add grid for readability

plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_2_multiline.png')
plt.close()

print("✅ Created multi-line plot")
print("   - Shows two trends together")
print("   - Different markers and colors")
print("   - Legend to distinguish lines")
print()


# ============================================================================
# PART 3: SCATTER PLOTS — Finding Relationships
# ============================================================================

print("EXAMPLE 3: Scatter Plot (Correlation)")
print("-" * 70)

fig, ax = plt.subplots(figsize=(10, 6))

# Imagine: Study hours vs Exam scores (100 students)
np.random.seed(42)
study_hours = np.random.uniform(0, 10, 100)
exam_scores = 50 + 5 * study_hours + np.random.randn(100) * 5

# Scatter plot
ax.scatter(study_hours, exam_scores, alpha=0.6, s=50, color='blue')

# Add trend line (linear regression)
z = np.polyfit(study_hours, exam_scores, 1)
p = np.poly1d(z)
ax.plot(study_hours, p(study_hours), "r--", linewidth=2, label="Trend line")

ax.set_xlabel("Study Hours", fontsize=12)
ax.set_ylabel("Exam Score", fontsize=12)
ax.set_title("Relationship: Study Hours vs Exam Scores", fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)

plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_3_scatter.png')
plt.close()

print("✅ Created scatter plot")
print("   - Shows relationship between two variables")
print("   - Includes trend line")
print("   - alpha=0.6 shows overlapping points (transparency)")
print()


# ============================================================================
# PART 4: BAR CHARTS — Comparing Categories
# ============================================================================

print("EXAMPLE 4: Bar Chart (Comparing Categories)")
print("-" * 70)

fig, ax = plt.subplots(figsize=(10, 6))

# Data: Sales by product (imagine a store)
products = ['Python', 'JavaScript', 'Java', 'C++', 'Go', 'Rust']
sales = [450, 380, 320, 290, 210, 150]

# Bar chart
bars = ax.bar(products, sales, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F'])

# Add value labels on top of bars
for i, (bar, sale) in enumerate(zip(bars, sales)):
    ax.text(bar.get_x() + bar.get_width()/2, sale + 10,
            str(sale), ha='center', va='bottom', fontweight='bold')

ax.set_xlabel("Programming Language", fontsize=12)
ax.set_ylabel("Sales ($)", fontsize=12)
ax.set_title("Sales by Programming Language", fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_4_bar.png')
plt.close()

print("✅ Created bar chart")
print("   - Shows comparison across categories")
print("   - Color-coded for visual appeal")
print("   - Values displayed on bars")
print()


# ============================================================================
# PART 5: HISTOGRAM — Distribution of Data
# ============================================================================

print("EXAMPLE 5: Histogram (Distribution)")
print("-" * 70)

fig, ax = plt.subplots(figsize=(10, 6))

# Data: Test scores of 1000 students
test_scores = np.random.normal(70, 15, 1000)  # Mean=70, StdDev=15

# Histogram
ax.hist(test_scores, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

# Add mean and std dev lines
mean_score = test_scores.mean()
std_score = test_scores.std()

ax.axvline(mean_score, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_score:.1f}')
ax.axvline(mean_score - std_score, color='orange', linestyle=':', linewidth=2, label=f'±1 Std Dev: {std_score:.1f}')
ax.axvline(mean_score + std_score, color='orange', linestyle=':', linewidth=2)

ax.set_xlabel("Test Score", fontsize=12)
ax.set_ylabel("Frequency (Number of Students)", fontsize=12)
ax.set_title("Distribution of Test Scores (1000 Students)", fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_5_histogram.png')
plt.close()

print("✅ Created histogram")
print("   - Shows distribution of values")
print("   - Mean line: red dashed")
print("   - Standard deviation: orange dotted")
print("   - bins=30: divides data into 30 segments")
print()


# ============================================================================
# PART 6: SUBPLOTS — Multiple Plots Together
# ============================================================================

print("EXAMPLE 6: Multiple Subplots (2x2 Grid)")
print("-" * 70)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Subplot 1: Line plot
axes[0, 0].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'b-o')
axes[0, 0].set_title("Line Plot: y = x²")
axes[0, 0].grid(True, alpha=0.3)

# Subplot 2: Scatter plot
x_scatter = np.random.randn(100)
y_scatter = np.random.randn(100)
axes[0, 1].scatter(x_scatter, y_scatter, alpha=0.5)
axes[0, 1].set_title("Scatter Plot: Random Data")
axes[0, 1].grid(True, alpha=0.3)

# Subplot 3: Bar chart
axes[1, 0].bar(['A', 'B', 'C', 'D'], [10, 24, 36, 18])
axes[1, 0].set_title("Bar Chart: Categories")
axes[1, 0].grid(True, alpha=0.3, axis='y')

# Subplot 4: Histogram
data = np.random.normal(0, 1, 1000)
axes[1, 1].hist(data, bins=30, color='green', alpha=0.7)
axes[1, 1].set_title("Histogram: Normal Distribution")
axes[1, 1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_6_subplots.png')
plt.close()

print("✅ Created 2x2 subplot grid")
print("   - Top-left: Line plot")
print("   - Top-right: Scatter plot")
print("   - Bottom-left: Bar chart")
print("   - Bottom-right: Histogram")
print()


# ============================================================================
# PART 7: UNDERSTANDING THE WHY
# ============================================================================

print("=" * 70)
print("WHY VISUALIZATIONS MATTER")
print("=" * 70)
print()

print("1. LINE PLOTS — Show trends over time")
print("   When to use: Time series, trends, changes")
print("   Example: Stock prices, temperature, growth")
print()

print("2. SCATTER PLOTS — Show relationships between two variables")
print("   When to use: Correlation, causation, outliers")
print("   Example: Height vs weight, age vs salary")
print()

print("3. BAR CHARTS — Compare values across categories")
print("   When to use: Categories, comparison, ranking")
print("   Example: Sales by region, population by country")
print()

print("4. HISTOGRAMS — Show distribution of data")
print("   When to use: Distribution, normality, outliers")
print("   Example: Test scores, income distribution, heights")
print()

print("5. BOX PLOTS — Show spread and outliers")
print("   When to use: Distribution, comparison, quality control")
print("   Example: Comparing test scores across classes")
print()

print("6. HEATMAPS — Show relationships in 2D data")
print("   When to use: Correlation, intensity, patterns")
print("   Example: Correlation matrix, temperature maps")
print()


# ============================================================================
# PART 8: KEY MATPLOTLIB CONCEPTS
# ============================================================================

print("=" * 70)
print("KEY MATPLOTLIB CONCEPTS")
print("=" * 70)
print()

print("1. FIGURE: The overall window/canvas")
print("   fig, ax = plt.subplots()")
print()

print("2. AXES: The actual plot area where you draw")
print("   ax.plot(), ax.scatter(), ax.bar()")
print()

print("3. PLOT METHODS:")
print("   - ax.plot(x, y)          : Line plot")
print("   - ax.scatter(x, y)       : Scatter plot")
print("   - ax.bar(categories, values) : Bar chart")
print("   - ax.hist(data, bins)    : Histogram")
print()

print("4. STYLING:")
print("   - ax.set_xlabel('label') : X-axis label")
print("   - ax.set_ylabel('label') : Y-axis label")
print("   - ax.set_title('title')  : Plot title")
print("   - ax.legend()            : Show labels")
print("   - ax.grid(True)          : Show grid")
print()

print("5. SAVING PLOTS:")
print("   plt.savefig('filename.png')")
print("   plt.savefig('filename.pdf')  # For print quality")
print()

print("6. DISPLAYING PLOTS:")
print("   plt.show()  # Shows interactive window")
print()


# ============================================================================
# PART 9: COLORS AND MARKERS
# ============================================================================

print("=" * 70)
print("COLORS AND MARKERS IN MATPLOTLIB")
print("=" * 70)
print()

print("COLORS:")
print("  - Named: 'red', 'blue', 'green', 'black', 'white'")
print("  - Hex: '#FF6B6B', '#4ECDC4'")
print("  - RGB: (1.0, 0.5, 0.5)")  # Values 0-1
print()

print("MARKERS (for scatter or line plots):")
print("  - 'o' : Circle")
print("  - 's' : Square")
print("  - '^' : Triangle")
print("  - '*' : Star")
print("  - '+' : Plus")
print("  - 'x' : X mark")
print()

print("LINE STYLES:")
print("  - '-'  : Solid line")
print("  - '--' : Dashed line")
print("  - ':' : Dotted line")
print("  - '-.' : Dash-dot line")
print()


# ============================================================================
# SUMMARY
# ============================================================================

print()
print("=" * 70)
print("LESSON 1 COMPLETE ✅")
print("=" * 70)
print()
print("What you learned:")
print("  ✅ Figure and axes (the canvas)")
print("  ✅ Line plots (trends)")
print("  ✅ Scatter plots (relationships)")
print("  ✅ Bar charts (comparisons)")
print("  ✅ Histograms (distributions)")
print("  ✅ Subplots (multiple plots together)")
print("  ✅ Styling and customization")
print()
print("All plots have been saved as PNG files in the same folder.")
print()
print("Next: Lesson 2 - Seaborn for Beautiful Statistical Plots")
print()
print("🙏 Keep learning, dear student. Visualization is the language of data. 🙏")
