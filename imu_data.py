#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Clone of the C++ message structure of the same name. This clone will be used for Flask Server.
"""

from ctypes import *


class Header(Structure):
    _fields_ = [("time", c_longdouble),
                ("frame_id", c_char_p)]
    
# header = Header();

class Quaternion(Structure):
    _fields_ = [("x", c_longdouble),
                ("y", c_longdouble),
                ("z", c_longdouble),
                ("w", c_longdouble)]
    
# orientation = Quaternion()

class Vector3(Structure):
    _fields_ = [("x", c_longdouble),
                ("y", c_longdouble),
                ("z", c_longdouble)]
    
# angular_velocity = Vector3()
# linear_acceleration = Vector3()

class Imu(Structure):
    _fields_ = [("header", Header),
                ("orientation", Quaternion),
                ("orientation_covariance", POINTER(c_double*9)),
                ("angular_velocity", Vector3),
                ("angular_velocity_covariance", POINTER(c_double*9)),
                ("linear_acceleration", Vector3),
                ("linear_acceleration_covariance", POINTER(c_double*9))]