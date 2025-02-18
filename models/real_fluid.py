import pandas as pd

def calculate_real_fluid(temperature, pressure, data):
    # Assuming data is a pandas DataFrame loaded from Excel
    fluid_data = data[(data['Temperature'] == temperature) & (data['Pressure'] == pressure)]
    if fluid_data.empty:
        return None, None, None
    else:
        return fluid_data['Enthalpy'].values[0], fluid_data['Entropy'].values[0], fluid_data['Specific Volume'].values[0]
