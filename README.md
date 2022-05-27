# Data Science Salary Estimator
- Created a tool that estimates data science salaries to help data scientists negotiate their income when they get a job.
- Scraped over 1000 job descriptions from glassdoor using python and selenium.
- Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
- Used various regression techniques to get the best model.

# Technologies/Libraries Used
- Python 3
- Pandas
- NumPy
- Seaborn
- Scikit-learn
- Matplotlib
- Spyder
- Jupyter

# Web Scraping
Used the web scraper  to scrape 1000 job postings from glassdoor.com. With each job, we got the following:
- Job title
- Salary Estimate
- Job Description
- Rating
- Company
- Location
- Company Headquarters
- Company Size
- Company Founded Date
- Type of Ownership
- Industry
- Sector
- Revenue

# Data Cleaning
After scraping the data, I cleaned it up so that it can be useful for your analysis. For that I did the following changes:
- Parsed numeric data out of the salary
- Parsed rating from company text
- Removed rows without salary
- Separate columns for Employer provided salary and hourly wages
- Made columns for if different skills were listed in the job description:
  - Python
  - R
  - Excel
  - AWS
  - Spark
- Column for description length

# EDA
Performed an overall exploratory data analysis to figure out the relations among features and categorize the important features of analysis using various plots.

# Model Building
Firstly, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried three different models and evaluated them using Mean Absolute Error. Those models are:
- **Multiple Linear Regression** – Baseline for the model
- **Lasso Regression** – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
- **Random Forest** – Again, with the sparsity associated with the data, I thought that this would be a good fit

# Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets.
- Linear Regression: MAE = 18.23
- Lasso Regression: MAE = 19.61
- - Random Forest : MAE = 11.09

# Productionization
_In Progress_

