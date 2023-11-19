from sensor_msgs.msg import CompressedImage
from picamera import PiCamera
from picamera.array import PiRGBArray
import rospy
import time
import cv2
import numpy as np
  
def publish_message():
 
  # Node is publishing to the video_frames topic using 
  # the message type Image
  pub = rospy.Publisher('image', CompressedImage, queue_size=1)
     
  # Tells rospy the name of the node.
  # Anonymous = True makes sure the node has a unique name. Random
  # numbers are added to the end of the name.
  rospy.init_node('robot_pub', anonymous=True)
     
  # Go through the loop 15 times per second
  rate = rospy.Rate(60) # 15hz

  #Camera initialization
  camera = PiCamera()
  camera.framerate = 60
  camera.resolution = (1280, 720)
  # Object for captured frame
  frame = PiRGBArray(camera,size=(1280,720))
  frameMsg = CompressedImage()
  frameMsg.format = 'jpeg'
  id = 0
  start = time.time()

  try:
    for frameCapture in camera.capture_continuous(frame, format = "bgr", use_video_port=True):
      stamp = rospy.Time.now()
      id = id+1
      img = frameCapture.array
      frameMsg.data = np.array(cv2.imencode('.jpg', img)[1]).tostring()
      frameMsg.header.stamp = stamp
      # Publish the image.
      #print(frameMsg)
      #print(frameMsg.data)
      print('fps: ',id/ (time.time()-start))
      pub.publish(frameMsg)
      frame.truncate(0)
      rate.sleep()
     # if KeyboardInterrupt:
     #   print("Process Interrupted")
     #   break
  except KeyboardInterrupt:
    print("Process Interrupted")
    pass

  

         
if __name__ == '__main__':
  publish_message()
