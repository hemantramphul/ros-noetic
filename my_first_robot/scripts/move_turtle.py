#!/usr/bin/env python3
"""Drive the turtlesim turtle in a circle.

Publishes speed commands on /turtle1/cmd_vel, 10 times per second.
"""
import rospy
from geometry_msgs.msg import Twist


def main():
    rospy.init_node("move_turtle")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10 messages per second

    cmd = Twist()
    cmd.linear.x = 2.0   # forward speed
    cmd.angular.z = 1.0  # turning speed (makes it a circle)

    rospy.loginfo("Driving the turtle in a circle. Press Ctrl+C to stop.")
    while not rospy.is_shutdown():
        pub.publish(cmd)
        rate.sleep()


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
