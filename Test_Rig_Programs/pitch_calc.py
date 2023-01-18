# ===================================================
# AUTHOR        : Oliver Clements
# CREATE DATE   : 2/12/22
# PURPOSE       : Calculates pitch of propeller    
# ===================================================

import numpy as np
MM_TO_INCH = 0.03937007874
INCH_TO_MM = 25.4

#   These are at 75% along
# L75 = 16.2 / 2 * 0.75
# T_H = 13.82
# T_L = 10.65
# WIDTH = 22.69

def mm_to_inch(measurement):
    """ Converts mm to inch"""
    return measurement * MM_TO_INCH


def inch_to_mm(measurement):
    """ Converts inch to mm"""
    return measurement * INCH_TO_MM


def l_75_func(prop_len):
    """ finds the 75% len of prop"""
    return (prop_len / 2) * 0.75


def angle_distance(width, l_75):
    """ Finds the angle from shaft to the with of each end
        of the prop """
    theta = 2 * np.arctan(width / (2 * l_75))
    return theta


def current_pitch_inch(angle, th, tl):
    """ FInds the current pitch in inchs"""
    current_pitch = (2 * np.pi / angle) * (abs(th - tl))
    current_pitch = mm_to_inch(current_pitch)
    return current_pitch


def current_pitch_angle(t_h, t_l, width):
    """ Finds the current pitch of prop"""
    return np.arcsin(abs(t_h - t_l) / width)


def pitch_func(theta, width,  current, added):
    """ Finds pitch of prop in inchs"""
    pitch =  (2 * np.pi / theta) * width * np.tan((current + added))
    pitch = mm_to_inch(pitch)
    return pitch


def pitch_iterate(angle, width, current_pitch):
    """ Iterates through a number of angles that relates to the pitch"""
    added_pitch = 0
    pitch = 0
    while pitch < 12:
        pitch = pitch_func(angle, width, current_pitch, np.deg2rad(added_pitch))
        print(f"The prop pitch with {added_pitch} of added pitch gives: {pitch:.3f} inches")
        added_pitch += 1
        


def main(prop_len_inch, t_h, t_l, width, added_pitch):
    """ main"""
    prop_len_mm = inch_to_mm(prop_len_inch)
    l_75 = l_75_func(prop_len_mm)
    angle = angle_distance(width, l_75)
    current_pitch1 = current_pitch_inch(angle, t_h, t_l)
    current_pitch = current_pitch_angle(t_h, t_l, width)
    pitch = pitch_func(angle, width, current_pitch, added_pitch)
    
    # print(f"prop width angle: {angle} rads")
    # print(f"nominal current pitch: {np.rad2deg(current_pitch)} degrees")
    # # print(f"The current pitch in inchs is {current_pitch1}")
    # print(f"Current pitch: {pitch} inch")
    pitch_iterate(angle, width, current_pitch)
    
# main(15.2, 13.50, 10.42, 23.45, np.deg2rad(0)) # for 15.2 inch prop
# main(16.2, 14.40, 11.2, 24.83, 0) # for 16.2 inch prop
main(18.2, 10.77, 14.750, 29.50, 0)

    
    