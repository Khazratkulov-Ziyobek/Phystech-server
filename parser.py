# Importing pandas
import pandas as pd

# The webpage URL whose table we want to extract
url = "https://phystech-server.herokuapp.com/"

# Assign the table data to a Pandas dataframe
table = pd.read_html(url)[0]

# Store the dataframe in Excel file
table.to_excel("student_data.xlsx")
