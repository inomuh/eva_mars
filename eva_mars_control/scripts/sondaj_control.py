#!/usr/bin/env python3
import rospy
import time
from std_msgs.msg import Float64

control_param = True
def sondaj_control():

    global control_param
    pub_sondaj = rospy.Publisher('eva_mars/sondaj_joint_position_controller/command', Float64, queue_size=10)
    pub_sondaj2 = rospy.Publisher('eva_mars/sondaj2_joint_position_controller/command', Float64, queue_size=10)
    pub_sondaj3 = rospy.Publisher('eva_mars/sondaj3_joint_position_controller/command', Float64, queue_size=10)
    pub_camport = rospy.Publisher('eva_mars/camera_port_joint_position_controller/command', Float64, queue_size=10)
    
    rospy.init_node('sondaj_control')
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        control_str = input("For Drilling, click 'd' button. For end drilling, click 'e'. For camera control screen click 'c'. For exit, click 'x' ")
        if not control_str == "c":
            if control_param:
                if control_str == "d":
                    rospy.loginfo("Drilling...")
                    pub_sondaj.publish(float(-0.04))
                    rate.sleep()
                    pub_sondaj2.publish(float(-0.10))
                    rate.sleep()
                    pub_sondaj3.publish(float(-0.24))
                    control_param = False
                elif control_str == "x":
                    rospy.loginfo("Terminated..")
                    break
                else:
                    rospy.loginfo("You cannot end before starting!")
                rate.sleep()
            else:
                if control_str == "e":
                    rospy.loginfo("Finishing...")
                    pub_sondaj3.publish(float(0.0))
                    rate.sleep()
                    pub_sondaj2.publish(float(0.0))
                    rate.sleep()
                    pub_sondaj.publish(float(0.0))
                    control_param = True
                elif control_str == "x":
                    rospy.loginfo("Terminated..")
                    break
                else:
                    rospy.loginfo("You cannot start, before ending!")
                rate.sleep()
        else:
            cam_control_str = input("Camera Control Screen. Left Move : 'l', Right Move : 'r', Start Pos: 's'. For exit, click 'x'")
            if cam_control_str == "l":
                    rospy.loginfo("Turning Left...")
                    pub_camport.publish(float(0.6))
            elif cam_control_str == "r":
                    rospy.loginfo("Turning Right...")
                    pub_camport.publish(float(-0.6))
            elif cam_control_str == "s":
                    rospy.loginfo("Returning the start position..")
                    pub_camport.publish(float(0.0))
            elif cam_control_str == "x":
                    rospy.loginfo("Terminated")
                    break
            else:
                rospy.loginfo("Please enter exeptable command !")
                break                               

        rate.sleep()


if __name__ == '__main__':
    try:
        sondaj_control()
    except rospy.ROSInterruptException:
        pass
