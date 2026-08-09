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
sns.set_style("ticks")
sns.set_palette("husl")

# plt.tight_layout()
# plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_sea_example.png')
# plt.close()

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

print("Dataset created: ")
print(df.head(10))
print()

# ============================================================================
# EXAMPLE 2: Distribution Plots
# ============================================================================

print("EXAMPLE 2: Distribution Plots (How data is spread)")
print("-" * 70)

fig, axes = plt.subplots(2,2, figsize=(12,10))

# histplot: Distribution with histogram
sns.histplot(data=df, x='Score', kde=True, ax=axes[0,0])
axes[0,0].set_title("Histogram with KDE (Kernel Density Estimate)")

# kdeplot: Smooth distribution curve
sns.kdeplot(data=df, x='Score', ax=axes[0,1], fill=True)
axes[0,1].set_title("KDE Plot (Smooth Distribution)")

# boxplot: Distribution and outliers
sns.boxplot(data=df, x='Subject', y='Score', ax=axes[1,0])
axes[1,0].set_title("Box Plot (Shows outliers and spread)")

# violinplot: Distribution shape
sns.violinplot(data=df, x='Subject', y='Score', ax=axes[1,1])
axes[1,1].set_title("Violin Plot (Distribution shape)")

plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_sea_example.png')
plt.close()

# ============================================================================
# EXAMPLE 3: Relationship Plots
# ============================================================================

print("EXAMPLE 3: Relationship Plots (Between two variables)")
print("-" * 70)

fig, axes = plt.subplots(2,2, figsize=(12,10))

# scatterplot: Points colored by category
sns.scatterplot(data=df, x='Hours_Studied', y='Score',
                hue='Subject', s=100, ax=axes[0,0]
                )
axes[0,0].set_title("Scatter Plot (colored by Subject)")

# regplot: Scatter with regression line
sns.regplot(data=df, x='Hours_Studied', y='Score', ax=axes[0,1])
axes[0,1].set_title("Regression Plot (with trend line)")

# lmplot-style comparison (multiple regression lines)
# We'll use multiple regplot calls
for subject in df['Subject'].unique():
    subset = df[df['Subject'] == subject]
    sns.regplot(data=subset, x='Hours_Studied', y='Score',
                ax=axes[1,0], label=subject, scatter=True
                )

axes[1,0].set_title("Multiple Regression Lines (by Subject)")
axes[1,0].legend()

# swarmplot: Shows individual points clearly
sns.swarmplot(data=df, x='Subject', y='Score', ax=axes[1,1])
axes[1,1].set_title("Swarm Plot (All individual points)")


plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_sea_2_ex.png')
plt.close()


# ============================================================================
# EXAMPLE 4: Categorical Plots
# ============================================================================

print("EXAMPLE 4: Categorical Plots (Compare across groups)")
print("-" * 70)

fig, axes = plt.subplots(2,2, figsize=(12,10))

# barplot: Average per category
sns.barplot(data=df, x='Subject', y='Score', ax=axes[0,0])
axes[0,0].set_title("Bar Plot (Average Score by Subject)")

# countplot: Count occurrences
subject_counts = df['Subject'].value_counts()
sns.countplot(data=df, x='Subject', ax=axes[0,1])
axes[0,1].set_title("Count Plot (How many in each subject)")

# stripplot: Individual point
sns.stripplot(data=df, x='Subject', y='Score', jitter=True, size=8, ax=axes[1,0])
axes[0,1].set_title("Strip Plot (Individual points with jitter)")

# boxplot with points
sns.boxplot(data=df, x='Subject', y='Score', ax=axes[1,1])
sns.stripplot(data=df, x='Subject', y='Score', color='red', alpha=0.3, size=4, ax=axes[1,1])
axes[1,1].set_title("Box Plot + Individual Points")

plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_sea_3_ex.png')
plt.close()


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
# print(numeric_data)
fig, ax = plt.subplots(figsize=(8,6))

# Calculate correlation
correlation = numeric_df.corr()

# Create heatmap
sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', center=0, ax=ax, cbar_kws={'label': 'Correlation'})
ax.set_title("Correlation Heatmap (Subject Scores)", fontweight='bold')

plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_sea_4_ex.png')
plt.close()

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

fig, ax = plt.subplots(figsize=(12,7))

# scatterplot with multiple dimensions:
# x = Age, y = Salary, size = Experience, hue = Satisfaction
sns.scatterplot(data=multi_data, x='Age', y='Salary', size='Experience', hue='Satisfaction', 
                palette='viridis', sizes=(50,300), ax=ax, alpha=0.6)

ax.set_title("Multi-Variable Scatter Plot\n(Age vs Salary, sized by Experience, colored by Satisfaction)",
             fontweight='bold')
ax.set_xlabel("Age (years)", fontsize=12)
ax.set_ylabel("Salary ($)", fontsize=12)

plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_sea_5_ex.png')
plt.close()

# ============================================================================
# EXAMPLE 7: FIGURE-LEVEL FUNCTIONS
# ============================================================================

print("EXAMPLE 7: Figure-Level Functions (Multiple subplots automatically)")
print("-" * 70)

# relplot creates a figure with subplots automatically
g = sns.relplot(data=df, x='Hours_Studied', y='Score',
                col='Subject', kind='scatter', height=4, aspect=1)

g.set_titles("{col_name}")
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_sea_6_ex.png',
            bbox_inches='tight', dpi=100)
plt.close()

# ============================================================================
# EXAMPLE 8: STYLING SEABORN
# ============================================================================

print("EXAMPLE 8: Seaborn Styles and Palettes")
print("-" * 70)

fig, axes = plt.subplots(2,2, figsize=(12,10))

# Different seaborn styles
styles = ['white', 'dark', 'whitegrid', 'darkgrid']

for idx, style in enumerate(styles):
    ax = axes[idx // 2, idx % 2]
    sns.set_style(style)
    
    sns.scatterplot(data=df, x='Hours_Studied', y='Score', ax=ax, s=100)
    ax.set_title(f"Style: {style}")


plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_sea_7_ex.png')
plt.close()

# ============================================================================
# EXAMPLE 9: COLOR PALETTES
# ============================================================================

print("EXAMPLE 9: Seaborn Color Palettes")
print("-" * 70)

palettes = ['deep', 'muted', 'pastel', 'husl', 'Set2', 'dark']

fig, axes = plt.subplots(2,3, figsize=(14, 8))

for idx, palette in enumerate(palettes):
    ax = axes[idx // 3, idx % 3]
    sns.set_palette(palette)
    
    sns.barplot(data=df, x='Subject', y='Score', ax=ax)
    ax.set_title(f"Pallete: {palette}")


plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_sea_8_ex.png')
plt.close()

# Reset to default
sns.set_palette("husl")