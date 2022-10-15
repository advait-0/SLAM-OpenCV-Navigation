#!/usr/bin/env python3
# -- coding: utf-8 --
import rospy
from sensor_msgs.msg import Image
from sensor_msgs.msg import LaserScan
from darknet_ros_msgs.msg import BoundingBoxes
from std_msgs.msg import Header
from std_msgs.msg import String
from geometry_msgs.msg import Twist

     
def yolo_readings(msg):
     for box in msg.bounding_boxes:
    
        parts = {
          'xmin': (box.xmin),
          'xmax': (box.xmax),
          'ymin': (box.ymin),
          'ymax': (box.ymax)
                }
        objname=box.Class
        logic(parts)
pub = None


# def yolo_readings(msg):
#     parts = {
#         'xmin': (msg.bounding_boxes.box[0].xmin),
#         'xmax': (msg.bounding_boxes.box[0].xmax),
#         'ymin': (msg.bounding_boxes.box[0].ymin),
#         'ymax': (msg.bounding_boxes.box[0].ymax)
#     }
#     rospy.loginfo(parts)
#     logic(parts)


def logic(parts):
  linear_speed_x = 0
  angular_speed_z = 0
  msg = Twist()
  height=480
  width=640
  mid_x = (parts['xmax']-parts['xmin'])/2 + parts['xmin']
  mid_y = (parts['ymax']-parts['ymin'])/2 + parts['ymin']
  yolo_width=parts['xmax']-parts['xmin']
  yolo_height=parts['ymax']-parts['ymin']
  # box_area = (2 * 3.14 * 180) / (((yolo_width + yolo_height) * 360) * 1000) + 3
  box_area=yolo_height*yolo_width
  # box_area=cv_image[mid_x,mid_y]
  rospy.loginfo(box_area)
  init_dist = 1.0000058691588785
#   if objname == False:
#       angular_speed_z = -prev_angular_speed
#       linear_speed_x=0
  if mid_x>width/2:
      angular_speed_z = -0.5
    #   prev_angular_speed=angular_speed_z
    #   prev_linear_speed=linear_speed_x
      
      if box_area > 50000:
          linear_speed_x = 0.5
        #   prev_angular_speed = angular_speed_z
      
      elif box_area <= 50000:
          linear_speed_x = 0
          angular_speed_z = 0
        #   prev_angular_speed = angular_speed_z
      
      elif box_area == 50000:
          linear_speed_x = 0
          angular_speed_z = 0
        #   prev_angular_speed = angular_speed_z

  elif mid_x < width/2:
      angular_speed_z=0.5
    #   prev_angular_speed = angular_speed_z
      
      if box_area > 50000:
          linear_speed_x = 0.5
          
      elif box_area <= 50000:
          linear_speed_x = 0
          angular_speed_z = 0
      
      elif box_area == 50000:
          linear_speed_x = 0
          angular_speed_z = 0

  else:
      rospy.loginfo(parts)

  msg.linear.x = linear_speed_x
  msg.angular.z = angular_speed_z
  rospy.loginfo(linear_speed_x)
  rospy.loginfo(angular_speed_z)
  pub.publish(msg)


def main():
    global pub
    rospy.init_node('obj_following')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    sub = rospy.Subscriber("/darknet_ros/bounding_boxes", BoundingBoxes, yolo_readings)
    # sub1 = rospy.Subscriber('/camera/depth/image_raw', Image,logic)
    rospy.spin()


if __name__ == '__main__':
  main()
