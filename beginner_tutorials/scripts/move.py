#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt ,sin ,cos
    
    
class TurtleBot:
    def __init__(self):
       rospy.init_node('bot', anonymous=True)
          
    def O(self):
       self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',
                                                     Twist, queue_size=10)
   
       self.pose_subscriber = rospy.Subscriber('/turtle1/pose',
                                                   Pose, self.update_pose)
       
       self.pose = Pose()
       #Function for Turtle1 (stationary one)
       self.rate = rospy.Rate(10)
    def T(self):
       self.velocity_publisher = rospy.Publisher('/turtle2/cmd_vel',
                                                     Twist, queue_size=10)
   
       self.pose_subscriber = rospy.Subscriber('/turtle2/pose',
                                                   Pose, self.update_pose)
       #Pose contains attributes of Turtle object
       self.pose = Pose()
       #Function for Turtle2(moving one)
       self.rate = rospy.Rate(10)
    def update_pose(self, data):
       # To update pose
       self.pose = data
       self.pose.x = round(self.pose.x, 4)
       self.pose.y = round(self.pose.y, 4)
   
    def distance(self,T1):
       
       q=T1.pose.x-self.pose.x
       p=T1.pose.y-self.pose.y
           
       return (sqrt(pow((q), 2) +pow((p), 2)))
   
       #Geometric distance between both turtles
   
    def angle(self, T1):
        return atan2(T1.pose.y - self.pose.y, T1.pose.x - self.pose.x)
   
       #Angle between both turtles
    def move2goal(self,T1):
        pose = Pose()
        vel_msg = Twist()
        
        for i in range(1):
            w=self.distance(T1)
            self.rate.sleep()
        
        #pose for turtle2 needs to update once for a recently spawned turtle
        while self.distance(T1) > 2.00:
   
               
            #Turtle2 moves with speed of 1 in x direction
            vel_msg.linear.x = 1.0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
   
            vel_msg.angular.x = 0
            vel_msg.angular.z = 0
            vel_msg.angular.y = 0
            
              
            #Publishing velocity to topic /turtle1/cmd_vel
            self.velocity_publisher.publish(vel_msg)
   
               
            self.rate.sleep()
   
           
        vel_msg.linear.x = 0
        vel_msg.angular.z=0
        #Reset velocity
        self.velocity_publisher.publish(vel_msg)
        
        while self.angle(T1)<=1.57:
            vel_msg.linear.x=-2.0*sin(self.angle(T1))
            vel_msg.linear.y=2.0*cos(self.angle(T1))
            # x=-rsinQ , y-=rcosQ for circular motion
            vel_msg.linear.z=0
            vel_msg.angular.x=0
            vel_msg.angular.y=0
            vel_msg.angular.z=0 
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
        
        vel_msg.linear.x=0
        vel_msg.linear.y=0
        self.velocity_publisher.publish(vel_msg)
        #Safe distance is 3.5 from turtle1
        while self.distance(T1)<3.5:
            vel_msg.linear.x=1
            vel_msg.linear.y=0
            vel_msg.linear.z=0
            vel_msg.angular.x=0
            vel_msg.angular.y=0
            vel_msg.angular.z=0
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
        vel_msg.linear.x=0
        self.velocity_publisher.publish(vel_msg)    
        rospy.spin()
       
if __name__ == '__main__':
   try:
       T1 = TurtleBot()
       T2 = TurtleBot()
       #Each turtle is represented by an object. This is more suitable
       #for situations where both turtles are moving.
       T1.O()
       #Establishing publisher and subscriber for both objects (different topics)
       T2.T()
       
       T2.move2goal(T1)
   except rospy.ROSInterruptException:
       pass

