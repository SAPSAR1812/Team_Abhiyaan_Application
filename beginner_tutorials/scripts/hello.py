#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def hello():
       pub=rospy.Publisher("team_abhiyaan",String,queue_size=10)
       rospy.init_node('hello',anonymous=True)
       #rate = rospy.Rate(10)

       msg=String()
       msg.data="Team Abhiyaan:"
       
       rospy.loginfo(msg)
       pub.publish(msg)
       #rate.sleep()
if __name__=='__main__':
   try:
      hello()
   except rospy.ROSInterruptException:
      pass
