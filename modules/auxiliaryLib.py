#!/usr/bin/python

import numpy as np

def normalisedDesiredDirection(rk, r):
    '''Returns the normalized vector from the current position r to the desired direction rk'''
    return (rk - r) / np.linalg.norm(rk - r)

def attractiveForceToDestination(velocity, desiredVelocity, position, target):
    '''Returns the attractive force to a destination'''
    # define the desired direction
    eAlpha  = normalisedDesiredDirection(target, position)
    # define the desired velocity
    vAlpha0 = eAlpha * desiredVelocity
    # relaxation time [s]
    tauAlpha = 0.5

    return (vAlpha0 - velocity) / tauAlpha