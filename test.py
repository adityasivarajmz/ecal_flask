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
from imu_data import Imu

import ecal.core.core as ecal_core
from ecal.core.publisher import StringPublisher

#Declare a Flask function.
ecalApp = Flask(__name__)

@ecalApp.route('/ecal_data', methods = ['POST'])
def index():

    #eCAL subscriber
    sub = ecal_core.subscriber("imu")

    #receive data from eCAL topic
    msg = sub.receive(1000)

    #convert the received message to a dictionary
    data = {"value": msg.Imu}
    print(data)


if __name__ == "__main__":

  #Initialize eCAL API.
  ecal_core.initialize(sys.argv, "Python Hello World Publisher")

  #Run the Flask applet.
  ecalApp.run(debug = True)

  #Finalize eCAL API
  ecal_core.finalize()