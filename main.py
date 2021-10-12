#!/usr/bin/env python
from niryo_one_python_api.niryo_one_api import *
import rospy
import time

rospy.init_node('niryo_one_example_python_api')

#    print "--- Start"
n = NiryoOne()

#  try:
    # Calibration robot first
#    n.calibrate_auto()
    # n.calibrate_auto()
#    print "Calibration finished !\n"

#    time.sleep(1)

    #Test learning mode
#    n.activate_learning_mode(False)
#    print "Learning mode activated? "
#    print n.get_learning_mode()

    # Move
#    n.set_arm_max_velocity(30)



    #Preperation moves before Rock,Paper,Scissors
def initarm():
    n.move_joints([0.052, -0.449, -0.813, 0.028, 0.112, 0.116])
    n.move_joints([-0.055, -0.245, -0.358, 0.028, 0.108, 0.116])

    #Rock
def rock():
    n.move_joints([0.056,-0.553,-0.34,0.032,0.925,1.599])

    #Sax
def sax():
    n.move_joints([0.057, -0.5, -0.371, 0.032, 0.911, 2.374])

    #Paper
def paper():
    n.move_joints([0.063, -0.47, -0.38, 0.032, 0.885, -0.299])

position='rock'

initArm()
def f(position):
    match position:
        case 'rock':
            rock()
        case 'paper':
            sax()
        case 'paper':
            paper()

f(position)
    #Robot positions
    saved_positions = n.get_saved_position_list()
    print "\n  Saved positions: "
    print saved_positions

    #Others
    print "\n Hardware status: "
    print n.get_hardware_status()

    n.activate_learning_mode(True)

except NiryoOneException as e:
    print e
    # Handle errors here
