# ============================================================================
# PHASE 2.2 — LESSON 3: PLOTLY FOR INTERACTIVE VISUALIZATION
# ============================================================================
#
# "Plotly brings your data to life with interactivity."
#
# Static plots show ONE view. Interactive plots let the viewer explore.
# Hover, zoom, pan, select — the viewer becomes an explorer.
#
# ============================================================================

import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

print("=" * 70)
print("PLOTLY FUNDAMENTALS - LESSON 3")
print("=" * 70)
print()

# ============================================================================
# PART 1: PLOTLY vs MATPLOTLIB vs SEABORN
# ============================================================================
print("PLOTLY:")
print("  - INTERACTIVE, web-based (HTML)")
print("  - Hover, zoom, pan, select")
print("  - Good for dashboards, web apps")
print("  - Can be saved as standalone HTML")
print()
# ============================================================================
# PART 2: PLOTLY EXPRESS (High-level, quick plots)
# ============================================================================
print("=" * 70)
print("EXAMPLE 1: Scatter Plot with Hover Information")
print("-" * 70)

# Create data
np.random.seed(42)
data_student = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank',
                'Grace', 'Henry', 'Iris', 'Jack'] * 5,
    'Subject': ['Math', 'Science', 'English', 'History', 'Art'] * 10,
    'Score': np.random.randint(60, 100, 50),
    'Hours_Studied': np.random.randint(1, 10, 50),
    'Attendance': np.random.randint(70, 100, 50)
})

fig = px.scatter(data_student, x='Hours_Studied', y='Score',
                 color='Subject', # Different color per subject
                 size='Attendance', # Size by attendance
                 hover_name='Student', # Show name on hover 
                 title='Interactive: Study Hours vs Exam Scores',
                 labels={'Hours_Studied':'Hours Studied', 'Score': 'Exam Score'})


fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/my_interactive_scatter_1.html')


# ============================================================================
# EXAMPLE 2: Interactive Bar Chart
# ============================================================================

print("EXAMPLE 2: Interactive Bar Chart")
print("-" * 70)

# Aggregate data by subject
subject_summary = data_student.groupby('Subject').agg({
    'Score': 'mean',
    'Hours_Studied': 'mean',
    'Attendance': 'mean'
}).reset_index()

# Create bar chart with hover
fig = px.bar(subject_summary, x='Subject', y='Score',
             color='Hours_Studied', # Color by hours studied
             hover_data={'Attendance':':.1f'}, # Show attendance on hover
             title='Average Scores by Subject',
             labels={'Score': 'Average Score', 'Hours_Studied': 'Avg Hours'})

fig.update_layout(hovermode='x') # Show all hoverable data

fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/my_interactive_scatter_2.html')

# ============================================================================
# EXAMPLE 3: LINE PLOT WITH MULTIPLE TRACES
# ============================================================================

print("EXAMPLE 3: Interactive Line Plot (Time Series)")
print("-" * 70)

# Create time series data
days = np.arange(1, 31)
fig = px.line(pd.DataFrame({
    'Day': list(days) * 3,
    'Temperature': list(20 + 5 * np.sin(days / 5) + np.random.randn(30) * 0.5) + 
                   list(25 + 3 * np.cos(days / 4) + np.random.randn(30) * 0.5) + 
                   list(18 + 4 * np.cos(days / 6) + np.random.randn(30) * 0.5),
    'Location': ['Room A'] * 30 + ['Room B'] * 30 + ['Room C'] * 30
}), x='Day', y='Temperature', color='Location',
              title='Temperature Over Time (3 Rooms)',
              hover_data={'Temperature': ':.1f'})

fig.update_traces(mode='lines+markers')

fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/my_interactive_scatter_3.html')


