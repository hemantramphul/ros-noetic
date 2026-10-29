#!/usr/bin/env python3
"""Print where the turtlesim turtle is.

Listens on /turtle1/pose and prints the position once per second.
"""
import rospy
from turtlesim.msg import Pose


def on_pose(pose):
    # Called every time a new position arrives (about 60 times per second).
    # loginfo_throttle prints at most once per second so the screen stays readable.
    rospy.loginfo_throttle(1, "x=%.2f  y=%.2f  angle=%.2f" % (pose.x, pose.y, pose.theta))


def main():
    rospy.init_node("watch_turtle")
    rospy.Subscriber("/turtle1/pose", Pose, on_pose)
    rospy.loginfo("Watching the turtle. Press Ctrl+C to stop.")
    rospy.spin()  # keep running and wait for messages


if __name__ == "__main__":
    main()
