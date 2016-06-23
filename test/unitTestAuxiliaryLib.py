'''
Created on 30 Mar 2016

@author: RolandGuichard
'''
import unittest

import numpy as np
# import sys
# sys.path.append('../src/')
# import bicycleKinematics

# from src.bicycleDynamics import *
#from modules.mathlib import *

from modules.auxiliaryLib import *

#import src.bicycle as bicycle

class Test(unittest.TestCase):

    def testNormalisedDesiredDirection(self):
        target   = np.array([10., 10., 10.])
        position = np.array([1., 1., 1.])       
        expectedNormalisedDirection = np.array([1., 1., 1.])
        returnedNormalisedDirection = normalisedDesiredDirection(target, position)
        errorMessage = "Wrong value for normalised direction vector."
        self.assertEqual(returnedNormalisedDirection.all(), expectedNormalisedDirection.all(), errorMessage)  
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNormalisedDesiredDirection']
    unittest.main()