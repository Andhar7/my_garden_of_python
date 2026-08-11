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

# ============================================================================
# EXAMPLE 4: BOX PLOT (Distribution Comparison)
# ============================================================================

print("EXAMPLE 4: Interactive Box Plot")
print("-" * 70)

fig = px.box(data_student, x='Subject', y='Score',
             points='outliers', # Show outlier points
             title='Score Distribution by Subject',
             labels={'Score':'Exam Score'}) 

fig.update_traces(boxmean='sd') # Ad mean and std dev

fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/my_interactive_scatter_4.html')


# ============================================================================
# EXAMPLE 5: HEATMAP
# ============================================================================

print("EXAMPLE 5: Interactive Heatmap (Correlation)")
print("-" * 70)

# Create correlation matrix
numeric_cols = ['Score', 'Hours_Studied', 'Attendance']
correlation = data_student[numeric_cols].corr()

fig = px.imshow(correlation,
                labels=dict(color='Correlation'),
                title='Correlation Matrix (Heatmap)',
                color_continuous_scale='RdBu_r', # Red - Blue reversed
                text_auto='.2f') # Show correlation values


fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/my_interactive_scatter_5.html')


# ============================================================================
# EXAMPLE 6: SCATTER 3D
# ============================================================================

print("EXAMPLE 6: 3D Scatter Plot")
print("-" * 70)

fig = px.scatter_3d(data_student, x='Hours_Studied', y='Score', z='Attendance',
                    color='Subject', 
                    hover_name='Student', 
                    title='3D: Study Hours vs Score vs Attendance',
                    labels={'Hours_Studied': 'Hours',
                           'Score': 'Score',
                           'Attendance': 'Attendance %'})

fig.update_traces(marker=dict(size=5))

fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/my_interactive_scatter_6.html')

# ============================================================================
# EXAMPLE 7: SUBPLOTS (Multiple plots in one)
# ============================================================================

print("EXAMPLE 7: Subplots with Plotly")
print("-" * 70)

from plotly.subplots import make_subplots

# Create subplot figure (2x2)
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Line Plot', 'Scatter', 'Bar Chart', 'Box Plot'),
    specs=[
        [{}, {}],
        [{}, {}]
    ]
)

# Add line plot (row 1, col 1)
fig.add_trace(
    go.Scatter(x=np.arange(1,11), y=np.random.randn(10).cumsum(),
               mode='lines+markers', name='Trend'),
    row=1, col=1
)

# Add scatter (row 1, col 2)
fig.add_trace(
    go.Scatter(x=np.random.randn(50), y=np.random.randn(50), mode='markers', name='Points'),
    row=1, col=2
)

# Add bar chart (row 2, col 1)
fig.add_trace(
    go.Bar(x=['A', 'B', 'C'], y=[10, 15, 13], name='Data'),
    row=2, col=1
)

# Add box plot (row 2, col 2)
fig.add_trace(
    go.Box(y=np.random.randn(100), name='Distribution'),
    row=2, col=2
)

fig.update_layout(height=700, title_text="Multiple Plot Types (Subplots)")
fig.update_xaxes(title_text='X Axis', row=1, col=1)
fig.update_yaxes(title_text='Y Axis', row=1, col=1)


fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/my_interactive_scatter_7.html')


# ============================================================================
# EXAMPLE 8: PLOTLY GRAPH_OBJECTS (Lower-level, more control)
# ============================================================================

print("EXAMPLE 8: Using Graph Objects (Advanced)")
print("-" * 70)

# Create figure
fig = go.Figure()

# Add traces (plots)
for subject in data_student['Subject'].unique():
    subset = data_student[data_student['Subject'] == subject]
    fig.add_trace(go.Scatter(
        x=subset['Hours_Studied'],
        y=subset['Score'],
        mode='markers',
        name=subject,
        marker=dict(size=10)
    ))

# Update layout
fig.update_layout(
    title='Study Hours vs Scores (by Subject)',
    xaxis_title='Hours Studied',
    yaxis_title='Exam Score',
    hovermode='closest',
    height=500
)


fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/my_interactive_scatter_8.html')

# ============================================================================
# EXAMPLE 9: ANIMATION (Time-based changes)
# ============================================================================

print("EXAMPLE 9: Animated Plot (Changes over time)")
print("-" * 70)

# # Create data that changes over time
frames_data = []
for frame in range(5):
    frames_data.extend({
        'x': np.random.randn(20),
        'y': np.random.randn(20) + frame * 0.5,
        'Frame': f'Frame {frame + 1}'
    } for _ in range(1))

# For simplicity, create static representation of animation concept
fig = px.scatter(data_student.head(20), x='Hours_Studied', y='Score',
                color='Subject',
                animation_frame=None,  # Would need time column for real animation
                title='Example: Animated Plot Concept')



fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/my_interactive_scatter_9.html')