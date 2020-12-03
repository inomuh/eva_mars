# EvaMars Robot 

Robot Information
-----------------
The EvaMars robot is a Mars reconnaissance robot model developed for the Uplat (theuplat.com) environment. It is modeled to be able to perform exploration missions in the Martian environment, conduct drilling works, and move in the harsh terrain of the environment. A possible Mars exploration scenario was created by means of Eva-Mars and robotics training packages were revealed with this scenario.

![Image of EvaMars](https://github.com/inomuh/eva_mars/blob/main/images/eva_mars.png)

- eva_mars_description: It is the sub-package containing urdf and mesh files of the EvaMars.
- eva_mars_simulation: It is a sub-package containing the package and launch files required for the simulation of the EvaMars.
- eva_mars_control: It is a sub-package containing the EvaMars drill and camera port controller's launch and config files.

UPlat EvaMars Training Missions
-------------------------------
EvaMars Robot is a Mars mission training robot developed by Inovasyon Mühendislik for UPlat virtual laboratory. A robotic simulation was created with a Gazebo environment built from a real Mars map, along with a training package of seven different Mars missions. With the training to be carried out in this simulation environment, users are expected to complete this training by performing Mars exploration missions with various participation ways. In line with this training that UPlat will provide us, a robotics training has emerged that can be completed by users with intermediate ROS and Python knowledge. 

![Image of EvaMars Mission Diagram](https://github.com/inomuh/eva_mars/blob/noetic-devel/images/eva_mars_missions.png)

This Github repository contains only the robot model and basic ROS packages. For experiments, the Martian environment and more:

    UPlat Virtual Laboratory: https://www.theuplat.com/home

![Image of EvaMars Mission IV](https://github.com/inomuh/eva_mars/blob/noetic-devel/images/evamars_uplat_mars_rockylake_1.png)


Launch Commands
---------------

Gazebo Launching:

    $ roslaunch eva_mars_simulation eva_mars_emptyworld.launch

Solo-Rviz Launching:

    $ roslaunch eva_mars_simulation eva_mars_rviz_standalone.launch
    
Rviz (with Gazebo) Launching:

    $ roslaunch eva_mars_simulation eva_mars_rviz.launch
    
Drill and Camera Port Controller Launching (Activate):

    $ roslaunch eva_mars_control eva_mars_control.launch

Drill and Camera Port Control Script Running:
    
    $ rosrun eva_mars_control sondaj_control.py
   
------------------------------------------------------------------------------
Requirements:
-------------
- In order for the "joint_state_publisher" to work, "joint_state_publisher_gui" package must be downloaded to your computer.

        $ sudo apt update
        $ sudo apt install ros-noetic-joint-state-publisher-gui
        
- In order for the "joint_state_controller" to work, "joint_state_controller_gui" package must be downloaded to your computer.

        $ sudo apt install ros-noetic-ros-controllers
 
- In order for the robot's differential drive plugin to work, "hector_gazebo" package must be downloaded to your workspace.
        
        $ cd ~/catkin_ws/src
        $ git clone https://github.com/tu-darmstadt-ros-pkg/hector_gazebo -b melodic-devel

NOTE: If the "catkin_make" operation fails after installing hector_gazebo, the problem can be solved by deleting the faulty hector_gazebo plugin parts from CMakeList. This will fix the noetic incompatibility.

- In order for the "laserscan" to work, "pointcloud_to_laserscan" package must be downloaded to your workspace.

        $ cd ~/catkin_ws/src
        $ git clone https://github.com/ros-perception/pointcloud_to_laserscan
        
- In order for the "sondaj_control.py" file (for controlling drill and camera port script) in "eva_mars_control/scripts" to work, the following commands should be run.

        $ cd ~/catkin_ws/src/eva_mars/eva_mars_control/scripts
        $ chmod +x sondaj_control.py

![Image of EvaMars Mission V](https://github.com/inomuh/eva_mars/blob/noetic-devel/images/mission5_3_1.png)

-------------------------------------------------------------------------------
Changelog:
----------
Update v1.0 - 01.12.20
----------------------
- First version
