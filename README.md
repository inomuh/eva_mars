# EvaMars Robot 
The EvaMars robot is a Mars reconnaissance robot model developed for the Uplat (theuplat.com) environment. It is modeled to be able to perform exploration missions in the Martian environment, conduct drilling works, and move in the harsh terrain of the environment. A possible Mars exploration scenario was created by means of Eva-Mars and robotics training packages were revealed with this scenario.

![Image of EvaMars](https://github.com/inomuh/eva_mars/blob/main/eva_mars.png)

- eva_mars_description: It is the sub-package containing urdf and mesh files of the EvaMars.
- eva_mars_simulation: It is a sub-package containing the package and launch files required for the simulation of the EvaMars.
- eva_mars_control: It is a sub-package containing the EvaMars drill and camera port controller's launch and config files.

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
 
- In order for the robot's differential drive plugin to work, "hector_gazebo" package must be downloaded to your computer.
        
        $ cd ~/catkin_ws/src
        $ git clone https://github.com/tu-darmstadt-ros-pkg/hector_gazebo -b melodic-devel

NOTE: If the "catkin_make" operation fails after installing hector_gazebo, the problem can be solved by deleting the faulty hector_gazebo plugin parts from CMakeList. This will fix the noetic incompatibility.

- In order for the "laserscan" to work, "pointcloud_to_laserscan" package must be downloaded to your computer.

        $ cd ~/catkin_ws/src
        $ git clone https://github.com/ros-perception/pointcloud_to_laserscan
        
- In order for the "sondaj_control.py" file (for controlling drill and camera port script) in "eva_mars_control/scripts" to work, the following commands should be run.

        $ cd ~/catkin_ws/src/eva_mars/eva_mars_control/scripts
        $ chmod +x sondaj_control.py

-------------------------------------------------------------------------------
Changelog:
----------
Update v1.0 - 26.11.20
----------------------
- First version
