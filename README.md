# InterIIT-2021
Contains the code and implementation instructions for DRDO Event, Drone Problem Statement 

Clone the repo or the file **start_drone.py**. 

In a terminal, run:
 ```
 $ cd ~/catkin_ws/src/interiit21/
 $ mkdir scripts
 ```
Place start_drone.py in the scripts directory.
 
To launch the interiit world, run:
 ```
 $ cd ~/catkin_ws/src/interiit21/
 $ ./start_sim.sh 
 ```
Make sure that the file is made executable.
In a new terminal:
 ```
 $ cd ~/catkin_ws/src/interiit21/scripts
 $ chmod +x start_drone.py
 $ rosrun interiit21 start_drone.py
 ```
The altitude can be changed from within the file.
