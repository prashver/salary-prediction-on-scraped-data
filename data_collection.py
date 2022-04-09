# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 13:31:24 2022

@author: verma
"""

import glassdoor_scraper as gs

path= "C:/Projects/salary_project_ds/chromedriver"

df = gs.get_jobs('data scientist',1000,False,path,5)

df.to_csv('glassdoor_jobs.csv',index=False)