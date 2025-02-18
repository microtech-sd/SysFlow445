def calculate_exergy(enthalpy, entropy, ambient_temp):
    return enthalpy - ambient_temp * entropy

def exergy_efficiency(enthalpy, exergy):
    total = enthalpy + exergy
    return (enthalpy / total) * 100, (exergy / total) * 100

