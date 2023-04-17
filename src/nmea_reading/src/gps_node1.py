#!/usr/bin/env python3

import rospy
import serial

from sensor_msgs.msg import NavSatFix

def gps_node():
    # Initialize ROS node and publisher
    rospy.init_node('gps_node', anonymous=True)
    pub = rospy.Publisher('/gps', NavSatFix, queue_size=10)

    # Open serial port to read GPS data
    ser = serial.Serial('/dev/ttyACM0', 9600)

    # Open file to write GPS data
    file = open('/home/tranhieu/catkin_ws/gps_data.txt', 'w')

    # Loop to read and process GPS data
    while not rospy.is_shutdown():
        line = ser.readline().decode('ISO-8859-1')
        fields = line.split(',')
        if fields[0] == '$GNGGA':
            # Extract latitude, longitude, and altitude from GPS data
            latitude = float(fields[2][:2]) + float(fields[2][2:]) / 60.0
            if fields[3] == 'S':
                latitude = -latitude
            longitude = float(fields[4][:3]) + float(fields[4][3:]) / 60.0
            if fields[5] == 'W':
                longitude = -longitude
            altitude = float(fields[9])
            
            # Publish GPS data as a NavSatFix message
            msg = NavSatFix()
            msg.latitude = latitude
            msg.longitude = longitude
            msg.altitude = altitude
            pub.publish(msg)

            # Write GPS data to file
            rospy.loginfo(msg)
            file.write(line)

    # Close serial port and file
    ser.close()
    file.close()

if __name__ == '__main__':
    try:
        gps_node()
    except rospy.ROSInterruptException:
        pass
