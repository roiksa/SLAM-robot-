import io
from sensor_msgs.msg import CompressedImage
from picamera import PiCamera
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
  rate = rospy.Rate(30) # 15hz

  #Camera initialization
  camera = PiCamera()
  camera.framerate = 15
  camera.resolution = (640, 480)
  # Object for captured frame
  frame = io.BytesIO()
  frameMsg = CompressedImage()
  frameMsg.height = 480
  frameMsg.width = 640
  frameMsg.encoding = 'rgb8'
  frameMsg.format = 'jpeg'
  frameMsg.step = 1920
  id = 1
  start = time.time()
 
 
  # While ROS is still running.
  while not rospy.is_shutdown():
     
      # Capture frame-by-frame
      # This method returns True/False as well
      # as the video frame.
      #start = time.time()
      camera.capture(frame,format='rgb', use_video_port=True)
      stamp = rospy.Time.now()
      id = id+1
      img = np.array(frame.getvalue())
      #end = time.time()
      #print('Time for image capture: ', end-start)
         
      if  (img):
        #Print debugging information to the terminal
        #rospy.loginfo('[%s]publishing video frame-%s',stamp, id)
        frameMsg.data = cv2.imencode()
        frameMsg.header.stamp = stamp
        # Publish the image.
        print('fps: ',id/ (time.time()-start))
        pub.publish(frameMsg)
      else :
        rospy.loginfo('Camera Error')
                   
      # Sleep just enough to maintain the desired rate
      #start = time.time()      
      frame.truncate(0)
      frame.seek(0)
      rate.sleep()
      #end = time.time()
      #print('Time for frame clean: ', end-start)

         
if __name__ == '__main__':
  try:
    publish_message()
  except rospy.ROSInterruptException:
    pass
