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

class GPSStatus(Structure):
    _fields_ = [("STATUS_NO_FIX", c_uint16),
                ("STATUS_FIX", c_uint16),
                ("STATUS_SBAS_FIX", c_uint16),
                ("STATUS_GBAS_FIX", c_uint16),
                ("STATUS_DGPS_FIX", c_uint16),
                ("STATUS_WAAS_FIX", c_uint16),
                ("SOURCE_NONE", c_uint16),
                ("SOURCE_GPS", c_uint16),
                ("SOURCE_POINTS", c_uint16),
                ("SOURCE_DOPPLER", c_uint16),
                ("SOURCE_ALTIMETER", c_uint16),
                ("SOURCE_MAGNETIC", c_uint16),
                ("SOURCE_GYRO", c_uint16),
                ("SOURCE_ACCEL", c_uint16),
                ("header", Header),
                ("sattelites_used", c_uint16),
                # ("sattelites_used_prn", POINTER(c_int32*100)),
                ("satellites_visible", c_uint16),
                # ("sattelites_visible_prn", POINTER(c_int32*100)),
                # ("sattelites_visible_z", POINTER(c_int32*100)),
                # ("sattelites_visible_azimuth", POINTER(c_int32*100)),
                # ("sattelites_visible_snr", POINTER(c_int32*100)),
                ("status", c_int16),
                ("motion_source", c_uint16),
                ("orientation_cource", c_uint16),
                ("position_source", c_uint16)]
# status = GPSStatus()
    
class GPSFix(Structure):
    _fields_ = [("COVARIANCE_TYPE_UNKNOWN", c_uint16),
                ("COVARIANCE_TYPE_APPROXIMATED", c_uint16),
                ("COVARIANCE_TYPE_DIAGONAL_KNOWN", c_uint16),
                ("COVARIANCE_TYPE_KNOWN", c_uint16),
                ("header", Header),
                ("status", GPSStatus),
                ("latitude", c_longdouble),
                ("longitude", c_longdouble),
                ("altitude", c_longdouble),
                ("track", c_longdouble),
                ("speed", c_longdouble),
                ("climb", c_longdouble),
                ("pitch", c_longdouble),
                ("roll", c_longdouble),
                ("dip", c_longdouble),
                ("time", c_longdouble),
                ("gdop", c_longdouble),
                ("pdop", c_longdouble),
                ("hdop", c_longdouble),
                ("vdop", c_longdouble),
                ("tdop", c_longdouble),
                ("err", c_longdouble),
                ("err_horz", c_longdouble),
                ("err_vert", c_longdouble),
                ("err_track", c_longdouble),
                ("err_speed", c_longdouble),
                ("err_climb", c_longdouble),
                ("err_time", c_longdouble),
                ("err_pitch", c_longdouble),
                ("err_roll", c_longdouble),
                ("err_dip", c_longdouble),
                ("position_covariance", POINTER(c_double*9)),
                ("position_covariance_type", c_uint8)]