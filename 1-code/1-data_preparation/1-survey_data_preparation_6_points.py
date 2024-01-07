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
