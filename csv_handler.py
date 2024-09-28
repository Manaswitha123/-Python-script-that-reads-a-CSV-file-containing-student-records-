import pandas as pd

# Read the CSV file
df = pd.read_csv('students.csv')

# Calculate the average grade
average_grade = df['grade'].mean()
print(f'Average Grade: {average_grade}')

# Find the student with the highest grade
top_student = df.loc[df['grade'].idxmax()]
print(f'Top Student: {top_student["name"]} with grade {top_student["grade"]}')
