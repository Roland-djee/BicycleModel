#!/usr/bin/python

import numpy as np

def normalisedDesiredDirection(rk, r):
    '''Returns the normalized vector from the current position r to the desired direction rk'''
    return (rk - r) / np.linalg.norm(rk - r)

def attractiveForceToDestination(velocity, desiredVelocity, position, target):
    '''Returns the attractive force to a destination'''
    eAlpha  = normalisedDesiredDirection(target, position)
    vAlpha0 = eAlpha* desiredVelocity
    tauAlpha = 1.
    return (vAlpha0 - velocity) / tauAlpha