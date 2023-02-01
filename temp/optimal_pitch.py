from __future__ import annotations

import sympy as sp
import numpy as np



AIR_DENSITY = 1.22
MOTOR_EFFICIENCY = 0.8
LOSES = 0.83


INCH_M_CONSTANT = 39.37

v1 = sp.Symbol('v1', real=True)

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
        working_radius = Prop.seventy_five_len()
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
        
    def give_magnitude(vec: Velocity) -> Velocity:
        return sp.sqrt(vec.vx ** 2 + vec.vy)
    
    def give_angle(vec: Velocity) -> Velocity:
        return sp.atan(vec.vy / vec.vx)
        
        
    
def give_v0(top_prop: Prop, top_motor: Motor) -> Velocity:
    """ Finds the effective exit velocity of the 1st propeller
        using momentum theory

    Args:
        prop (Prop): Propeller characteristics
        # power (float): Power from electric motors supplied

    Returns:
        float: _description_
    """
    
    power = top_motor.give_power()
    v0 = sp.N((power * MOTOR_EFFICIENCY / (2 * top_prop.give_Acs() * AIR_DENSITY)) ** (1 / 3))
    
    return Velocity(0, v0)


def give_v0_star(v0: Velocity) -> Velocity:
    """ Gives the accelerated velocity of the prop that the back prop will experience"""
    v_0_star = 2 * v0.vy * LOSES
    
    return Velocity(0, v_0_star)


def give_v1(v0_star: Velocity, back_prop: Prop, back_motor: Motor) -> Velocity:
    """ Gives the perpendicular air velocity going to back prop"""
    power = back_motor.give_power()
    Acs = back_prop.give_Acs()
    solution = sp.solve((v1 ** 3) - (v0_star.vy * v1 ** 2) - (power * MOTOR_EFFICIENCY / (2 * Acs * AIR_DENSITY)), v1)
    v1_ = max(solution)
    
    return Velocity(0, v1_)

def give_v_swirl(top_prop: Prop, top_motor: Motor) -> Velocity:
    """ Calculates the parallel swirl velocity generated from the top propeller"""
    rotational_velocity = rpm_to_theta(top_motor.give_rpm()) 
    v_swirl = sp.N(top_prop.constant_proportionality *  rotational_velocity *  top_prop.diameter / 2)
    
    return Velocity(v_swirl, 0)

def give_v_rel(prop: Prop, motor: Motor) -> Velocity:
    """ Gives teh parallel relative velocity the prop experiences as it spins"""
    v_rel = sp.N(rpm_to_theta(motor.give_rpm()) * prop.seventy_five_len())
    
    return Velocity(v_rel, 0)
        
        
F18 = Prop(18.3, 6.2, 0.04)
FOLD = Prop(18.2, 5.9, 0.04)
TOP_MOTOR = Motor(140, 0.51, 48.3, 2.55)
BOT_MOTOR = Motor(160, 0.51, 48.3, 3.8)


def main(top_prop: Prop, back_prop: Prop, top_motor: Motor, back_motor: Motor):
    
    v0 = give_v0(top_prop, top_motor)
    v0_star = give_v0_star(v0)
    v1 = give_v1(v0_star, back_prop, back_motor)
    v_swirl = give_v_swirl(top_prop, top_motor)
    v0_rel = give_v_rel(top_prop, top_motor)
    v1_rel = give_v_rel(back_prop, back_motor)
    
    v0_total = Velocity.add_vectors([v0, v0_rel])
    v1_total = Velocity.add_vectors([v1, v_swirl, v1_rel])
    print(v0_total)
    print(v1_total)

main(FOLD, FOLD, TOP_MOTOR, BOT_MOTOR)

