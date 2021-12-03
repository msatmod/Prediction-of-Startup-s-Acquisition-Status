# Prediction of Startup's Acquisition Status

The goal of this project is to predict a former startup’s acquisition status based on a company’s financial statistics.

## Objective:
The objective of the project is to predict whether a startup which is currently Operating, IPO, Acquired, or closed. This problem will be solved through a Supervised Machine Learning approach by training a model based on the history of startups which were either acquired or closed.

## Dataset
- The dataset used for this project is a kaggle dataset sourced from Crunchbase called: “Crunchbase 2013- Companies, Investors, etc.”
- There are nearly 196553 rows and 15 columns, each row of the dataset contains a startup’s information.
- The dataset labels show that the dataset is extremely biased.

## Exploratory Data Analytics (EDA)
Exploratory data analysis is a way to better understand your data which helps in further Data preprocessing. 
And data visualization is key, making the exploratory data analysis process streamline and easily analyzing data using wonderful plots and charts.

## Data Cleaning
Data cleaning is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset. When combining multiple data sources, there are many opportunities for data to be duplicated or mislabeled. If data is incorrect, outcomes and algorithms are unreliable, even though they may look correct. 

- The dataset had many features and attributes, all were not relevant for the prediction of the startup’s status such as “Company Name”, “unnamed: 0” and many other columns, hence we dropped all the unnecessary data columns.
- Afterwards, we removed the inconsistencies present in the datatype of some columns to have a uniform dataset. 
- Then, handling missing values and removing the duplicates values was primordial in order to continue with the data exploration and analysis. 
- Removing the outliers with the help of IQR method was important as outliers are excessively deviating the value from the scale of the feature.

## Data Transformation 
It is the process of converting data from one format or structure into another. 

- Here we did One Hot Encoding on Category and Country_code columns as there were so many countries and  the data can be provided to machine learning algorithms to improve predictions. This created new columns for each Country_code.
- Two more columns were added: “isClosed” tells us whether the startup is still running or closed and “Active days” which shows the number since the startup has been running. 

## Model Building

Random Forest Model

The random forest is a model made up of many decision trees. Rather than just simply averaging the prediction of trees (which we could call a “forest”), this model uses two key concepts that gives it the name random:

1. Random sampling of training data points when building trees
2. Random subsets of features considered when splitting nodes

We have built one model without hyperparameters tuning and one with hyperparameters tuning. The final data consists of  3496 rows and 7 columns.

## Model Evaluation

Model Evaluation is an integral part of the model development process. It helps to find the best model that represents our data and how well the chosen model will work in the future.

Confusion Matrix A confusion matrix is a correlation between the predictions of a model and the actual class labels of the data points.


## Deployment

The project is hosted on Heroku which is a cloud Platform as a container-based Service (PaaS). Heroku is used by developers to launch, manage, and grow contemporary programs. Heroku is an open-source software platform for machine learning and data science that makes it simple to develop and publish attractive, bespoke web apps.

The tools used for this project are HTML, CSS, FLASK and HEROKU.


### Working Demo App Link:- https://startup-acquisition-status.herokuapp.com/


