import matplotlib.pyplot as plt

def plot_temperature_entropy(temperature, enthalpy, entropy):
    fig, ax = plt.subplots()
    ax.plot([temperature, temperature], [0, entropy], label="Temperature vs Entropy")
    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel("Entropy (kJ/kg·K)")
    ax.set_title("Temperature vs Entropy")
    return fig

def plot_pressure_volume(pressure, specific_volume):
    fig, ax = plt.subplots()
    ax.plot([pressure, pressure], [0, specific_volume], label="Pressure vs Specific Volume")
    ax.set_xlabel("Pressure (Pa)")
    ax.set_ylabel("Specific Volume (m³/kg)")
    ax.set_title("Pressure vs Specific Volume")
    return fig

