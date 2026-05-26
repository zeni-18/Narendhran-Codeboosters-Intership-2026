import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. Load Data & Create SQLite Database
# ==========================================
# Load the uploaded CSV file
df = pd.read_csv('student_performance.csv')

# Create an in-memory SQLite database
conn = sqlite3.connect(':memory:')

# Write the dataframe into the SQL database as a table named 'students'
df.to_sql('students', conn, index=False)

# ==========================================
# 2. SQL QUERIES
# ==========================================

# Query 1: Avg math by department
query1 = """
    SELECT department, AVG(math_score) as avg_math 
    FROM students 
    GROUP BY department
"""
df_math_dept = pd.read_sql_query(query1, conn)

# Query 2: Student count by department
query2 = """
    SELECT department, COUNT(*) as student_count 
    FROM students 
    GROUP BY department
"""
df_count_dept = pd.read_sql_query(query2, conn)

# Query 3: Top 8 students by total score
# We calculate total score by summing the 4 subject scores present in the CSV
query3 = """
    SELECT name, (math_score + science_score + english_score + programming_score) as total_score 
    FROM students 
    ORDER BY total_score DESC 
    LIMIT 8
"""
df_top_students = pd.read_sql_query(query3, conn)

# Query 4: Gender-wise average attendance
# The column name in the CSV is 'attendance_percentage'
query4 = """
    SELECT gender, AVG(attendance_percentage) as avg_attendance 
    FROM students 
    GROUP BY gender
"""
df_gender_att = pd.read_sql_query(query4, conn)

# ==========================================
# 3. MATPLOTLIB DASHBOARD (2x2 Grid)
# ==========================================
fig, axs = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Student Performance Dashboard', fontsize=16, fontweight='bold')

# ── Panel 1 (top-left): Avg Math by Department - BAR Chart ──
axs[0, 0].bar(df_math_dept['department'], df_math_dept['avg_math'], color='skyblue', edgecolor='black')
axs[0, 0].set_title('Average Math Score by Department')
axs[0, 0].set_xlabel('Department')
axs[0, 0].set_ylabel('Average Math Score')
axs[0, 0].tick_params(axis='x', rotation=15)

# ── Panel 2 (top-right): Student Count Pie Chart ──
axs[0, 1].pie(df_count_dept['student_count'], labels=df_count_dept['department'], autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0'])
axs[0, 1].set_title('Student Count by Department')

# ── Panel 3 (bottom-left): Top 8 Students Horizontal Bar ──
# Sorting ascending for horizontal bar chart so the highest is at the top
df_top_students = df_top_students.sort_values(by='total_score', ascending=True)
axs[1, 0].barh(df_top_students['name'], df_top_students['total_score'], color='lightgreen', edgecolor='black')
axs[1, 0].set_title('Top 8 Students by Total Score')
axs[1, 0].set_xlabel('Total Score')
axs[1, 0].set_ylabel('Student Name')

# ── Panel 4 (bottom-right): Gender Avg Attendance Bar ──
axs[1, 1].bar(df_gender_att['gender'], df_gender_att['avg_attendance'], color=['salmon', 'lightblue'], edgecolor='black', width=0.5)
axs[1, 1].set_title('Gender-wise Average Attendance')
axs[1, 1].set_xlabel('Gender')
axs[1, 1].set_ylabel('Average Attendance (%)')
axs[1, 1].set_ylim(0, 100) # Attendance is out of 100

# Adjust layout to prevent overlapping text
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show the dashboard
plt.show()

# Close the database connection
conn.close()