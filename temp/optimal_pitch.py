from __future__ import annotations

import sympy as sp
import numpy as np

from pitch_assist import Prop, Motor, Velocity, rpm_to_theta


AIR_DENSITY = 1.22
MOTOR_EFFICIENCY = 0.8
LOSES = 0.83


INCH_M_CONSTANT = 39.37

v1 = sp.Symbol('v1', real=True)
         
    
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
TOP_MOTOR = Motor(160, 0.51, 48.3, 3.8)
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
    v0_mag = v0_total.give_magnitude()
    v1_mag = v1_total.give_magnitude()
    v0_angle = v0_total.give_angle()
    v1_angle = v1_total.give_angle()
    print(f"v0 mag: {v0_mag}, v0 angle: {v0_angle}")
    print(f"v1 mag: {v1_mag}, v1 angle: {v1_angle}")
    print(top_prop.angle())

main(FOLD, FOLD, TOP_MOTOR, BOT_MOTOR)

