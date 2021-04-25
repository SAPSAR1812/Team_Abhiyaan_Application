#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def hello1():
       pub=rospy.Publisher("autonomy",String,queue_size=10)
       rospy.init_node('hello1',anonymous=True)
       #rate = rospy.Rate(10)

       msg=String()
       msg.data="fueled by autonomy."
       
       rospy.loginfo(msg)
       pub.publish(msg)
       #rate.sleep()
if __name__=='__main__':
   try:
      hello1()
   except rospy.ROSInterruptException:
      pass
