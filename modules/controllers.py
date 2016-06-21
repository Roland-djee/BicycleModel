#!/usr/bin/python


def PIDController(angle, setAngle, integral, previous_error, dt):
    """ Defines the Proportional-Integral-derivative controller behaviour
    to modify the steering angle to target.
    """
    Kp = 1.
    Ki = 1.
    Kd = 1.
    error = setAngle - angle
    integral = integral + error * dt
    derivative = (error - previous_error)
    output = Kp * error + Ki * integral + Kd * derivative
    previous_error = error
    return output, integral, previous_error
    
    