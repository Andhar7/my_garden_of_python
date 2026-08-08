# ============================================================================
# PHASE 2.2 — LESSON 2: SEABORN FOR BEAUTIFUL STATISTICAL PLOTS
# ============================================================================
#
# "Seaborn builds on Matplotlib but makes beautiful plots easy."
#
# Matplotlib is the foundation. Seaborn is the artistry.
# Seaborn works WITH DataFrames (Pandas integration!)
#
# ============================================================================

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Set style once, beautiful everywhere
sns.set_style("whitegrid")
sns.set_palette("husl")

print("=" * 70)
print("SEABORN FUNDAMENTALS - LESSON 2")
print("=" * 70)
print()

# ============================================================================
# PART 1: SEABORN vs MATPLOTLIB
# ============================================================================

print("SEABORN vs MATPLOTLIB")
print("-" * 70)
print()

print("MATPLOTLIB:")
print("  - Low-level, more control")
print("  - Works with lists and arrays")
print("  - More code for beautiful plots")
print()

print("SEABORN:")
print("  - High-level, quick beautiful plots")
print("  - Works seamlessly with Pandas DataFrames")
print("  - Statistical estimation built-in")
print("  - Beautiful color palettes")
print()


# ============================================================================
# PART 2: WORKING WITH SEABORN + PANDAS
# ============================================================================

print("=" * 70)
print("EXAMPLE 1: Seaborn with Pandas DataFrames")
print("-" * 70)

# Create sample dataset (student performance)
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank',
                'Grace', 'Henry', 'Iris', 'Jack'] * 3,
    'Subject': ['Math'] * 10 + ['Science'] * 10 + ['English'] * 10,
    'Score': np.random.randint(60, 100, 30),
    'Hours_Studied': np.random.randint(1, 10, 30)
}

df = pd.DataFrame(data)

print("Dataset created:")
print(df.head(10))
print()


# ============================================================================
# EXAMPLE 2: Distribution Plots
# ============================================================================

print("EXAMPLE 2: Distribution Plots (How data is spread)")
print("-" * 70)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# histplot: Distribution with histogram
sns.histplot(data=df, x='Score', kde=True, ax=axes[0, 0])
axes[0, 0].set_title("Histogram with KDE (Kernel Density Estimate)")

# kdeplot: Smooth distribution curve
sns.kdeplot(data=df, x='Score', ax=axes[0, 1], fill=True)
axes[0, 1].set_title("KDE Plot (Smooth Distribution)")

# boxplot: Distribution and outliers
sns.boxplot(data=df, x='Subject', y='Score', ax=axes[1, 0])
axes[1, 0].set_title("Box Plot (Shows outliers and spread)")

# violinplot: Distribution shape
sns.violinplot(data=df, x='Subject', y='Score', ax=axes[1, 1])
axes[1, 1].set_title("Violin Plot (Distribution shape)")

plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_7_distributions.png')
plt.close()

print("✅ Created 4 distribution plots")
print("   - histplot: Histogram with smooth curve")
print("   - kdeplot: Pure smooth distribution")
print("   - boxplot: Shows quartiles and outliers")
print("   - violinplot: Shows full distribution shape")
print()


# ============================================================================
# EXAMPLE 3: Relationship Plots
# ============================================================================

print("EXAMPLE 3: Relationship Plots (Between two variables)")
print("-" * 70)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# scatterplot: Points colored by category
sns.scatterplot(data=df, x='Hours_Studied', y='Score',
                hue='Subject', s=100, ax=axes[0, 0])
axes[0, 0].set_title("Scatter Plot (colored by Subject)")

# regplot: Scatter with regression line
sns.regplot(data=df, x='Hours_Studied', y='Score', ax=axes[0, 1])
axes[0, 1].set_title("Regression Plot (with trend line)")

# lmplot-style comparison (multiple regression lines)
# We'll use multiple regplot calls
for subject in df['Subject'].unique():
    subset = df[df['Subject'] == subject]
    sns.regplot(data=subset, x='Hours_Studied', y='Score',
                ax=axes[1, 0], label=subject, scatter=True)
axes[1, 0].set_title("Multiple Regression Lines (by Subject)")
axes[1, 0].legend()

# swarmplot: Shows individual points clearly
sns.swarmplot(data=df, x='Subject', y='Score', ax=axes[1, 1])
axes[1, 1].set_title("Swarm Plot (All individual points)")

plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_8_relationships.png')
plt.close()

print("✅ Created 4 relationship plots")
print("   - scatterplot: Colored points by category")
print("   - regplot: Scatter + regression line + confidence interval")
print("   - Multiple regplot: Compare trends by group")
print("   - swarmplot: All points, spread to avoid overlap")
print()


# ============================================================================
# EXAMPLE 4: Categorical Plots
# ============================================================================

print("EXAMPLE 4: Categorical Plots (Compare across groups)")
print("-" * 70)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# barplot: Average per category
sns.barplot(data=df, x='Subject', y='Score', ax=axes[0, 0])
axes[0, 0].set_title("Bar Plot (Average Score by Subject)")

# countplot: Count occurrences
subject_counts = df['Subject'].value_counts()
sns.countplot(data=df, x='Subject', ax=axes[0, 1])
axes[0, 1].set_title("Count Plot (How many in each subject)")

# stripplot: Individual points
sns.stripplot(data=df, x='Subject', y='Score',
              jitter=True, size=8, ax=axes[1, 0])
axes[1, 0].set_title("Strip Plot (Individual points with jitter)")

# boxplot with points
sns.boxplot(data=df, x='Subject', y='Score', ax=axes[1, 1])
sns.stripplot(data=df, x='Subject', y='Score',
              color='red', alpha=0.3, size=4, ax=axes[1, 1])
axes[1, 1].set_title("Box Plot + Individual Points")

plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_9_categorical.png')
plt.close()

print("✅ Created 4 categorical plots")
print("   - barplot: Average values per category")
print("   - countplot: Frequency per category")
print("   - stripplot: Individual points (jittered)")
print("   - boxplot + stripplot: Combined view")
print()


# ============================================================================
# EXAMPLE 5: CORRELATION HEATMAP
# ============================================================================

print("EXAMPLE 5: Correlation Heatmap (See relationships in 2D)")
print("-" * 70)

# Create data with numeric columns for correlation
numeric_data = {
    'Math': np.random.normal(75, 15, 100),
    'Science': np.random.normal(72, 16, 100),
    'English': np.random.normal(78, 14, 100),
    'History': np.random.normal(76, 15, 100),
    'Art': np.random.normal(80, 12, 100)
}

numeric_df = pd.DataFrame(numeric_data)

fig, ax = plt.subplots(figsize=(8, 6))

# Calculate correlation
correlation = numeric_df.corr()

# Create heatmap
sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, ax=ax, cbar_kws={'label': 'Correlation'})

ax.set_title("Correlation Heatmap (Subject Scores)", fontweight='bold')

plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_10_heatmap.png')
plt.close()

print("✅ Created correlation heatmap")
print("   - Shows correlation between all pairs of variables")
print("   - Red = positive correlation (move together)")
print("   - Blue = negative correlation (move opposite)")
print("   - Numbers show strength (-1.0 to +1.0)")
print()


# ============================================================================
# EXAMPLE 6: MULTI-VARIABLE VISUALIZATION
# ============================================================================

print("EXAMPLE 6: Multi-Variable Plot (4+ dimensions at once)")
print("-" * 70)

# Create richer dataset
np.random.seed(42)
multi_data = pd.DataFrame({
    'Age': np.random.randint(20, 60, 200),
    'Salary': np.random.randint(30000, 150000, 200),
    'Experience': np.random.randint(0, 40, 200),
    'Satisfaction': np.random.randint(1, 10, 200),
    'Department': np.random.choice(['HR', 'Tech', 'Sales', 'Finance'], 200)
})

fig, ax = plt.subplots(figsize=(12, 7))

# scatterplot with multiple dimensions:
# x = Age, y = Salary, size = Experience, hue = Satisfaction
sns.scatterplot(data=multi_data, x='Age', y='Salary',
                size='Experience', hue='Satisfaction',
                palette='viridis', sizes=(50, 300),
                ax=ax, alpha=0.6)

ax.set_title("Multi-Variable Scatter Plot\n(Age vs Salary, sized by Experience, colored by Satisfaction)",
             fontweight='bold')
ax.set_ylabel("Salary ($)", fontsize=11)
ax.set_xlabel("Age (years)", fontsize=11)

plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_11_multivariable.png')
plt.close()

print("✅ Created multi-variable scatter plot")
print("   - X axis: Age")
print("   - Y axis: Salary")
print("   - Size: Experience (bigger = more experience)")
print("   - Color: Satisfaction (darker = more satisfied)")
print("   - Shows 4 dimensions in one plot!")
print()


# ============================================================================
# EXAMPLE 7: FIGURE-LEVEL FUNCTIONS
# ============================================================================

print("EXAMPLE 7: Figure-Level Functions (Multiple subplots automatically)")
print("-" * 70)

# relplot creates a figure with subplots automatically
g = sns.relplot(data=df, x='Hours_Studied', y='Score',
                col='Subject', kind='scatter', height=4, aspect=1)

g.set_titles("{col_name}")

plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_12_relplot.png',
            bbox_inches='tight', dpi=100)
plt.close()

print("✅ Created relplot (automatically creates subplots)")
print("   - Splits plot by 'col' parameter (one per Subject)")
print("   - Returns Figure object 'g' for customization")
print()


# ============================================================================
# EXAMPLE 8: STYLING SEABORN
# ============================================================================

print("EXAMPLE 8: Seaborn Styles and Palettes")
print("-" * 70)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Different seaborn styles
styles = ['white', 'dark', 'whitegrid', 'darkgrid']

for idx, style in enumerate(styles):
    ax = axes[idx // 2, idx % 2]
    sns.set_style(style)

    sns.scatterplot(data=df, x='Hours_Studied', y='Score', ax=ax, s=100)
    ax.set_title(f"Style: {style}")

plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_13_styles.png')
plt.close()

# Reset style
sns.set_style("whitegrid")

print("✅ Created plots with different styles")
print("   - 'white': Clean white background")
print("   - 'dark': Dark background")
print("   - 'whitegrid': White with grid")
print("   - 'darkgrid': Dark with grid")
print()


# ============================================================================
# EXAMPLE 9: COLOR PALETTES
# ============================================================================

print("EXAMPLE 9: Seaborn Color Palettes")
print("-" * 70)

palettes = ['deep', 'muted', 'pastel', 'husl', 'Set2', 'dark']

fig, axes = plt.subplots(2, 3, figsize=(14, 8))

for idx, palette in enumerate(palettes):
    ax = axes[idx // 3, idx % 3]
    sns.set_palette(palette)

    sns.barplot(data=df, x='Subject', y='Score', ax=ax)
    ax.set_title(f"Palette: {palette}")

plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_14_palettes.png')
plt.close()

# Reset to default
sns.set_palette("husl")

print("✅ Created plots with different color palettes")
print("   Available palettes: deep, muted, pastel, bright, dark,")
print("                       colorblind, Set1, Set2, husl, etc.")
print()


# ============================================================================
# SUMMARY: SEABORN PLOT TYPES
# ============================================================================

print("=" * 70)
print("SEABORN PLOT TYPES SUMMARY")
print("=" * 70)
print()

print("DISTRIBUTION PLOTS (How data is spread)")
print("  - histplot()    : Histogram")
print("  - kdeplot()     : Smooth distribution curve")
print("  - boxplot()     : Box and whiskers")
print("  - violinplot()  : Full distribution shape")
print("  - stripplot()   : Individual points")
print()

print("RELATIONSHIP PLOTS (Between two variables)")
print("  - scatterplot() : Points")
print("  - regplot()     : Scatter + regression line")
print("  - lmplot()      : Figure-level regression (multiple subplots)")
print("  - lineplot()    : Line plots (for time series)")
print()

print("CATEGORICAL PLOTS (Compare across groups)")
print("  - barplot()     : Average per category")
print("  - countplot()   : Count per category")
print("  - boxplot()     : Distribution per category")
print("  - violinplot()  : Full distribution per category")
print("  - swarmplot()   : Individual points per category")
print()

print("MATRIX PLOTS (2D data visualization)")
print("  - heatmap()     : Color grid (correlations, etc.)")
print("  - clustermap()  : Heatmap with dendrograms")
print()

print("FIGURE-LEVEL FUNCTIONS (Creates full figure with subplots)")
print("  - relplot()     : Relationship plot (with col/row)")
print("  - displot()     : Distribution plot (with col/row)")
print("  - catplot()     : Categorical plot (with col/row)")
print("  - lmplot()      : Linear model plot")
print()


# ============================================================================
# KEY ADVANTAGES OF SEABORN
# ============================================================================

print("=" * 70)
print("WHY USE SEABORN?")
print("=" * 70)
print()

print("1. BEAUTIFUL BY DEFAULT")
print("   - Great colors and styles out of the box")
print("   - No tweaking needed for professional plots")
print()

print("2. PANDAS INTEGRATION")
print("   - Works directly with DataFrames")
print("   - Column names in the plot")
print("   - Automatic grouping by category")
print()

print("3. STATISTICAL ESTIMATION")
print("   - Confidence intervals built-in")
print("   - Trend lines with uncertainty")
print("   - Saves you from manual calculations")
print()

print("4. MULTIPLE PLOT TYPES")
print("   - Distribution, relationship, categorical, matrix")
print("   - Covers most data science needs")
print()

print("5. EASY CUSTOMIZATION")
print("   - Styles, palettes, sizes")
print("   - Works well with Matplotlib customization")
print()


# ============================================================================
# LESSON COMPLETE
# ============================================================================

print()
print("=" * 70)
print("LESSON 2 COMPLETE ✅")
print("=" * 70)
print()
print("What you learned:")
print("  ✅ Seaborn vs Matplotlib comparison")
print("  ✅ Distribution plots (histogram, KDE, box, violin)")
print("  ✅ Relationship plots (scatter, regression)")
print("  ✅ Categorical plots (bar, count, strip, box)")
print("  ✅ Correlation heatmaps")
print("  ✅ Multi-variable visualization")
print("  ✅ Figure-level functions")
print("  ✅ Styles and color palettes")
print()
print("All plots have been saved as PNG files in the same folder.")
print()
print("Next: Lesson 3 - Plotly for Interactive Visualization")
print()
print("🙏 Beautiful data tells the truth more powerfully than numbers alone. 🙏")
