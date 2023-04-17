#!/usr/bin/env python3

import rospy
import serial
from serial import SerialException

if __name__ == '__main__':
    rospy.init_node('gps_node')
    port = '/dev/ttyACM0'
    baudrate = 9600

    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        rospy.loginfo("Serial port {} initialized.".format(port))
    except serial.SerialException as e:
        rospy.logerr("Unable to open port {}: {}".format(port, e))
        rospy.signal_shutdown("Unable to open serial port")

    while not rospy.is_shutdown():
        nmea_message = ser.readline().strip()
        rospy.loginfo("Received NMEA message: {}".format(nmea_message))