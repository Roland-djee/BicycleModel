#!/usr/bin/python

from math import *
import numpy as np

# from modules import controllers

class bicycle:
    def __init__(self):
        # Bicycle constants
        self.frontWheelLength   = 1.        #[m]
        self.backWheelLength    = 1.        #[m]
        self.backWheelAngle     = 0.        #[rads]
        self.wheelRadius        = 0.5       #[m]
        self.frontWheelCorneringStiffness = 1.
        self.backWheelCorneringStiffness  = 1.
        self.mass               = 1.        # [kg]
        self.inertialMomentum   = 1.
        self.backWheelForceInX  = 1.
        self.backWheelForceInY  = 1.
        self.frontWheelForceInY = 1.
        
        # Variables
        self.psiDotDot          = 0.
        self.psiDot             = 0.
        self.psi                = 0.
        self.position           = np.array([-10., 5.])
        self.velocity           = np.array([0.5, 0.])
        self.desiredVelocity    = 2.5
        self.target             = np.array([20., 20.])
        self.frontWheelAngle    = np.pi/10. #[rads]
        self.frontWheelPosition  = np.array([0., 0.])
        self.backWheelPosition   = np.array([0., 0.]) 
        self.frontOfFrontWheelPosition  = np.array([0., 0.])
        self.backOfFrontWheelPosition   = np.array([0., 0.]) 
        
        # Controller variables 
        self.set_of_controllers = {"PID": "PID", "HMC": "HMC"}
        
        
    def preferred_controller(self, controller):
        return self.set_of_controlers[controller]
            
    def updateFrontOfFrontWheelPosition(self, newPosition):
        self.frontOfFrontWheelPosition = newPosition    
    
    def getFrontOfFrontWheelX(self):
        return self.frontOfFrontWheelPosition[0]
    
    def getFrontOfFrontWheelY(self):
        return self.frontOfFrontWheelPosition[1]
    
    def updateBackOfFrontWheelPosition(self, newPosition):
        self.backOfFrontWheelPosition = newPosition    
    
    def getBackOfFrontWheelX(self):
        return self.backOfFrontWheelPosition[0]
    
    def getBackOfFrontWheelY(self):
        return self.backOfFrontWheelPosition[1]    
        
    def updateBackWheelPosition(self, newPosition):
        self.backWheelPosition = newPosition    
    
    def getBackWheelX(self):
        return self.backWheelPosition[0]
    
    def getBackWheelY(self):
        return self.backWheelPosition[1]
        
    def updateFrontWheelPosition(self, newPosition):
        self.frontWheelPosition = newPosition    
    
    def getFrontWheelX(self):
        return self.frontWheelPosition[0]
    
    def getFrontWheelY(self):
        return self.frontWheelPosition[1]
        
    def getTargetX(self):
        return self.target[0]
    
    def getTargetY(self):
        return self.target[1]
        
    def updateTarget(self, newTarget):
        self.target = newTarget
        
    def updateYaw(self, newYaw):
        self.psi = newYaw
        
    def updateYawDot(self, newYawDot):
        self.psiDot = newYawDot
               
    def updateYawDotDot(self, newYawDotDot):
        self.psiDotDot = newYawDotDot
    
    def getVelocityX(self):
        return self.velocity[0]
    
    def getVelocityY(self):
        return self.velocity[1]
        
    def updateVelocity(self, newVelocity):
        self.velocity = newVelocity
           
    def getPositionX(self):
        return self.position[0]
    
    def getPositionY(self):
        return self.position[1]
        
    def updatePosition(self, newPosition):
        self.position = newPosition 
        
    def updateFrontWheelAngle(self, newFrontWheelAngle):
        self.frontWheelAngle = newFrontWheelAngle
