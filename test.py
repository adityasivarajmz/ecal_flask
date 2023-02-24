#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 12:17:55 2023

@author: AdityaSivaraj
"""
import sys

import time
from flask import Flask
import numpy as np
import matplotlib as mtb
from ctypes import *

import imu_data
from imu_data import Imu, Quaternion, Vector3, Header

import ecal.core.core as ecal_core
from ecal.core.publisher import StringPublisher

#Declare a Flask function.
ecalApp = Flask(__name__)

@ecalApp.route('/ecaldata')
def index():

    #eCAL subscriber
    sub = ecal_core.subscriber("imu/data")

    #receive data from eCAL topic
    msg = sub.receive(1000)

    #convert the received message to a dictionary
    
    print(msg)

    imu = Imu()
    header = Header()
    orientation = Quaternion()
    linear_acceleration = Vector3()
    angular_velocity = Vector3()

    header.ts = time.time()
    header.frame_id = "imu/data"

    orientation.x = 0.0
    orientation.y = 0.0
    orientation.z = 0.0
    orientation.w = 1.0
    orientation_covariance = (c_double * 9)(1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0)

    linear_acceleration.x = 0.0
    linear_acceleration.y = 0.0
    linear_acceleration.z = 0.0
    linear_acceleration_covariance = (c_double * 9)(1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0)

    angular_velocity.x = 0.0
    angular_velocity.y = 0.0
    angular_velocity.z = 0.0
    angular_velocity_covariance = (c_double * 9)(1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0)

    imu.header = header
    imu.orientation = orientation
    imu.orientation_covariance = orientation_covariance #(c_double * 9)(1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0)
    imu.angular_velocity = angular_velocity
    imu.angular_velocity_covariance = linear_acceleration_covariance #(c_double * 9)(1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0)
    imu.linear_acceleration = linear_acceleration
    imu.linear_acceleration_covariance = angular_velocity_covariance #(c_double * 9)(1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0)
    
    return f'{imu.header.frame_id}'


if __name__ == "__main__":

  #Initialize eCAL API.
  ecal_core.initialize(sys.argv, "Python Hello World Publisher")

  #Run the Flask applet.
  ecalApp.run(debug = True)

  #Finalize eCAL API
  ecal_core.finalize()