import numpy as np


Rt = 287.058
Rd = 461.523


def air_density_calc(T: float, humidity: float, pressure: float) -> float:
    """"""
    saturation_vapour_pressure = (6.112) * np.exp((17.62 * T) /(243.12 + T))

    T = T + 273.15

    Rf = Rt / (1 - humidity * saturation_vapour_pressure / pressure * (1 - Rt/Rd))

    density = pressure / (Rf * T)
    
    return density


def keeper():
    """"""
    Tue_2 = air_density_calc(20, 0.75, 1012)
    Wed_9 = air_density_calc(16, 0.96, 1010)
    Wed_2 = air_density_calc(22.5, 0.61, 1013)
    Fri_8 = air_density_calc(15.9, 0.99, 1004)
    Mon_9 = air_density_calc(21, 0.80, 1019)
    
    print(Tue_2)
    print(Wed_9)
    print(Wed_2)
    print(Fri_8)
    print(Mon_9)
    
    print(f"Difference is {Fri_8 - Wed_2}")
    
keeper()
    




