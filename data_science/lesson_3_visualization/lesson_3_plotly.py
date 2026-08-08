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

print("PLOTLY vs MATPLOTLIB vs SEABORN")
print("-" * 70)
print()

print("MATPLOTLIB:")
print("  - Static, saved as images")
print("  - Fine control, low-level")
print("  - Good for papers, reports")
print()

print("SEABORN:")
print("  - Static, built on Matplotlib")
print("  - Beautiful by default")
print("  - Good for data exploration")
print()

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
data = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank',
                'Grace', 'Henry', 'Iris', 'Jack'] * 5,
    'Subject': ['Math', 'Science', 'English', 'History', 'Art'] * 10,
    'Score': np.random.randint(60, 100, 50),
    'Hours_Studied': np.random.randint(1, 10, 50),
    'Attendance': np.random.randint(70, 100, 50)
})

# Create interactive scatter plot
fig = px.scatter(data, x='Hours_Studied', y='Score',
                 color='Subject',  # Different color per subject
                 size='Attendance',  # Size by attendance
                 hover_name='Student',  # Show name on hover
                 hover_data={'Attendance': True},  # Show attendance on hover
                 title='Interactive: Study Hours vs Exam Scores',
                 labels={'Hours_Studied': 'Hours Studied', 'Score': 'Exam Score'})

fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_15_interactive_scatter.html')

print("✅ Created interactive scatter plot")
print("   - Hover over points to see Student name and Attendance")
print("   - Zoom, pan, select with toolbar")
print("   - Colors represent Subject")
print("   - Size represents Attendance")
print("   - Saved as HTML file (open in browser!)")
print()


# ============================================================================
# EXAMPLE 2: Interactive Bar Chart
# ============================================================================

print("EXAMPLE 2: Interactive Bar Chart")
print("-" * 70)

# Aggregate data by subject
subject_summary = data.groupby('Subject').agg({
    'Score': 'mean',
    'Hours_Studied': 'mean',
    'Attendance': 'mean'
}).reset_index()

# Create bar chart with hover
fig = px.bar(subject_summary, x='Subject', y='Score',
             color='Hours_Studied',  # Color by hours studied
             hover_data={'Attendance': ':.1f'},  # Show attendance on hover
             title='Average Scores by Subject',
             labels={'Score': 'Average Score', 'Hours_Studied': 'Avg Hours'})

fig.update_layout(hovermode='x')  # Show all hoverable data

fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_16_interactive_bar.html')

print("✅ Created interactive bar chart")
print("   - Hover to see detailed statistics")
print("   - Click legend to show/hide subjects")
print("   - Drag to zoom, double-click to reset")
print()


# ============================================================================
# EXAMPLE 3: LINE PLOT WITH MULTIPLE TRACES
# ============================================================================

print("EXAMPLE 3: Interactive Line Plot (Time Series)")
print("-" * 70)

# Create time series data
days = np.arange(1, 31)
fig = px.line(pd.DataFrame({
    'Day': list(days) * 3,
    'Temperature': list(20 + 5*np.sin(days/5) + np.random.randn(30)*0.5) +
                   list(25 + 3*np.cos(days/4) + np.random.randn(30)*0.5) +
                   list(18 + 4*np.sin(days/6) + np.random.randn(30)*0.5),
    'Location': ['Room A']*30 + ['Room B']*30 + ['Room C']*30
}), x='Day', y='Temperature', color='Location',
             title='Temperature Over Time (3 Rooms)',
             hover_data={'Temperature': ':.1f'})

fig.update_traces(mode='lines+markers')

fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_17_interactive_line.html')

print("✅ Created interactive line plot")
print("   - Hover for exact values")
print("   - Click legend items to toggle visibility")
print("   - Multiple lines with different colors")
print("   - Markers on each data point")
print()


# ============================================================================
# EXAMPLE 4: BOX PLOT (Distribution Comparison)
# ============================================================================

print("EXAMPLE 4: Interactive Box Plot")
print("-" * 70)

fig = px.box(data, x='Subject', y='Score',
             points='outliers',  # Show outlier points
             title='Score Distribution by Subject',
             labels={'Score': 'Exam Score'})

fig.update_traces(boxmean='sd')  # Add mean and std dev

fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_18_interactive_box.html')

print("✅ Created interactive box plot")
print("   - Shows quartiles, median, whiskers")
print("   - Outliers highlighted as points")
print("   - Hover for exact values")
print()


# ============================================================================
# EXAMPLE 5: HEATMAP
# ============================================================================

print("EXAMPLE 5: Interactive Heatmap (Correlation)")
print("-" * 70)

# Create correlation matrix
numeric_cols = ['Score', 'Hours_Studied', 'Attendance']
correlation = data[numeric_cols].corr()

fig = px.imshow(correlation,
                labels=dict(color='Correlation'),
                title='Correlation Matrix (Heatmap)',
                color_continuous_scale='RdBu_r',  # Red-Blue reversed
                text_auto='.2f')  # Show correlation values

fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_19_interactive_heatmap.html')

print("✅ Created interactive heatmap")
print("   - Hover to see exact correlation values")
print("   - Colors show correlation strength")
print("   - Red = positive, Blue = negative")
print()


# ============================================================================
# EXAMPLE 6: SCATTER 3D
# ============================================================================

print("EXAMPLE 6: 3D Scatter Plot")
print("-" * 70)

fig = px.scatter_3d(data, x='Hours_Studied', y='Score', z='Attendance',
                    color='Subject',
                    hover_name='Student',
                    title='3D: Study Hours vs Score vs Attendance',
                    labels={'Hours_Studied': 'Hours',
                           'Score': 'Score',
                           'Attendance': 'Attendance %'})

fig.update_traces(marker=dict(size=5))

fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_20_interactive_3d.html')

print("✅ Created 3D scatter plot")
print("   - Rotate to view from different angles")
print("   - Zoom with scroll")
print("   - Shows 3 variables in 3D space")
print()


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
    specs=[[{}, {}],
           [{}, {}]]
)

# Add line plot (row 1, col 1)
fig.add_trace(
    go.Scatter(x=np.arange(1, 11), y=np.random.randn(10).cumsum(),
               mode='lines+markers', name='Trend'),
    row=1, col=1
)

# Add scatter (row 1, col 2)
fig.add_trace(
    go.Scatter(x=np.random.randn(50), y=np.random.randn(50),
               mode='markers', name='Points'),
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

fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_21_interactive_subplots.html')

print("✅ Created subplot figure")
print("   - 2x2 grid of different plot types")
print("   - Each plot is interactive")
print("   - Can customize each plot independently")
print()


# ============================================================================
# EXAMPLE 8: PLOTLY GRAPH_OBJECTS (Lower-level, more control)
# ============================================================================

print("EXAMPLE 8: Using Graph Objects (Advanced)")
print("-" * 70)

# Create figure
fig = go.Figure()

# Add traces (plots)
for subject in data['Subject'].unique():
    subset = data[data['Subject'] == subject]
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

fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_22_graph_objects.html')

print("✅ Created plot with Graph Objects")
print("   - More control than Express")
print("   - Manually add traces (plots)")
print("   - Customize every detail")
print()


# ============================================================================
# EXAMPLE 9: ANIMATION (Time-based changes)
# ============================================================================

print("EXAMPLE 9: Animated Plot (Changes over time)")
print("-" * 70)

# Create data that changes over time
frames_data = []
for frame in range(5):
    frames_data.extend({
        'x': np.random.randn(20),
        'y': np.random.randn(20) + frame * 0.5,
        'Frame': f'Frame {frame + 1}'
    } for _ in range(1))

# For simplicity, create static representation of animation concept
fig = px.scatter(data.head(20), x='Hours_Studied', y='Score',
                color='Subject',
                animation_frame=None,  # Would need time column for real animation
                title='Example: Animated Plot Concept')

fig.write_html('/Users/andhar/desktop/my_garden_of_python/data_science/lesson_3_visualization/plot_23_animation.html')

print("✅ Created static plot (animation explained)")
print("   - Plotly can animate plots based on time columns")
print("   - Perfect for showing how data changes")
print("   - Use animation_frame parameter in px functions")
print()


# ============================================================================
# SUMMARY: PLOTLY PLOT TYPES
# ============================================================================

print("=" * 70)
print("PLOTLY PLOT TYPES SUMMARY")
print("=" * 70)
print()

print("BASIC PLOTS:")
print("  px.scatter()     : Scatter plot")
print("  px.line()        : Line plot")
print("  px.bar()         : Bar chart")
print("  px.box()         : Box plot")
print("  px.histogram()   : Histogram")
print()

print("STATISTICAL PLOTS:")
print("  px.violin()      : Violin plot")
print("  px.strip()       : Strip plot")
print("  px.density_contour() : Density contours")
print()

print("MATRIX PLOTS:")
print("  px.imshow()      : Heatmap (images, correlation)")
print("  px.choropleth()  : Geographic maps")
print()

print("3D PLOTS:")
print("  px.scatter_3d()  : 3D scatter")
print("  px.surface()     : 3D surface")
print("  px.mesh_3d()     : 3D mesh")
print()

print("ADVANCED:")
print("  go.Figure()      : Graph Objects (manual control)")
print("  make_subplots()  : Create subplot grids")
print()


# ============================================================================
# KEY ADVANTAGES OF PLOTLY
# ============================================================================

print("=" * 70)
print("WHY USE PLOTLY?")
print("=" * 70)
print()

print("1. INTERACTIVITY")
print("   - Hover for details")
print("   - Zoom, pan, select")
print("   - Click legend to toggle")
print()

print("2. WEB-READY")
print("   - Saves as standalone HTML")
print("   - Works in Jupyter notebooks")
print("   - Can embed in web pages")
print()

print("3. BEAUTIFUL DEFAULT")
print("   - Professional look without tweaking")
print("   - Smooth animations and transitions")
print()

print("4. MULTIPLE PLOT TYPES")
print("   - Covers most visualization needs")
print("   - 2D, 3D, geographic, and more")
print()

print("5. PANDAS INTEGRATION")
print("   - Works directly with DataFrames")
print("   - Easy grouping and coloring")
print()

print("6. ANIMATION SUPPORT")
print("   - Show how data changes over time")
print("   - Perfect for storytelling")
print()


# ============================================================================
# WHEN TO USE EACH LIBRARY
# ============================================================================

print("=" * 70)
print("WHEN TO USE EACH VISUALIZATION LIBRARY")
print("=" * 70)
print()

print("USE MATPLOTLIB WHEN:")
print("  - You need fine control")
print("  - Creating plots for papers")
print("  - Working with very large datasets")
print()

print("USE SEABORN WHEN:")
print("  - You want beautiful statistical plots")
print("  - Exploring data (static)")
print("  - Need correlation matrices, distributions")
print()

print("USE PLOTLY WHEN:")
print("  - You want interactivity")
print("  - Creating dashboards")
print("  - Building web applications")
print("  - Need 3D visualizations")
print("  - Presenting to stakeholders")
print()


# ============================================================================
# LESSON COMPLETE
# ============================================================================

print()
print("=" * 70)
print("LESSON 3 COMPLETE ✅")
print("=" * 70)
print()
print("What you learned:")
print("  ✅ Plotly Express (high-level API)")
print("  ✅ Interactive scatter plots")
print("  ✅ Interactive bar charts")
print("  ✅ Interactive line plots")
print("  ✅ Box plots and heatmaps")
print("  ✅ 3D scatter plots")
print("  ✅ Subplots with multiple plot types")
print("  ✅ Graph Objects (low-level control)")
print("  ✅ Animation concepts")
print()
print("All plots have been saved as HTML files.")
print("Open them in your web browser to interact with them!")
print()
print("=" * 70)
print("PHASE 2.2 - DATA VISUALIZATION COMPLETE! 🎨✨")
print("=" * 70)
print()
print("You have mastered:")
print("  ✅ Matplotlib (the foundation)")
print("  ✅ Seaborn (beautiful statistical plots)")
print("  ✅ Plotly (interactive web visualizations)")
print()
print("Next: Challenges to prove your mastery!")
print()
print("🙏 Data visualization is the bridge between numbers and truth. 🙏")
