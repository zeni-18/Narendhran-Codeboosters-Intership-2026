import os
import sqlite3
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'student_performance.db')

print("="*70)
print("             DAY 2 PRACTICE QUESTIONS SOLUTIONS")
print("="*70)
print()

# Attempt to connect to DB to run queries
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    
    # Q1
    q1_sql = "SELECT AVG(programming_score) FROM students WHERE gender = 'Female';"
    df_q1 = pd.read_sql_query(q1_sql, conn)
    ans1 = df_q1.iloc[0,0]
    ans1_str = f"{ans1:.2f}" if pd.notnull(ans1) else "N/A"
    
    # Q3
    q3_sql = "SELECT department, AVG(attendance_percentage) as avg_att FROM students GROUP BY department HAVING avg_att > 85;"
    df_q3 = pd.read_sql_query(q3_sql, conn)
    ans3_list = df_q3['department'].tolist() if not df_q3.empty else []
    
    conn.close()
else:
    ans1_str = "N/A (Run Mini_Project.py first to create the database)"
    ans3_list = ["N/A (Run Mini_Project.py first to create the database)"]

# Question 1
print("Question 1: Write a SQL query to find the average programming score for female students only.")
print(f"   Answer (Value): {ans1_str}")
print("   SQL Query:")
print("     SELECT AVG(programming_score)")
print("     FROM students")
print("     WHERE gender = 'Female';")
print("-" * 70)

# Question 2
print("Question 2: What is the difference between WHERE and HAVING? Write one example of each using the students table.")
print("   Answer:")
print("     - WHERE: Filters rows BEFORE any grouping (GROUP BY) takes place.")
print("     - HAVING: Filters groups AFTER the GROUP BY clause has been applied.")
print("   Example WHERE:")
print("     SELECT name, math_score FROM students WHERE math_score > 80;")
print("   Example HAVING:")
print("     SELECT department, AVG(math_score) FROM students GROUP BY department HAVING AVG(math_score) > 80;")
print("-" * 70)

# Question 3
print("Question 3: Write a SQL query to find all departments where the average attendance is above 85%.")
print(f"   Answer (Departments): {', '.join(ans3_list)}")
print("   SQL Query:")
print("     SELECT department, AVG(attendance_percentage)")
print("     FROM students")
print("     GROUP BY department")
print("     HAVING AVG(attendance_percentage) > 85;")
print("-" * 70)

# Question 4
print("Question 4: What does pd.read_sql_query() return? What two arguments does it require?")
print("   Answer:")
print("     - Return Value: It returns a Pandas DataFrame containing the results of the SQL query.")
print("     - Required Arguments:")
print("         1. sql: The SQL query string to be executed.")
print("         2. con: The database connection object (e.g., sqlite3 connection engine).")
print("-" * 70)

# Question 5
print("Question 5: Modify Chart 1 (bar chart) to show average PROGRAMMING scores instead of math scores.")
print("   Answer:")
print("     To modify Panel 1 in Mini_Project.py, update the SQL query and Matplotlib code as follows:")
print("\n     1. SQL Query Update:")
print("         query_panel1 = '''")
print("         SELECT department, ROUND(AVG(programming_score), 2) AS avg_prog")
print("         FROM students")
print("         GROUP BY department")
print("         ORDER BY avg_prog DESC;")
print("         '''")
print("\n     2. Matplotlib Update:")
print("         bars1 = ax1.bar(df_panel1['department'], df_panel1['avg_prog'], color=ACCENT_COLORS[0])")
print("         ax1.set_title('Average Programming Score by Department')")
print("         ax1.set_ylabel('Avg Programming Score')")
print("="*70)
