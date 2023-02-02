from __future__ import annotations

# Library Imports
import sympy as sp

# Module Imports
from pitch_assist import Prop, Motor, Velocity, rpm_to_theta

# Constants (may need to be altered)
AIR_DENSITY = 1.21
MOTOR_EFFICIENCY = 0.8
LOSES = 0.82


# PROP TO CHOOSE FROM
F18 = Prop(18.3, 6.2, 0.04)
FOLD = Prop(18.2, 5.9, 0.04)

# ======================================
# EDIT THESE VALUES!!!!
TOP_MOTOR = Motor(140, 0.51, 48.3, 2.55)
BOT_MOTOR = Motor(160, 0.51, 48.3, 4)
TOP_PROP = FOLD
BACK_PROP = FOLD
# ======================================

v1 = sp.Symbol('v1', real=True)        

    
def give_v0(top_prop: Prop, top_motor: Motor) -> Velocity:
    """ Finds the local velocity at the front prop

    Args:
        top_prop (Prop): Top prop values
        top_motor (Motor): Top motor values

    Returns:
        Velocity: Velocity vector (all in y)
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
    print(motor.give_rpm())
    v_rel = sp.N(rpm_to_theta(motor.give_rpm()) * prop.seventy_five_len())
    
    return Velocity(v_rel, 0)

def pitch_to_angle_ratio(prop: Prop) -> float:
    angle = prop.angle()
    return angle / prop.pitch

def optimal_angle(v0_total: Velocity, v1_total: Velocity, bottom_prop: Prop) -> float:
    """ Finds the ratio to pitch in inches to an angle. 
        Assumes linear relationship so only can be used for small angles

    Args:
        v0_total (Velocity): The total velocity leaving the first prop
        v1_total (Velocity): The total local velocity at the 2nd prop

    Returns:
        float: The ratio to multiply the angle with
    """
    
    v0_angle = v0_total.give_angle()
    v1_angle = v1_total.give_angle()
    diff_angle = v1_angle - v0_angle
    ratio = pitch_to_angle_ratio(bottom_prop)
    
    print(f"Angle: {diff_angle}")
    


def main(top_prop: Prop, back_prop: Prop, top_motor: Motor, back_motor: Motor):
    """ Main function where function calls are made. Inside one function for trouble shooting

    Args:
        top_prop (Prop): The top prop to use
        back_prop (Prop): The back prop to use
        top_motor (Motor): The top motor to use
        back_motor (Motor): The back motor to use
    """
    
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

main(TOP_PROP, BACK_PROP, TOP_MOTOR, BOT_MOTOR)

