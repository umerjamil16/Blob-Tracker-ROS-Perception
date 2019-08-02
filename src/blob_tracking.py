#!/usr/bin/env python
import rospy
from cmvision.msg import Blobs, Blob
from geometry_msgs.msg import Twist

turn =0.0
blob_pos_x = 0

def blobs_callback(data):
    global turn
    global blob_pos_x

    if len(data.blobs):
        for obj in data.blobs:
            if obj.name == 'RedBall':
                rospy.loginfo("Blob <" + str(obj.name) + "> Detected!")
                blob_pos_x = obj.x
                rospy.loginfo("Blob is at %s"%blob_pos_x)

                if blob_pos_x < 180:
                    rospy.loginfo("Turn LEFT")
                    turn = 0.1
                elif blob_pos_x > 220:
                    rospy.loginfo("Turn RIGHT")
                    turn = -0.1
                elif (blob_pos_x < 220 and blob_pos_x > 180):
                    rospy.loginfo("CENTERED")
                    turn = 0.0
    else:
        turn = 0.0



def main_script():
    rospy.init_node("track_blob_color_node", log_level=rospy.WARN)
    rospy.loginfo("in main_script node")
    global turn
    global blob_pos_x

    rospy.Subscriber("/blobs", Blobs, blobs_callback)
    pub = rospy.Publisher("/mira/commands/velocity", Twist, queue_size = 1.0)

    twist = Twist()

    while not rospy.is_shutdown():
        if (turn != 0):
            rospy.loginfo("Turning %s"%turn)
            twist.linear.x = 0
            twist.linear.y = 0
            twist.linear.z = 0
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = turn
            turn = 0
        else:
            rospy.loginfo("Straight %s"%turn)
            twist.linear.x = 0
            twist.linear.y = 0
            twist.linear.z = 0
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = turn
            turn = 0

        pub.publish(twist)
        blob_pos_x = 0
        rospy.sleep(0.1)



if __name__ == '__main__':
    try:
        main_script()
    except rospy.ROSInterruptException: pass