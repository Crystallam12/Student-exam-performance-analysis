#Student Exam Performance Analysis
import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv('data/StudentsPerformance.csv')
SAMPLESIZE = len(dataframe) #there are 1000 datapoints, SAMPLESIZE = 1000
#explore/preview data
print(dataframe.head())
print(dataframe.describe()) #summary statistics for math, reading, and writing scores.
print(dataframe.info()) #gives summary of dataframe structure

#check for missing values
missing = dataframe.isnull().sum()
if missing.sum() == 0:
    print('No missing datapoints')
else:
    print('Missing Values: \n', missing)

import math
import numpy as np
from scipy.stats import norm


#Distribution of Overall Test Scores (all subjects combined average score per student)
dataframe['Overall Average'] = dataframe[['math score', 'reading score', 'writing score']].mean(axis = 1)
overall_average = dataframe['Overall Average']
print('Overall Average')

score_mean = dataframe['Overall Average'].mean()
score_std = dataframe['Overall Average'].std()
print(score_mean) #the average overall score of all students
x = np.linspace(0, 100, 1000) #horizontal

plt.hist(
    overall_average,
    bins = int(math.sqrt(SAMPLESIZE)),
    density = True,
    edgecolor = 'white',
    color = 'steelblue',
    linewidth = 1,
    alpha = 0.85
) #plot distribution
plt.plot(
    x,
    norm.pdf(x, score_mean, score_std),
    label = 'Normal Curve',
    color = 'navy',
    linewidth = 1.5
) #normal distribution (bell) curve
plt.axvline(score_mean, color = 'red', linestyle = '--', linewidth = 2, label = 'Mean') #overall mean
plt.xticks(np.arange(0,101, 10)) #want x-axis to go up increments of 10
plt.xlabel("Overall Exam Score")
plt.ylabel("Probability Density of Students")
plt.title("Distribution of Overall Student Exam Scores")
plt.legend()
plt.tight_layout()
plt.savefig('figures/fig1_overall_distribution.png', dpi = 300, bbox_inches = 'tight')
plt.show()


#Distribution of Overall Exam Scores by Gender
counts = dataframe['gender'].value_counts()
print(counts)
female_overall = dataframe.loc[dataframe['gender']=='female', 'Overall Average']
male_overall = dataframe.loc[dataframe['gender']=='male', 'Overall Average']
female_mean = female_overall.mean()
male_mean = male_overall.mean()
print('Female Average Score' + ':' + str(female_mean))
print('Male Average Score' + ':' + str(male_mean))
female_std = female_overall.std()
male_std = male_overall.std()

plt.hist(
    female_overall,
    density = True,
    edgecolor = 'white',
    bins = int(math.sqrt(SAMPLESIZE/2)),
    label = 'Female Students',
    linewidth = 1
) #Plot distribution for female scores
plt.hist(
    male_overall,
    density = True,
    edgecolor = 'white',
    alpha = 0.7,
    bins = int(math.sqrt(SAMPLESIZE/2)),
    label = 'Male Students',
    linewidth = 1
) #Plot distribution for male scores
plt.plot(
    x,
    norm.pdf(x, female_mean, female_std),
    color = 'navy',
    label = 'Normal Distribution for Females'
)
plt.plot(
    x,
    norm.pdf(x, male_mean, male_std),
    color = 'firebrick',
    label = 'Normal Distribution for Males'
)
plt.xticks(np.arange(0,101, 10))
plt.xlabel('Overall Exam Score')
plt.ylabel('Probability Density of Students')
plt.title("Overall Exam Score Distribution Between Female and Male Students")
plt.legend()
plt.savefig('figures/fig2_gender_score_distribution.png', dpi = 300, bbox_inches = 'tight')
plt.show()


#Comparing the scores of students who took the preparation test

prep_all_scores = dataframe.groupby('test preparation course')[
    [
    'math score',
    'reading score',
    'writing score']
].mean()
print(prep_all_scores)
g = prep_all_scores
subjects = ['Math', 'Reading', 'Writing']
s = np.arange(len(subjects))
prep = g.index #Test preparation Completed and None

width = 0.35

plt.bar(
    s - width/2,
    g.loc["completed"],
    width = 0.3,
    label='Preparation Completed',
    color = 'blue'
) #average score per subject when test preparation was done
plt.bar(
    s + width/2,
    g.loc['none'],
    width = 0.3,
    label = 'No Preparation',
    color = 'orange'
) #average score per subject when no test preparation was done
plt.ylim(0,100)
plt.title("Impact of Test Preparation on Average Exam Scores")
plt.ylabel("Average scores")
plt.xlabel("Subject Exams Scores")
plt.xticks(s, subjects)
plt.legend()
plt.tight_layout()
plt.savefig('figures/fig3_preparation_distribution.png', dpi = 300, bbox_inches = 'tight')
plt.show()


#Distribution of reading and writing scores to find correlation

plt.scatter(dataframe['reading score'], dataframe['writing score'], s = 20)
plt.xlabel("Reading Score")
plt.ylabel("Writing Score")
plt.title("Relationship between Reading and Writing Scores")
x_read = dataframe['reading score']
y_write = dataframe['writing score']
m, b = np.polyfit(x_read, y_write, 1)
plt.plot(x_read, x_read*m + b, '--', color = 'red', label = "Linear Regression")
#linear regression line used to quantify the correlation between reading and writing scores
plt.legend()
plt.tight_layout()
plt.savefig('figures/fig4_reading_writing_correlation.png', dpi = 300, bbox_inches = 'tight')
plt.show()
corr = x_read.corr(y_write)
print(corr)

#Distribution of the parental demographics of the top and bottom performing quartiles
top_25 = dataframe['Overall Average'].quantile(0.75)
bottom_25 = dataframe['Overall Average'].quantile(0.25)
def performance_quartile(score):
    if score >= top_25:
        return 'Top 25%'
    elif score <= bottom_25:
        return 'Bottom 25%'
    else:
        return 'Middle 50%'
dataframe['Performance Quartile'] = dataframe['Overall Average'].apply(performance_quartile)
print(dataframe['Performance Quartile'])
comb = dataframe.groupby(['Performance Quartile','parental level of education']).size()
print(comb)
top_bottom = dataframe[dataframe['Performance Quartile'].isin(['Top 25%','Bottom 25%'])]
print(top_bottom)
edu_order = ['some high school',
             'high school',
             'some college',
             "associate's degree",
             "bachelor's degree",
             "master's degree"
]
dataframe['parental level of education'] = pd.Categorical(
    dataframe['parental level of education'],
    categories = edu_order,
    ordered = True
)
pivot = top_bottom.pivot_table(
    index='Performance Quartile',
    columns= 'parental level of education',
    aggfunc= 'size',
    fill_value=0
)
pivot = pivot[edu_order]
print(pivot) #shows the count of how many students in each category with that parental education
pivot_percent = pivot.div(pivot.sum(axis = 1), axis = 0) #change the count to a percentage
print(pivot_percent)

pivot_percent.plot(kind='bar', stacked = True)
plt.xlabel("Performance Quartile")
plt.ylabel("Proportion of Students")
plt.title('Parent Education Distribution Among Top and Bottom \n Quartiles of Student Performance')
plt.legend(
    title = 'Parent Education',
    loc = 'upper right',
    fontsize = 7,
    title_fontsize = 8
)
plt.tight_layout()
plt.savefig('figures/fig5_parent_education_distribution.png', dpi = 300, bbox_inches = 'tight')
plt.show()



