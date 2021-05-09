# Importing pandas
import pandas as pd

# The webpage URL whose table we want to extract
url = ""

# Assign the table data to a Pandas dataframe
table = pd.read_html(url)[0]

# Store the dataframe in Excel file
table.to_excel("student_data.xlsx")
