# Semantic SLAM for Search and Rescue Mobile Robot (Robot side node)
for laptop side node see (https://github.com/roiksa/SLAM)

Based on 
- ORBSLAM3 Ros wrapper by thien94 (https://github.com/thien94/orb_slam3_ros)
- Yolov8 ROS by Alpaca-zip (https://github.com/Alpaca-zip/ultralytics_ros)

## Install

```
cd ~/catkin_ws/src
git clone https://github.com/roiksa/SLAM-robot.git
cd ~/catkin_ws
catkin build
```

## How to use
On laptop side
```
cd ~/catkin_ws
source devel/setup.bash
roslaunch orb_slam3_ros robot.launch
```
On the robot
```
roslaunch proto2 start.launch
```
