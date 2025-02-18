def calculate_ideal_gas(temperature, pressure):
    # Ideal Gas Law: PV = nRT -> V = nRT/P
    R = 8.314  # Universal gas constant in J/(mol·K)
    n = 1.0  # Assumed 1 mole of gas
    specific_volume = (R * temperature) / pressure  # Ideal gas equation
    enthalpy = specific_volume * pressure  # Simplified enthalpy calculation
    entropy = specific_volume * (R * temperature)  # Simplified entropy calculation
    return enthalpy, entropy, specific_volume

