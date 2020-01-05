# 3D PRM, RRT and Wavefront path finding algorithms on Python.
**Content of the folder:**

There are three Python programs in the folder. Wavefront algorithm of finding path
(wavefront.py), PRM algorithm (prm.py) and RRT algorithm (rrt.py)


**Dependencies:**

All programs require Numpy dependence. PRM and RRT uses math and random
modules on top. Both programs are tested using Python3

**Input format:**

All programs use given world.txt as input for space and obstacles position. 

Bounds _x_ direction

Bounds _y_ direction

Bounds _z_ direction

Cube_Center_x Cube_Center_y Cube_Center_z side_size

Cube_Center_x Cube_Center_y Cube_Center_z side_size

Sphere_Center_x Sphere_Center_y Sphere_Center_z radius

Sphere_Center_x Sphere_Center_y Sphere_Center_z radius

Start_Point

End_Point

**To start:**
Just simply run desired program from the folder like any other python
program:

python3 wavefront.py // The run should not take more than 30 seconds
python3 prm.py // The run should not take more than 1 minute
python3 rrt.py //The run should not take more than 30 seconds

**Settings:**

PRM and RRT has unique settings that you can change in the top of the code for a
better result.

**Visualization:**

You can visualize the path through Blender project file that is also in the folder.
For that you might need to change directory variable to yours inside project script
code.
