#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    
    print(data.data,end="")
    #printing messages in the same line after the listener program ends
    
def listener():
    print()
    rospy.init_node('listener', anonymous=True)
    #initialising node listener

    rospy.Subscriber("team_abhiyaan",String,callback)
    
    rospy.Subscriber("autonomy",String,callback)
    #Subscribing to topics team_abhiyaan and autonomy
    rospy.spin()
if __name__=='__main__':
   listener()
   
