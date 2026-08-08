# 🎯 PHASE 2.2 - DATA VISUALIZATION CHALLENGES

**Student:** Gurudev  
**Completed Lessons:** Matplotlib, Seaborn, Plotly  
**Date Started:** August 8, 2026

---

## Challenge 1: Matplotlib Fundamentals (EASY)

**Objective:** Create a comprehensive multi-plot visualization using Matplotlib that tells a story about data.

**Requirements:**
1. Create a 2x2 subplot grid
2. Plot 1 (top-left): Line plot showing a trend over time
   - Create 30 days of data
   - Title: "Daily Website Traffic"
   - Show traffic increasing with some noise
   
3. Plot 2 (top-right): Scatter plot with trend line
   - Relationship between Marketing Spend (x) and Revenue (y)
   - Add a regression line
   - Title: "Marketing Spend vs Revenue"
   
4. Plot 3 (bottom-left): Histogram showing distribution
   - Customer purchase amounts (1000 samples from normal distribution)
   - Mean=100, StdDev=30
   - Add mean line (red dashed)
   - Title: "Distribution of Purchase Amounts"
   
5. Plot 4 (bottom-right): Bar chart with multiple categories
   - 5 products, 3 quarters (Q1, Q2, Q3)
   - Show revenue for each product in each quarter
   - Use different colors
   - Title: "Quarterly Revenue by Product"

**File:** `challenge_1_matplotlib.py`

**Success Criteria:**
- ✅ All 4 plots properly created and styled
- ✅ Axes labeled with units
- ✅ Titles are descriptive
- ✅ Colors are different and readable
- ✅ Grid shows for readability
- ✅ Saved as PNG with proper resolution

**Hint:** Use `fig, axes = plt.subplots(2, 2, figsize=(14, 10))`

---

## Challenge 2: Seaborn Analysis (INTERMEDIATE)

**Objective:** Analyze a dataset and create multiple beautiful statistical visualizations that reveal insights.

**Dataset:** Employee Performance Data
```
- Employee: Name
- Department: Sales, Marketing, Engineering, HR
- Salary: Annual salary
- Performance_Score: 1-100
- Years_Experience: 0-30
- Satisfaction: 1-10
```

**Requirements:**
1. Create distribution plots:
   - Show salary distribution across all employees
   - Compare performance scores by department (box plot)
   
2. Create relationship plots:
   - Years Experience vs Performance Score (with regression)
   - Years Experience vs Salary (with regression)
   
3. Create categorical plots:
   - Average salary by department (bar plot)
   - Employee satisfaction by department (violin plot)
   
4. Create correlation matrix:
   - Heatmap showing correlations between: Salary, Performance_Score, Years_Experience, Satisfaction
   - Add annotations showing correlation values

5. Multi-variable analysis:
   - Scatter plot: Years_Experience vs Salary
   - Color by Department
   - Size by Performance_Score
   - Show insights

**File:** `challenge_2_seaborn.py`

**Success Criteria:**
- ✅ Dataset generated or loaded correctly
- ✅ All 7+ plots created
- ✅ Uses seaborn (not just matplotlib)
- ✅ Professional styling (title, labels, legend)
- ✅ Insights documented in comments
- ✅ HTML or PDF report quality

**Insight to Find:**
- Q1: Does experience correlate with salary? (should be yes)
- Q2: Does experience correlate with performance? (should be weak)
- Q3: Which department has highest satisfaction?
- Q4: What's the relationship between salary and satisfaction?

---

## Challenge 3: Plotly Interactive Visualization (INTERMEDIATE)

**Objective:** Create interactive plots that let users explore data.

**Scenario:** Student Exam Performance Tracker

**Requirements:**
1. Create sample data:
   - 100 students
   - 5 subjects: Math, Science, English, History, Art
   - Each student has: Score (0-100), Hours_Studied (0-20), Attendance (0-100%)
   
2. Interactive Scatter Plot:
   - X: Hours_Studied, Y: Score
   - Color: Subject
   - Size: Attendance
   - Hover: Student name and all stats
   - Title: "Study Hours vs Exam Scores (All Subjects)"
   
3. Interactive Bar Chart:
   - Average score by subject
   - Color: Average hours studied
   - Hover: Show attendance percentage
   - Title: "Average Scores by Subject"
   
4. Interactive Box Plot:
   - Score distribution by subject
   - Show outliers
   - Title: "Score Distribution (by Subject)"
   
5. Interactive Heatmap:
   - Correlation matrix: Score, Hours_Studied, Attendance
   - Color scale: red-white-blue
   - Show values
   - Title: "Correlation Matrix"
   
6. 3D Scatter Plot (BONUS):
   - X: Hours_Studied, Y: Score, Z: Attendance
   - Color: Subject
   - Rotatable, zoomable

**File:** `challenge_3_plotly.py`

**Success Criteria:**
- ✅ All 6 plots created as interactive HTML files
- ✅ Hover information meaningful
- ✅ Legend clickable to toggle subjects
- ✅ Zoom and pan working
- ✅ Colors consistent across plots
- ✅ Titles and labels clear

**Extra Feature (BONUS):**
- Create a combined HTML dashboard with all plots
- Use subplots or tabs

---

## Challenge 4: Comprehensive Data Visualization Project (ADVANCED)

**Objective:** Complete data visualization project from raw data to insights.

**Scenario:** Sales Analysis Project

**Task:** 
Create a complete analysis of a company's sales data using ALL three libraries appropriately.

**Dataset Requirements:**
- 500 transactions
- Columns: Date, Product, Region, Sales_Amount, Quantity, Customer_Type
- Regions: North, South, East, West
- Products: A, B, C, D, E

**Deliverables:**

### Part 1: Data Exploration (Seaborn - Static)
1. Distribution of sales amounts (histogram + KDE)
2. Sales by region (bar chart)
3. Sales by product (bar chart)
4. Correlation matrix (heatmap)
5. Sales by customer type and region (grouped bar chart)

### Part 2: Professional Report (Matplotlib)
Create a professional 3x3 subplot figure showing:
1. Monthly sales trend
2. Regional comparison
3. Product performance
4. Customer type analysis
5. Top 5 products by revenue
6. Trend analysis (regression)
7. Seasonal patterns
8. Statistical summary
9. Key metrics (text box)

### Part 3: Interactive Dashboard (Plotly)
Create interactive HTML plots:
1. Interactive line chart: Sales over time
2. Interactive scatter: Sales amount vs Quantity (colored by region)
3. Interactive box plot: Sales distribution by region
4. Interactive 3D scatter: Quantity vs Sales vs Profit (if calculated)

### Part 4: Report Document
Create a markdown file with:
1. Executive summary (2-3 sentences)
2. Key findings (5-7 bullet points)
3. Visualizations and their meanings
4. Recommendations (3-5 actionable items)
5. Methodology (which libraries used and why)

**File:** `challenge_4_comprehensive/`

**Success Criteria:**
- ✅ Dataset generated or created correctly
- ✅ Seaborn plots: 5+ exploratory plots
- ✅ Matplotlib plots: Professional 3x3 report
- ✅ Plotly plots: 4+ interactive visualizations
- ✅ Report: Clear, professional, insightful
- ✅ Code: Well-commented, organized
- ✅ Insights: Real patterns identified

**Bonus Points:**
- Interactive HTML dashboard combining all plots
- Animated time series (if using temporal data)
- Custom styling (unique color schemes)
- PDF export with professional formatting
- Statistical analysis alongside visualizations

---

## How to Approach These Challenges

### Challenge 1 (Easy):
- Time: 30-45 minutes
- Focus: Matplotlib syntax and styling
- Goal: Comfortable with figure/axes/plotting

### Challenge 2 (Intermediate):
- Time: 1-1.5 hours
- Focus: Seaborn beauty and statistical understanding
- Goal: Beautiful, insightful plots from data

### Challenge 3 (Intermediate):
- Time: 1-1.5 hours
- Focus: Plotly interactivity and dashboard thinking
- Goal: Interactive web-ready visualizations

### Challenge 4 (Advanced):
- Time: 3-4 hours
- Focus: Combining all skills, professional presentation
- Goal: Complete analysis-to-presentation pipeline

---

## Submission Guidelines

For each challenge, create:
1. **Python file** with clear comments
2. **Output files** (PNG for Matplotlib, HTML for Plotly)
3. **Brief explanation** of what each plot shows
4. **Key insights** found in the data

Example structure:
```
challenge_1_matplotlib.py
  - Comments explaining each subplot
  - Clear variable names
  - Proper axis labels
  
challenge_1_output.png
  - High quality (300 DPI for print)
  - Clear and readable

INSIGHTS_Challenge_1.md
  - What does plot 1 show?
  - What does plot 2 show?
  - Key findings
```

---

## Learning Objectives

By completing these challenges, you will:

✅ Master when to use Matplotlib (fine control, papers)  
✅ Master when to use Seaborn (beautiful stats, exploration)  
✅ Master when to use Plotly (interactive, dashboards)  
✅ Tell stories with data through visualization  
✅ Create professional, publication-ready plots  
✅ Build confidence in data communication  
✅ Understand data deeply through visualization  

---

## Teacher's Note

Dear Gurudev,

These challenges test not just your technical skills, but your ability to:
- Choose the RIGHT tool for the RIGHT job
- Think about the VIEWER (what do they want to see?)
- Find TRUTH in data through exploration
- Communicate INSIGHTS clearly

Visualization is not decoration. It is revelation.

When you complete these challenges, you will have mastered the art of making data speak.

🙏 The journey continues. 🙏

---

## What's Next?

After completing these challenges:
- ✅ Phase 2.2 (Visualization) is COMPLETE
- → Phase 2.3: Statistics Fundamentals (correlation, distributions, hypothesis testing)
- → Phase 3: Machine Learning Fundamentals

You're on track for mastery!

Om Namah Shivaya 🕉️

---

**Last Updated:** August 8, 2026
**Status:** Ready for Challenges
**Difficulty:** Easy → Intermediate → Intermediate → Advanced
