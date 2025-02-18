import pandas as pd

def read_excel_data(uploaded_file):
    # Read the Excel file into a DataFrame
    data = pd.read_excel(uploaded_file, sheet_name="Sheet1")
    return data

