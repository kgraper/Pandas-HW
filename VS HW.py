#Dependencies
import pandas as pd

#Reading in schools csv
schools = "Resources/raw_data/schools_complete.csv"
schools_read = pd.read_csv(schools)
schools_read

#Reading in students csv
students = "Resources/raw_data/students_complete.csv"
students_read = pd.read_csv(students)
students_read.head()

#creating the data frames
students_df = pd.DataFrame(students_read)
schools_df = pd.DataFrame(schools_read)

#Merging the data frames
student_school = pd.merge(students_df, schools_df, on = "name", how = "outer")
student_school.head()

#total number of students
total_students = student_school['Student ID'].count()
total_students

# total number of schools
num_schools = student_school["School ID"].count()
num_schools

# total budget of schools
budget_schools = student_school["budget"].sum()
budget_schools

# average math scores
avg_math_score = student_school['math_score'].mean()
avg_math_score

# average reading score
avg_read_score = student_school['reading_score'].mean()
avg_read_score

# total students passing math
# gets data frame to change the view of the 'math score' column to passing value
total_passing_math = student_school.loc[student_school['math_score'] > 69,:]
# stores the passing value number of students as a variable
num_passing_math = total_passing_math['Student ID'].count()
num_passing_math

# calculating the percentage of students passing math
percent_pass_math = num_passing_math / total_students
percent_pass_math

# getting to display as a full percent
percent_pass_math_final = percent_pass_math * 100
percent_pass_math_final

# total students passing reading
# gets data frame to change the view of the 'reading score' column to passing value
total_passing_reading = student_school.loc[student_school['reading_score'] > 69,:]
# stores the passing value number of students as a variable
num_passing_reading = total_passing_reading['Student ID'].count()
num_passing_reading

# calculating the percentage of students passing reading
percent_pass_reading = num_passing_reading / total_students
percent_pass_reading

# getting to display as a full percent
percent_pass_reading_final = percent_pass_reading * 100
percent_pass_reading_final

# overall passing rate of both reading and math (Average of the two)
overall_passing_rate = ((percent_pass_math + percent_pass_reading) / 2) *100
overall_passing_rate

# creating the 'District Summary'
district_table = pd.DataFrame({'Total Schools': [num_schools],
                              'Total Students': [total_students],
                              'Total Budget': [budget_schools],
                             'Average Math Scores': [avg_math_score],
                               'Average Reading Scores': [avg_read_score],
                               'Percent Passing Math': [percent_pass_math_final],
                               'Percent Passing Reading': [percent_pass_reading_final]
                              })
district_table = district_table[['Total Schools',
                                'Total Students',
                                'Total Budget',
                                'Average Math Scores',
                                'Average Reading Scores',
                                'Percent Passing Math',
                                'Percent Passing Reading']]
district_table = district_table.round(2)
district_table

#formatting 'District Summary'
district_table['Total Students'] = district_table['Total Students'].map("{0:,}".format)
district_table['Total Budget'] = district_table['Total Budget'].map("${0:,.2f}".format)
district_table['Percent Passing Math'] = district_table['Percent Passing Math'].map("{0:,.2f}%".format)
district_table['Percent Passing Reading'] = district_table['Percent Passing Reading'].map("{0:,.2f}%".format)
district_table