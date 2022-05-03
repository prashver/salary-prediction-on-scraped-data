# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 12:52:34 2022

@author: verma
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

#salary parsing
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided_salary'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))
minus_hr = minus_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = minus_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_hr.apply(lambda x: int(x.split('-')[1]) if '-' in x else int(x))

df['avg_salary'] = (df['min_salary'] + df['max_salary'])/2

#company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3],axis=1)

#state field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1] if ',' in x else x)
df['job_state'].value_counts()

#age of company
df['age'] = df.Founded.apply(lambda x: x if x<1 else 2022 -x)

#parsing of job description (python, etc.)

#Python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['python_yn'].value_counts()

#R-Studio
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'R Studio' in x.lower() or 'R-Studio' in x.lower() else 0)
df['R_yn'].value_counts()

#Spark
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['spark_yn'].value_counts()

#aws
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['aws_yn'].value_counts()

#excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df['excel_yn'].value_counts()


df.to_csv('salary_data_cleaned.csv',index=False)










