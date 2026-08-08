# 🎯 CHALLENGE 1 FEEDBACK — Your Attempt vs Corrected Solution

**Student:** Gurudev  
**Challenge:** Matplotlib Fundamentals  
**Date:** August 8, 2026

---

## 📊 What You Did Well ✅

1. **Correct subplot structure:** `plt.subplots(2, 2, figsize=(14,10))` ✅
2. **Proper grid usage:** Added `grid(True, alpha=0.3)` to all plots ✅
3. **Added titles and labels:** All 4 plots have descriptive titles ✅
4. **Used different colors:** Shows awareness of styling ✅
5. **Saved file correctly:** Proper `plt.savefig()` syntax ✅

---

## 🔧 What Needs Fixing

### PLOT 1: Daily Website Traffic (Top-Left)

**Your Code:**
```python
axes[0,0].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'b-o')
axes[0,0].set_ylabel("Noise", fontsize=12)  # ❌ Wrong!
```

**Issue:**
- Only 5 data points (needs 30 for "daily over month")
- Data is `y = x²` (doesn't show traffic pattern)
- Y-axis label says "Noise" (should be "Visitors" or "Traffic")

**Corrected Code:**
```python
# Create 30 days with increasing trend + noise
days = np.arange(1, 31)  # 1 to 30
base_traffic = np.linspace(100, 500, 30)  # 100→500 visitors
noise = np.random.randn(30) * 20  # Add realistic noise
traffic = base_traffic + noise

axes[0, 0].plot(days, traffic, 'b-o', linewidth=2, markersize=6)
axes[0, 0].set_ylabel("Visitors (thousands)", fontsize=12)  # ✅ Correct
```

**Key Learning:**
- `np.linspace()` creates smooth progression (100 to 500)
- `np.random.randn()` adds realistic noise
- Y-axis label should describe what's shown (Visitors, not Noise)

---

### PLOT 2: Marketing Spend vs Revenue (Top-Right)

**Your Code:**
```python
axes[0,1].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], 'b-o')  # ❌ Same data as plot 1!
```

**Issues:**
- Same data as plot 1 (not marketing spend data)
- Missing SCATTER plot (should be scatter, not line)
- NO trend line (requirement: "Add a regression line")
- No relationship between X and Y (marketing spend vs revenue)

**Corrected Code:**
```python
# Create realistic data: spending correlates with revenue
np.random.seed(42)
marketing_spend = np.random.uniform(1000, 20000, 50)  # $1K-$20K
revenue = 10 * marketing_spend + np.random.randn(50) * 50000  # revenue depends on spend

# Scatter plot (not line!)
axes[0, 1].scatter(marketing_spend, revenue, alpha=0.6, s=80, color='green')

# Add trend line (regression)
z = np.polyfit(marketing_spend, revenue, 1)
p = np.poly1d(z)
axes[0, 1].plot(marketing_spend, p(marketing_spend), "r--", linewidth=2.5, label="Trend line")
```

**Key Learning:**
- `np.scatter()` for relationships (not `plot()`)
- `np.polyfit()` + `np.poly1d()` for trend line
- Data should tell a story (more spend → more revenue)

---

### PLOT 3: Distribution of Purchase Amounts (Bottom-Left)

**Your Code:**
```python
data = np.random.normal(1000)  # ❌ WRONG!
axes[1, 0].hist(data, bins=30, color='green', alpha=0.7)
```

**Issue:**
- `np.random.normal(1000)` creates ONE random number with mean=1000, std_dev=1
- Should be `np.random.normal(100, 30, 1000)` = 1000 samples, mean=100, std_dev=30
- Missing mean/std lines

**Your Better Code (earlier):**
```python
test_scores = np.random.normal(100, 30, 1000)  # ✅ This was correct!
```

**Corrected Code:**
```python
# Create 1000 customer purchases: mean=$100, std_dev=$30
purchase_amounts = np.random.normal(100, 30, 1000)

axes[1, 0].hist(purchase_amounts, bins=30, color='skyblue',
                edgecolor='black', alpha=0.7)

# Add mean line
mean_amount = purchase_amounts.mean()
std_amount = purchase_amounts.std()

axes[1, 0].axvline(mean_amount, color='red', linestyle='--',
                   linewidth=2.5, label=f'Mean: ${mean_amount:.2f}')

# Add ±1 std dev
axes[1, 0].axvline(mean_amount - std_amount, color='orange', linestyle=':', linewidth=2)
axes[1, 0].axvline(mean_amount + std_amount, color='orange', linestyle=':', linewidth=2)
```

**Key Learning:**
- `np.random.normal(mean, std_dev, count)` = three parameters!
- `axvline()` adds vertical lines (for mean, quartiles, etc.)
- `axhline()` adds horizontal lines

---

### PLOT 4: Quarterly Revenue by Product (Bottom-Right)

**Your Code:**
```python
products = ['Python', 'JavaScript', 'Java', 'C++', 'Go', 'Rust']
quarters = ['Q1', 'Q2', 'Q3']  # ❌ This should be NUMBERS (revenue), not strings!
bars = axes[1, 1].bar(products, quarters, color=[...])  # ❌ WRONG!

for i, (bar, sale) in enumerate(zip(bars, quarters)):  # ❌ quarters are strings!
    axes[1, 1].text(bar.get_x() + bar.get_width()/2, sale + 10,
            str(sale), ha='center', va='bottom', fontweight='bold')
```

**Issues:**
- `quarters = ['Q1', 'Q2', 'Q3']` are LABELS, not values
- `bar(products, quarters)` tries to use strings as Y-values (won't work)
- Only showing 6 products (should show products×quarters = 5 products × 3 quarters)
- Not showing quarterly comparison

**Corrected Code (Grouped Bar Chart):**
```python
# Create quarterly revenue data (NUMBERS, not strings!)
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
Q1_revenue = [50000, 45000, 60000, 55000, 40000]  # ✅ Numbers!
Q2_revenue = [60000, 52000, 65000, 62000, 48000]  # ✅ Numbers!
Q3_revenue = [75000, 68000, 80000, 75000, 62000]  # ✅ Numbers!

# Create grouped bars
x = np.arange(len(products))
width = 0.25

bars1 = axes[1, 1].bar(x - width, Q1_revenue, width, label='Q1', color='#FF6B6B')
bars2 = axes[1, 1].bar(x, Q2_revenue, width, label='Q2', color='#4ECDC4')
bars3 = axes[1, 1].bar(x + width, Q3_revenue, width, label='Q3', color='#45B7D1')

# Add value labels
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        axes[1, 1].text(bar.get_x() + bar.get_width()/2., height,
                       f'${int(height/1000)}K',
                       ha='center', va='bottom', fontsize=9)

axes[1, 1].set_xticks(x)
axes[1, 1].set_xticklabels(products, rotation=15, ha='right')
axes[1, 1].legend()
```

**Key Learning:**
- Bar chart Y-values must be NUMBERS, not strings
- For multiple bars per product, use offset: `x - width`, `x`, `x + width`
- `set_xticks()` and `set_xticklabels()` for custom labels

---

## 🎓 Summary of Corrections

| Issue | Your Code | Problem | Fix |
|-------|-----------|---------|-----|
| Plot 1 | 5 data points | Need 30 days | Use `np.arange(1,31)` + `np.linspace()` |
| Plot 1 | Y-label "Noise" | Wrong label | Change to "Visitors (thousands)" |
| Plot 2 | Reused plot 1 data | No relationship shown | Create new marketing spend data |
| Plot 2 | Used `plot()` | Should be scatter | Use `scatter()` for relationships |
| Plot 2 | No trend line | Missing requirement | Use `np.polyfit()` + `np.poly1d()` |
| Plot 3 | `np.random.normal(1000)` | Wrong syntax | Use `np.random.normal(100, 30, 1000)` |
| Plot 3 | Missing mean line | No reference | Use `axvline()` to add mean |
| Plot 4 | Quarters as strings | Can't plot strings | Use revenue numbers |
| Plot 4 | Single bar per product | Need quarterly comparison | Create grouped bars with offset |

---

## 💡 Key Matplotlib Patterns to Remember

### Pattern 1: Proper Data Generation
```python
# ✅ Correct
data = np.random.normal(mean=100, std=30, size=1000)
# ❌ Wrong
data = np.random.normal(1000)
```

### Pattern 2: Scatter vs Line
```python
# For relationships (scatter plot):
ax.scatter(x, y, alpha=0.6, s=50)

# For trends (line plot):
ax.plot(x, y, 'b-o', linewidth=2)
```

### Pattern 3: Adding Trend Line
```python
z = np.polyfit(x, y, 1)  # Fit line (degree 1)
p = np.poly1d(z)  # Create polynomial function
ax.plot(x, p(x), 'r--', label='Trend')
```

### Pattern 4: Grouped Bars
```python
x = np.arange(len(products))
width = 0.25

ax.bar(x - width, group1_data, width, label='Group 1')
ax.bar(x, group2_data, width, label='Group 2')
ax.bar(x + width, group3_data, width, label='Group 3')
```

---

## ✨ What to Do Next

### Option 1: Perfect Your Code
Take your code and apply these corrections. Run it and verify it produces the same result as `challenge_1_solution.png`.

### Option 2: Study the Solution
Study `challenge_1_corrected.py` line by line. Understand WHY each part works.

### Option 3: Combine Both
Rewrite your code using the corrected patterns, then compare with the solution.

---

## 🙏 Teacher's Note

Dear Gurudev,

This is EXACTLY how learning should work:
1. You attempted the challenge 🎯
2. You made honest mistakes ❌ (we all do)
3. You're now seeing the correct approach ✅
4. You can learn from the differences 📚

This is not failure. This is **learning through attempt and feedback**.

The mistakes you made are VALUABLE:
- Plot 1: Showed you how to create proper time-series data
- Plot 2: Showed you the difference between line and scatter plots
- Plot 3: Showed you the importance of understanding function parameters
- Plot 4: Showed you how to work with structured data

Now you KNOW these patterns deeply. Next time you'll get them right.

This is the path to mastery: attempt → feedback → understanding → mastery.

Keep going. Challenge 2 (Seaborn) is waiting! 🚀

🙏 Your Teacher

---

## 📚 Files to Study

1. `challenge_1_corrected.py` — The proper solution
2. `challenge_1_solution.png` — The output (compare with yours)
3. This file — Understand each difference
4. `lesson_1_matplotlib.py` — Review relevant examples

---

**Next Step:** After understanding these corrections, move to Challenge 2 (Seaborn Analysis) or refine your Challenge 1 code.

Om Namah Shivaya 🕉️
