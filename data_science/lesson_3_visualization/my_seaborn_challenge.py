


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

np.random.seed(42)

print("-" * 70)
print("CHALLENGE 2: Seaborn Analysis")
print("-" * 70)

employee_data = pd.DataFrame({
      'Employee_ID': range(1, 201),
      'Department': np.random.choice(['Sales', 'Marketing', 'Engineering', 'HR'], 200),
      'Salary': np.random.randint(30000, 150000, 200),
      'Performance_Score': np.random.randint(50, 100, 200),
      'Years_Experience': np.random.randint(0, 30, 200),
      'Satisfaction': np.random.randint(1, 11, 200),
  })

print("Dataset created:")
print(employee_data.head())
print(f"Shape: {employee_data.shape}")
print()

# ============================================================================
# GROUP 1: DISTRIBUTION PLOTS
# ============================================================================
print("Creating Distribution Plots...")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# ---- PLOT 1: Salary Distribution (Histogram + KDE) ----
sns.histplot(data=employee_data, x='Salary', kde=True, ax=axes[0])
axes[0].set_title("Distribution of Employee Salaries", fontsize=14, fontweight='bold')
axes[0].set_xlabel("Salary ($)", fontsize=12)
axes[0].set_ylabel("Frequency", fontsize=12)

print("✅ Plot 1: Salary distribution histogram with KDE")

# ---- PLOT 2: Performance Score by Department (Box Plot) ----
sns.boxplot(data=employee_data, x='Department', y='Performance_Score', ax=axes[1])
axes[1].set_title("Performance Scores by Department", fontsize=14, fontweight='bold')
axes[1].set_xlabel("Department", fontsize=12)
axes[1].set_ylabel("Performance Score", fontsize=12)

print("✅ Plot 2: Performance scores by department (box plot)")


plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/challenge_2_distributions.png',
              dpi=300, bbox_inches='tight')
plt.close()

print()
print("=" * 70)
print("GROUP 1 COMPLETE!")
print("=" * 70)

# 2. Create relationship plots:
#    - Years Experience vs Performance Score (with regression)
#    - Years Experience vs Salary (with regression)
  # ============================================================================
  # GROUP 2: RELATIONSHIP PLOTS
  # ============================================================================
print("Creating Relationship Plots...")

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# ---- PLOT 1: Years Experience vs Performance Score (colored by Department) ----
for department in employee_data['Department'].unique():
      subset = employee_data[employee_data['Department'] == department]
      axes[0].scatter(subset['Years_Experience'], subset['Performance_Score'],
                     label=department, alpha=0.6, s=60)

# Add regression line (overall trend)
z = np.polyfit(employee_data['Years_Experience'], employee_data['Performance_Score'], 1)
p = np.poly1d(z)
x_line = np.array([employee_data['Years_Experience'].min(), employee_data['Years_Experience'].max()])
axes[0].plot(x_line, p(x_line), "r--", linewidth=2.5, label="Trend line")

axes[0].set_title("Years Experience vs Performance Score", fontsize=14, fontweight='bold')
axes[0].set_xlabel("Years Experience", fontsize=12)
axes[0].set_ylabel("Performance Score", fontsize=12)
axes[0].legend()
axes[0].grid(True, alpha=0.3)

print("✅ Plot 1: Experience vs Performance (with department colors)")

# ---- PLOT 2: Years Experience vs Salary (colored by Department) ----
for department in employee_data['Department'].unique():
      subset = employee_data[employee_data['Department'] == department]
      axes[1].scatter(subset['Years_Experience'], subset['Salary'],
                     label=department, alpha=0.6, s=60)

# Add regression line (overall trend)
z = np.polyfit(employee_data['Years_Experience'], employee_data['Salary'], 1)
p = np.poly1d(z)
x_line = np.array([employee_data['Years_Experience'].min(), employee_data['Years_Experience'].max()])
axes[1].plot(x_line, p(x_line), "r--", linewidth=2.5, label="Trend line")
axes[1].set_title("Years Experience vs Salary", fontsize=14, fontweight='bold')  # ✅ FIXED!
axes[1].set_xlabel("Years Experience", fontsize=12)
axes[1].set_ylabel("Salary ($)", fontsize=12)
axes[1].legend()
axes[1].grid(True, alpha=0.3)
print("✅ Plot 2: Experience vs Salary (with department colors)")
plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/challenge_2_relationship.png',
            dpi=300, bbox_inches='tight')
plt.close()
print()
print("=" * 70)
print("GROUP 2 COMPLETE!")
print("=" * 70)

# 3. Create categorical plots:
#    - Average salary by department (bar plot)
#    - Employee satisfaction by department (violin plot)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

#    - Average salary by department (bar plot)
sns.barplot(data=employee_data, x='Department', y='Salary', ax=axes[0])
axes[0].set_title("Average Salary by Department", fontsize=14, fontweight='bold')
axes[0].set_xlabel("Department", fontsize=12)
axes[0].set_ylabel("Salary ($)", fontsize=12)

#    - Employee satisfaction by department (violin plot)
sns.violinplot(data=employee_data, x='Department', y='Satisfaction', ax=axes[1])
axes[1].set_title("Employee satisfaction by department", fontsize=14, fontweight='bold')
axes[1].set_xlabel("Department", fontsize=12)
axes[1].set_ylabel("Satisfaction", fontsize=12)

plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/challenge_2_categorical.png',
            dpi=300, bbox_inches='tight')
plt.close()

# 4. Create correlation matrix:
#    - Heatmap showing correlations between: Salary, Performance_Score, Years_Experience, Satisfaction
#    - Add annotations showing correlation values
  # ============================================================================
  # GROUP 4: CORRELATION MATRIX
  # ============================================================================
print("=" * 70)
print("GROUP 4: CORRELATION MATRIX")
print("=" * 70)

# numeric_data = pd.DataFrame(employee_data)
numeric_data = employee_data[['Salary', 'Performance_Score', 'Years_Experience', 'Satisfaction']]


fig, ax = plt.subplots(figsize=(8,6))

# Calculate correlation
correlation = numeric_data.corr()

# Create heatmap
sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, ax=ax, cbar_kws={'label':'Correlation'})

ax.set_title("Correlation matrix between data", fontweight='bold')


plt.tight_layout()
plt.savefig('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/challenge_2_correlation.png',
            dpi=300, bbox_inches='tight')
plt.close()


  # For Challenge 2:

  # 1. Add Data Validation Section:
print("=" * 70)
print("DATA QUALITY VALIDATION")
print("=" * 70)

  # Check for missing values
print("Missing values:")
print(employee_data.isnull().sum())

  # Check value ranges
print("\nSalary range:", employee_data['Salary'].min(),
      "-", employee_data['Salary'].max())
print("Performance range:", employee_data['Performance_Score'].min(),
      "-", employee_data['Performance_Score'].max())
# Data quality assessment
print("\nData Quality Assessment:")
print("✅ Complete? Yes (no missing values)")
print("✅ Range realistic? Yes (salary 30k-150k is realistic)")
print("⚠️ Source: SIMULATED DATA (randomly generated)")
print("⚠️ Limitation: Random data shows NO real patterns")

  # 2. Add Note to Conclusions:
  # IMPORTANT NOTE:
  # This analysis uses SIMULATED (randomly generated) data.
  # Real employee data would likely show stronger correlations:
  # - Experience ↔ Salary: ~0.70 (strong)
  # - Performance ↔ Salary: ~0.40 (moderate)
  # - Salary ↔ Satisfaction: ~0.25 (weak but exists)

  # The lack of correlations in this dataset reflects the fact
  # that the data was randomly generated with NO real relationships.

  # In production ML: Always validate data quality BEFORE analysis!

