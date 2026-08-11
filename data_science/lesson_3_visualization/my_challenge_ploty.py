

import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

# Create data
np.random.seed(42)
students = pd.DataFrame({
    'Student_ID':  np.repeat(range(1, 101), 5), # Each student appears 5 times (once per subj)
    'Subject': ['Math', 'Science', 'English', 'History', 'Art'] * 100,
    'Score': np.random.randint(0, 100, 500),
    'Hours_Studied': np.random.randint(0, 20, 500),
    'Attendance': np.random.randint(0, 100, 500)
})

print("Dataset created:")
print(students.head(10))
print(f"\nShape: {students.shape}")  # Should show (500, 5)
print()
# Verify data
print("Data Verification:")
print(f"✅ Total records: {len(students)}")
print(f"✅ Students: {students['Student_ID'].nunique()}")
print(f"✅ Subjects: {students['Subject'].nunique()}")
print()

# 2. Interactive Scatter Plot:
#    - X: Hours_Studied, Y: Score
#    - Color: Subject
#    - Size: Attendance
#    - Hover: Student name and all stats
#    - Title: "Study Hours vs Exam Scores (All Subjects)"

fig = px.scatter(students, x='Hours_Studied', y='Score',
                 color='Subject',
                 size='Attendance',
                 hover_name='Student_ID',
                 hover_data={
                     'Subject':True,
                     'Score': True,
                     'Hours_Studied':False,
                     'Attendance':False
                 },
                 title='Study Hours vs Exam Scores (All Subjects)')


fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/my_scatter_plot.html')

  # Average Score by Subject (bar chart)
fig = px.bar(students, x='Subject', y='Score',
             color='Subject',
             title='Average Score by Subject')

fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/my_bar_chart.html')
 


#   💡 When IS hover_data Useful?

#   Use Case 1: Hide Unnecessary Columns

#   # Default: Shows EVERYTHING
#   fig = px.scatter(df, x='Hours_Studied', y='Score',
#                    hover_name='Student_ID')
#   # Hover shows: Student_ID, Subject, Score, Hours_Studied, Attendance,
#   #              index, other_column1, other_column2...
#   # Too much! 🤯

#   # With hover_data: Show ONLY what matters
#   fig = px.scatter(df, x='Hours_Studied', y='Score',
#                    hover_name='Student_ID',
#                    hover_data=['Subject', 'Score'])  # Hide Attendance, others
#   # Hover shows: Student_ID, Subject, Score (clean!) ✅

#   Use Case 2: Format Columns Specially

#   # Show Attendance as percentage with format
#   fig = px.scatter(df, x='Hours_Studied', y='Score',
#                    hover_name='Student_ID',
#                    hover_data={'Attendance': ':.0f%'})
#   # Shows: "Attendance: 85%"  (formatted!)

#   Use Case 3: Rename for Clarity

#   fig = px.scatter(df, x='Hours_Studied', y='Score',
#                    hover_name='Student_ID',
#                    hover_data={'Hours_Studied': ':.1f hours',
#                               'Attendance': ':.0f%'})
#   # Shows nice formatted labels

# 3. Interactive Bar Chart:
#    - Average score by subject
#    - Color: Average hours studied
#    - Hover: Show attendance percentage
#    - Title: "Average Scores by Subject"
# fig = px.bar(students, x='Subject', y='Score', 
#              color='Hours_Studied', 
#              hover_data={'Attendance': ':.0f'},  # ✅ Shows as "85"
#              hover_template='<b>%{x}</b><br>Score: %{y:.0f}<br>Attendance: %{customdata}%<extra></extra>',
#              title='Average Scores by Subject')
# TypeError: bar() got an unexpected keyword argument 'hover_template'

students['Attendance'] = students['Attendance'].astype(str) + '%'

fig = px.bar(students, x='Subject', y='Score',
             color='Hours_Studied',
             hover_data={'Attendance': True},
             title='Average Scores by Subject')

 #  - Shows: "Attendance: 85%" ✅


fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/my_bar_chart_2.html')

# 4. Interactive Box Plot:
#    - Score distribution by subject
#    - Show outliers
#    - Title: "Score Distribution (by Subject)"

