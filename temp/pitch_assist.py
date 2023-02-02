from __future__ import annotations

import sympy as sp
import numpy as np

INCH_M_CONSTANT = 39.37


def inch_to_m(measurement: float) -> float:
    return measurement / INCH_M_CONSTANT

def m_to_inch(measurement: float) -> float:
    return measurement * INCH_M_CONSTANT

def rpm_to_theta(rpm: float) -> float:
    return rpm / 60 * 2 * sp.pi


class Prop:
    """ Class containing the useful prop data and supporting functions"""
    
    def __init__(self, diameter: float, pitch: float, constant_proportionality: float) -> None:
        self.diameter = inch_to_m(diameter)
        self.pitch = inch_to_m(pitch)
        self.constant_proportionality = constant_proportionality
        
    def __str__(self) -> str:
        return f"Diameter (inch): {m_to_inch(self.diameter)}, Pitch (inch): {m_to_inch(self.pitch)}"
    
    
    def seventy_five_len(self) -> float:
        """ Finds the 75% of the prop radius

        Returns:
            float: _description_
        """
        return self.diameter / 2 * 0.75
    
    def give_Acs(self) -> float:
        """ Finds the cross sectional area of the propeller

        Args:
            prop Prop: Prop data

        Returns:
            float: cross sectional area
        """
        return sp.pi * (self.diameter / 2) ** 2
    
    def angle(self) -> float:
        """ Finds the angle of the propeller at 75% of the props radius
        angle = atan(pitch/(2π * 75%len))

        Returns:
            float: Angle (degrees)
        """
        working_radius = Prop.seventy_five_len(self)
        angle = sp.atan(self.pitch / (2 * sp.pi * working_radius))
        return np.rad2deg(float(angle))
    

class Motor:
    
    def __init__(self, kV, throttle_pct, V, I) -> None:
        self.kV = kV
        self.throttle_pct = throttle_pct
        self.V = V
        self.I = I

    def give_power(self) -> float:
        """ Calculates the power based off ohms law P = VI

        Args:
            V (float): Voltage (V)
            I (float): Current (A)

        Returns:
            float: Power (W)
        """
        return self.V * self.I
     
    def give_rpm(self) -> float:
        """ Calculates the rpm of motor"""
        return self.V * self.kV * self.throttle_pct
    

class Velocity:
    """ Velocity class"""
    
    def __init__(self, vx: Velocity, vy: Velocity) -> None:
        self.vx = vx
        self.vy = vy
        
    def __str__(self) -> str:
        return f"Velocity(vx: {self.vx}, vy: {self.vy})"
    
    @classmethod    
    def add_vectors(self, vec_list: list[Velocity]) -> Velocity:
        resultant_vec = Velocity(0, 0)
        
        for vec in vec_list:
            resultant_vec.vx += vec.vx
            resultant_vec.vy += vec.vy
        
        return resultant_vec
    
    @classmethod 
    def give_magnitude(self) -> Velocity:
        return sp.sqrt((self.vx) ** 2 + (self.vy) ** 2)
    
    @classmethod 
    def give_angle(self) -> Velocity:
        angle = float(sp.atan(self.vy / self.vx))
        return np.rad2deg(angle)