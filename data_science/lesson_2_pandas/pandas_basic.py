

import pandas as pd
import numpy as np

  # Create a DataFrame (like an Excel sheet)
data = {
      'Name': ['Alice', 'Bob', 'Charlie'],
      'Age': [25, 30, 35],
      'Salary': [50000, 60000, 75000]
  }

df = pd.DataFrame(data)
print(f"{df}")
print(f"Data frame from pandas: {df}")

print("======= Challenge 1: Create DataFrame =======")
  # Create a DataFrame from dictionary
students = {
      'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
      'Math': [85, 90, 78, 92],
      'English': [88, 85, 90, 87],
      'Science': [92, 88, 85, 95]
  }

df = pd.DataFrame(students)
print(f"{df}  - Data Frame of students")
print(f"\nShape: {df.shape}") # 4 - rows , 4 - columns
print(f"Columns: {df.columns.to_list()}")

print("======= Challenge 2: Access Data =======")
# Get a single column
print("Math scores:")
print(df['Math'])

# Get a single row
print("\nAlice scores: ")
print(df.iloc[0]) # First row

# Get specific cell
print(f"\nBob´s Math score: {df.loc[1, 'Math']}")

print("======= Challenge 3: Statistics =======")
# Get statistics for each column
print("Mean scores: ")
print(df[['Math', 'English', 'Science']].mean())

print("Max scores: ")
print(df[['Math', 'English', 'Science']].max())

print("Min scores: ")
print(df[['Math', 'English', 'Science']].min())

print("======= Challenge 4: Create New Column =======")
# Calculate average score for each student
df['Average'] = df[['Math', 'English', 'Science']].mean(axis=1).round(4)
print("Students with their average: ")
print(df)


print("======= Challenge 5: Filter Data =======")
# Find students with Math score > 85
high_math = df[df['Math'] > 85]
print("Students with Math score > 85")
print(high_math)

# Find students with Average > 88
high_average = df[df['Average'] > 88]
print("Students with Average > 88")
print(high_average)

print("======= Challenge 6: Sort Data =======")
# Sort by Math score descending
sorted_by_math = df.sort_values('Math', ascending=False)
print("Sorted by Math score (highest first)")
print(sorted_by_math)

# Sort by Average ascending
sorted_by_avg = df.sort_values('Average')
print("Sorted by Average (lowest first)")
print(sorted_by_avg)


print("======= Challenge 7: Handle Missing Data =======")
# Create Data Frame with missing values
incomplete = pd.DataFrame({
      'Name': ['Alice', 'Bob', 'Charlie'],
      'Score': [85, np.nan, 90]  # np.nan = missing value
  })
print("Data with missing value: ")
print(incomplete)

  # Fill missing with mean
incomplete['Score'] = incomplete['Score'].fillna(incomplete['Score'].mean())
print("\nAfter filling missing values:")
print(incomplete)


print("\n======= Challenge 8: Group and Aggregate =======")
  # Create more realistic data
grades = pd.DataFrame({
      'Subject': ['Math', 'Math', 'English', 'English', 'Science', 'Science'],
      'Teacher': ['Smith', 'Jones', 'Smith', 'Jones', 'Smith', 'Jones'],
      'Grade': [85, 90, 88, 92, 80, 88]
  })
print("Grades data:")
print(grades)

  # Group by Subject and get mean
print("\nMean grade by Subject:")
print(grades.groupby('Subject')['Grade'].mean())

  # Group by Teacher and get max
print("\nMax grade by Teacher:")
print(grades.groupby('Teacher')['Grade'].max())

print("\n[Done] All Pandas challenges complete!")


  # Group by Teacher and get max
print("\nMax grade by Teacher:")
print(grades.groupby('Teacher')['Grade'].max())

print("\n[Done] All Pandas challenges complete!")








