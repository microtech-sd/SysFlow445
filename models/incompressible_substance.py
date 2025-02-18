def calculate_incompressible(temperature, pressure):
    # Approximate formula for incompressible fluids (simplified)
    # In this case, we assume ideal values for entropy and enthalpy.
    specific_volume = 1.0  # Assumed constant for incompressible fluid
    enthalpy = temperature * 4.18  # Example relationship (simplified)
    entropy = 4.18 * temperature  # Simplified formula
    return enthalpy, entropy, specific_volume

