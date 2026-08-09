


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

