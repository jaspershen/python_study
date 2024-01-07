import pandas as pd 
import os

os.getcwd()

1+1

# Specify the file path
file_path = "2-data/66491TheLastingChang-ReportDemographicsC1_DATA_2023-12-20_2109.csv"

# Read the CSV file
data = pd.read_csv(file_path)

# Print the data
print(data)

data

###how to get the column names
data.columns

###how to get the row names
data.index

###how to get the data types
data.dtypes

##how to get the shape of the data
data.shape

##how to get the summary statistics
data.describe()

###how to get the first 5 rows
data.head()

###how to get the first 10 rows
data.head(10)

###how to get the last 5 rows
data.tail()

###how to get the first row
data.iloc[0]