'''
*****************************************************************************************
*
*  ===============================================
*     Niti Vahan (NV) Theme of eYRC 2026-27
*  ===============================================
*
*  This script is intended for implementation of Task 1A of Niti Vahan (NV) Theme.
*
*  Filename:         NV_Task1A.py
*  Created:          2026
*  Last Modified:
*  Author:           e-Yantra Team
*
*  You are ONLY allowed to write your code inside the block marked
*  "ADD YOUR IMPLEMENTATION HERE". Do not change anything outside it - the
*  evaluation script relies on the rest of this file staying as it is.
*
*****************************************************************************************
'''

# Team ID:          4863
# Author List:      anand
# Filename:         NV_Task1A.py
# Functions:        ackermann_wheel_angles
# Global variables: < List any global variables you add, "None" if you add none >


####################### IMPORT MODULES #######################
import math
import numpy as np
##############################################################


#################### VEHICLE CONSTANTS #######################
WHEELBASE = 0.120           # L: distance between front and rear axle centrelines
TRACK_WIDTH = 0.110         # W: distance between left and right wheel centre
WHEEL_OFFSET = 0.0275       # O: distance between kingpin axis and wheel centre.
##############################################################


##############################################################
############### ADD YOUR IMPLEMENTATION HERE #################
##############################################################


def ackermann_wheel_angles(delta):
    '''
    Purpose:
    ---
    Convert a single virtual steering angle into the two real front-wheel
    angles, per the Ackermann geometry.

    Input Arguments:
    ---
    `delta` :   [ float ]
        Steering angle of the virtual centred front wheel, in radians.

    Returns:
    ---
    `left_angle`  : [ float ]
    `right_angle` : [ float ]
        The two real front-wheel steering angles, in radians, using the
        same sign convention as delta.

    REMEMBER:
    ---
    WHEEL_OFFSET changes the effective half-track width inside each wheel's triangle.
    '''

    # Straight position
    if abs(delta) < 1e-9:
        left_angle = 0.0
        right_angle = 0.0
        return left_angle, right_angle

    # Effective half-track from vehicle centreline to kingpin axis
    effective_half_track = (TRACK_WIDTH / 2.0) - WHEEL_OFFSET

    # Turning radius of the virtual centred front wheel
    R = WHEELBASE / math.tan(abs(delta))

    # Inside and outside wheel steering angles
    inside_angle = math.atan(
        WHEELBASE / (R - effective_half_track)
    )

    outside_angle = math.atan(
        WHEELBASE / (R + effective_half_track)
    )

    # Positive delta -> left turn
    if delta > 0:
        left_angle = inside_angle
        right_angle = outside_angle

    # Negative delta -> right turn
    else:
        left_angle = -outside_angle
        right_angle = -inside_angle

    return left_angle, right_angle


##############################################################
################ END OF YOUR IMPLEMENTATION ##################
##############################################################


#################### DO NOT EDIT BELOW THIS LINE ####################

if __name__ == "__main__":

    test_angles = np.arange(-0.35, 0.35, 0.05)

    for d in test_angles:
        left, right = ackermann_wheel_angles(d)
        print(f"delta={d}  ->  left={left}, right={right}")
