# ROS-robot-position
bare minimum code for saving the last position of a robot and re-spawning the robot back at that position.

PosefilePub = publisher file publishing the " initial position " of a robot using geometry_msgs.msg, PoseWithCovarianceStamped.

PoseSaveSubs = subscribe node, subscribing toh the odomotery parameters and saving them in a file.
      it subscribe odometry in navigation msgs nav_msgs.msg import.
