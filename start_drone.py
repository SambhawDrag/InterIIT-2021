#!/usr/bin/env python

from __future__ import print_function
import sys
import rospy
from mavros_msgs.srv import *
from mavros_msgs.msg import *
import time

print("Hi")

def mode_client():
    rospy.wait_for_service('/mavros/set_mode')
    try:
        print("Trying")
        set_mode = rospy.ServiceProxy('/mavros/set_mode', SetMode)
        resp1 = set_mode(0, "Guided")
        return resp1
    except rospy.ServiceException as e:
        print("Service call mode_client failed: %s" %e)

def arm_client():
    rospy.wait_for_service('/mavros/cmd/arming')
    try:
        print("Trying")
        arming = rospy.ServiceProxy('/mavros/cmd/arming', CommandBool)
        resp1 = arming(True)
        return resp1
    except rospy.ServiceException as e:
        print("Service call arm_client failed: %s" %e)

print("\nTaking off")
def takeoff_client():
    rospy.wait_for_service('/mavros/cmd/takeoff')
    try:
        print("Trying")
        takeoff_cl = rospy.ServiceProxy('/mavros/cmd/takeoff', CommandTOL)
        response = takeoff_cl(altitude=10, latitude=0, longitude=0, min_pitch=0, yaw=0)
        rospy.loginfo(response)
    except rospy.ServiceException as e:
        print("Service call takeoff_client failed: %s" %e)

print("\nHovering...")
time.sleep(5)

rospy.init_node('boot_up', anonymous=True)
print(mode_client())
print(arm_client())
print(takeoff_client())