GUI_OPTIONS=--env=DISPLAY --env=QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix
GENERAL_OPTIONS=-it --rm --privileged --net=host --volume $(PWD):/code

bash: build
	xhost +local:docker
	docker run $(GENERAL_OPTIONS) $(GUI_OPTIONS) devenv:latest bash

build:
	docker build --network=host -t devenv:latest .

empty_gazebo: build
	xhost +local:docker
	docker run $(GENERAL_OPTIONS) $(GUI_OPTIONS) devenv:latest bash -c "source /opt/ros/melodic/setup.bash && gazebo"

empty_roscore: build
	docker run $(GENERAL_OPTIONS) devenv:latest bash -c "source /opt/ros/melodic/setup.bash && roscore"

empty_rviz: build
	xhost +local:docker
	docker run $(GENERAL_OPTIONS) $(GUI_OPTIONS) devenv:latest bash -c "source /opt/ros/melodic/setup.bash && rviz"

gazebo: build
	xhost +local:docker
	docker run $(GENERAL_OPTIONS) $(GUI_OPTIONS) devenv:latest bash -c "cd /code/robot_ws && source /opt/ros/melodic/setup.bash && catkin_make && source /code/robot_ws/devel/setup.bash && roslaunch pvcchair_description gazebo.launch"

setup: build
	xhost +local:docker
	docker run $(GENERAL_OPTIONS) $(GUI_OPTIONS) devenv:latest bash -w /code/robot_ws && source /opt/ros/melodic/setup.bash && source /code/robot_ws/devel/setup.bash

roscore: build
	docker run $(GENERAL_OPTIONS) devenv:latest bash -c "cd /code/robot_ws && source /opt/ros/melodic/setup.bash && catkin_make && source /code/robot_ws/devel/setup.bash && roscore"

rviz: build
	xhost +local:docker
	docker run $(GENERAL_OPTIONS) $(GUI_OPTIONS) devenv:latest bash -c "cd /code/robot_ws && source /opt/ros/melodic/setup.bash && catkin_make && source /code/robot_ws/devel/setup.bash && roslaunch pvcchair_description visualize_urdf.launch"
