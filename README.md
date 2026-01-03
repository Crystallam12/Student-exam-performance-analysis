# Student Exam Performance Data Analysis
## Project Overview
This project analyzes student exam performance data to explore the relation between academic performance to demographics
and educational factors. Using Python based exploratory data analysis techniques, this analysis explores score 
distributions, subject relationships, and the impact of gender, parental education, and test preparation on overall
student performance.

## Dataset
The dataset was sourced from Kaggle and contains math, reading, and writing exam scores for 1000 students, along with 
gender, parent education level, and test preparation completion variables.
## Methodology
An **Overall Score** was calculated for each student as the average of their math, reading, and writing exam 
scores. This metric was used to analyze the overall score distribution, and to identify how gender, parental education,
and test preparation relate to overall academic performance.
## Visualizations
### Figure 1: Distribution of Overall Student Exam Scores.
![Figure1](figures/fig1_overall_distribution.png)
**Caption:**
Overall student exam scores follow an approximately normal distribution, with a mean score of 67.77 across all students.
### Figure 2: Overall Exam Score Distribution Between Female and Male Students.
![Figure2](figures/fig2_gender_score_distribution.png)
**Caption:**
Both female and male students show an approximate normal distribution for overall exam scores. However, female students 
have a slightly higher average at 69.57 compared to the average male score at 65.84.
### Figure 3: Impact of Test Preparation on Average Exam Scores for Each Subject.
![Figure3](figures/fig3_preparation_distribution.png)
**Caption:**
Students who completed the test preparation achieved higher average score across all subjects compared to students who
did not complete the test preparation.
### Figure 4: Relationship between Reading and Writing Scores
![Figure4](figures/fig4_reading_writing_correlation.png)
**Caption:**
Reading and writing scores show a strong positive relationship with a correlation of 0.9546, indicating that students 
who perform well in reading tend to perform similarly in writing.
### Figure 5: Parent Education Distribution Among Top and Bottom Quartiles of Student Performance
![Figure5](figures/fig5_parent_education_distribution.png)
**Caption:**
Students in the top performance quartile are more likely to have parents with higher education such as a bachelor's 
degree or a master's degree compared to students in the bottom performance quartile.
## Key Takeaways
- Overall student performance follows an approximately normal distribution with most students scoring near the mean score.
- Performance distributions of both female and male students follow a similar approximately normal distribution, with female students achieving a slightly higher average than males.
- Completion of the test preparation is associated with higher scores across all subjects.
- Higher parental education levels are more prevalent in the students of the top performing quartile, highlighting a potential influence of educational support from parents on academic outcomes.
## Tools Used
- Python
- Pandas
- Matplotlib
- Numpy
- Scipy.stats
- Math