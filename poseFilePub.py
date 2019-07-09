#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from nav_msgs.msg import Odometry


f =open("demo.txt")
values = [float(x.strip('-')) for x in f]


def publish():
    rospy.init_node('jatin',anonymous=True)
    pub=rospy.Publisher('/initialpose',PoseWithCovarianceStamped,queue_size =1)

    move=PoseWithCovarianceStamped()

    move.header.frame_id="map"
    #move.header.stamp=rospy.Time.now()
    
    move.pose.pose.position.x=values[0]
    move.pose.pose.position.y=values[1]
    move.pose.pose.position.z=values[2]

    move.pose.pose.orientation.x=0.0
    move.pose.pose.orientation.y=0.0
    move.pose.pose.orientation.z=0.0
    move.pose.pose.orientation.w=1.0
    while not rospy.is_shutdown():
       connections = pub.get_num_connections()
       rospy.loginfo('Connections: %d', connections)
       if connections > 0:
           pub.publish(move)
           print "published"
           break
publish()



