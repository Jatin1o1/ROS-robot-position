#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
import time
a=b=c= 0.0

def subs(msg):
    
    a = msg.pose.pose.position.x
    b = msg.pose.pose.position.y
    c = msg.pose.pose.position.z
    d = msg.pose.pose.orientation.x
    e = msg.pose.pose.orientation.y
    f = msg.pose.pose.orientation.z
    g = msg.pose.pose.orientation.w
    
    #h = open("demo.txt", "w")
    h = open("/home/jatin/catkin_ws/src/move_tb3/src/final/demo.txt", "w")
    
    l= str(a).strip('-')+ "\n" +str(b).strip('-')+ "\n" +str(c).strip('-')+ "\n" +str(d).strip('-')+ "\n" +str(e).strip('-')+ "\n" +str(f).strip('-')+ "\n" +str(g).strip('-')
    print(l + "\n")

    h.write(str(l))
    h.close()
    #print a
    #print b
    #print c
    
    time.sleep(2)
    
rospy.init_node('check_odometry')
odom_sub = rospy.Subscriber('/odom', Odometry, subs)

rospy.spin()
