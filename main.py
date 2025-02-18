import streamlit as st
import pandas as pd
from models.real_fluid import calculate_real_fluid
from models.incompressible_model import calculate_incompressible
from models.ideal_gas import calculate_ideal_gas
from utils.exergy import calculate_exergy, exergy_efficiency
from utils.excel_utils import read_excel_data
from plots.plotter import plot_temperature_entropy, plot_pressure_volume

# Title and Description
st.title("Thermodynamic Properties Calculator")
st.write("Select the thermodynamic model and provide input parameters.")

# Upload Excel data for real fluid model
uploaded_file = st.file_uploader("Upload Excel data for Real Fluid model", type=["xlsx", "xls"])
if uploaded_file is not None:
    data = read_excel_data(uploaded_file)
    st.write(data.head())  # Display the first few rows of the dataset

# Thermodynamic model choice
model_choice = st.selectbox("Choose a thermodynamic model", ("Real Fluid Model", "Incompressible Model", "Ideal Gas Model"))

# Input parameters (temperature, pressure, etc.)
temperature = st.number_input("Enter Temperature (K)", min_value=0.0, step=1.0)
pressure = st.number_input("Enter Pressure (Pa)", min_value=0.0, step=1000.0)

# Depending on the model, call respective calculation function
if model_choice == "Real Fluid Model":
    if uploaded_file is not None:
        enthalpy, entropy, specific_volume = calculate_real_fluid(temperature, pressure, data)
        st.write(f"Enthalpy: {enthalpy} kJ/kg, Entropy: {entropy} kJ/(kg·K), Specific Volume: {specific_volume} m³/kg")
    else:
        st.write("Please upload the Excel data file for the Real Fluid Model.")
    
elif model_choice == "Incompressible Model":
    # Implement the incompressible model calculation here
    enthalpy, entropy, specific_volume = calculate_incompressible(temperature, pressure)
    st.write(f"Enthalpy: {enthalpy} kJ/kg, Entropy: {entropy} kJ/(kg·K), Specific Volume: {specific_volume} m³/kg")

elif model_choice == "Ideal Gas Model":
    # Implement the ideal gas model calculation here
    enthalpy, entropy, specific_volume = calculate_ideal_gas(temperature, pressure)
    st.write(f"Enthalpy: {enthalpy} kJ/kg, Entropy: {entropy} kJ/(kg·K), Specific Volume: {specific_volume} m³/kg")

# Exergy calculation
ambient_temp = st.number_input("Enter Ambient Temperature (K)", min_value=0.0, step=1.0)
exergy = calculate_exergy(enthalpy, entropy, ambient_temp)
st.write(f"Exergy: {exergy} kJ/kg")

# Exergy efficiency
energy_efficiency, exergy_efficiency = exergy_efficiency(enthalpy, exergy)
st.write(f"Energy Efficiency: {energy_efficiency} %, Exergy Efficiency: {exergy_efficiency} %")

# Plotting Section
plot_choice = st.selectbox("Select Plot", ("Temperature vs Entropy", "Pressure vs Specific Volume"))

if plot_choice == "Temperature vs Entropy":
    plot = plot_temperature_entropy(temperature, enthalpy, entropy)
    st.pyplot(plot)

elif plot_choice == "Pressure vs Specific Volume":
    plot = plot_pressure_volume(pressure, specific_volume)
    st.pyplot(plot)
