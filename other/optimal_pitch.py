from __future__ import annotations

# Library Imports
import sympy as sp

# Module Imports
from pitch_assist import Prop, Motor, Velocity, rpm_to_theta

# Constants (may need to be altered)
AIR_DENSITY = 1.21
MOTOR_EFFICIENCY = 0.8
LOSES = 0.83    # Guessed value. About 22% less thrust is produced than the ideal equation so this is a value somewhere in that range
                # Works well with 140kv - 240kv motors and 15 - 18.3 inch props. Accuracy is not guaranteed passed these values.
                # Prop Should be well matched with motor for accuracy


# PROP TO CHOOSE FROM (add you own)
F18 = Prop(18.3, 6.2, 0.04)
FOLD18 = Prop(18.2, 5.9, 0.04)
FOLD16 = Prop(16.2, 5.3, 0.04)
FOLD15 = Prop(15.2, 5, 0.04)

# ======================================
# EDIT THESE VALUES!!!!
TOP_MOTOR = Motor(160, 0.51, 48.3, 3.8)
BOT_MOTOR = Motor(220, 0.51, 48.3, 5.6)
TOP_PROP = FOLD18
BACK_PROP = FOLD16
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
    loses = (v1_ - v0_star.vy) * ((1 - LOSES) /  3 ) # this 3 just seemed to work better than a 2. Possible error source
    v1_ = v1_ - loses
    
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


def angle_comp(prop: Prop, v_total: Velocity) -> float:
    
    v_angle = v_total.give_angle()
    prop_angle = prop.g_angle()
    return v_angle - prop_angle


def optimal_angle(v0_total: Velocity, v1_total: Velocity, free_v1_total: Velocity, bottom_prop: Prop) -> float:
    """ Finds the optimal angle to pitch the lower prop based on values fed to it

    Args:
        v0_total (Velocity): The local velocity vector of the top propeller
        v1_total (Velocity): The local velocity vector of the bottom propeller
        free_v1_total (Velocity): The local velocity vector of the bottom propeller IF free stream = 0
        bottom_prop (Prop): Bottom Prop parameters

    Returns:
        float: Optimal angle to pitch propellers
    """
    
    v0_angle = v0_total.give_angle()
    v1_angle = v1_total.give_angle()
    free_v1_angle = free_v1_total.give_angle()
    back_prop_angle = bottom_prop.g_angle()
    
    print(v0_angle)
    print(v1_angle)
    print(free_v1_angle)
    print(back_prop_angle)
    
    diff_v_angle = v1_angle - v0_angle
    diff_pv_angle = back_prop_angle - free_v1_angle
    
    opt_angle = diff_v_angle - diff_pv_angle
    
    print(f"Angle: {opt_angle}")
    
    return opt_angle
    


def main(top_prop: Prop, back_prop: Prop, top_motor: Motor, back_motor: Motor):
    """ Main function where function calls are made. Inside one function for trouble shooting

    Args:
        top_prop (Prop): The top prop to use
        back_prop (Prop): The back prop to use
        top_motor (Motor): The top motor to use
        back_motor (Motor): The back motor to use
    """
    
    # Calculates normal velocity's
    v0 = give_v0(top_prop, top_motor)
    v0_star = give_v0_star(v0)
    v1 = give_v1(v0_star, back_prop, back_motor)
    print(v0_star)
    print(v1)
    
    # In plane velocities
    v_swirl = give_v_swirl(top_prop, top_motor)
    v0_rel = give_v_rel(top_prop, top_motor)
    v1_rel = give_v_rel(back_prop, back_motor)
    
    # Total velocities
    v0_total = Velocity.add_vectors([v0, v0_rel])
    v1_total = Velocity.add_vectors([v1, v_swirl, v1_rel])
    
    # Velocity if bottom prop had a free stream velocity of 0
    free_v1_bot = give_v0(back_prop, back_motor)
    free_v1_total = Velocity.add_vectors([free_v1_bot, v1_rel])
    
    optimal_angle(v0_total, v1_total, free_v1_total, back_prop)
    
    v0_mag = v0_total.give_magnitude()
    v1_mag = v1_total.give_magnitude()
    v0_angle = v0_total.give_angle()
    v1_angle = v1_total.give_angle()

    
main(TOP_PROP, BACK_PROP, TOP_MOTOR, BOT_MOTOR)

