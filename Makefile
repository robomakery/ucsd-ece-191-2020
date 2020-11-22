GUI_OPTIONS=--env=DISPLAY --env=QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix
GENERAL_OPTIONS=-it --rm --privileged --net=host -v $(PWD):/code

bash: build
	xhost +local:docker
	docker run $(GENERAL_OPTIONS) $(GUI_OPTIONS) devenv:latest bash

build:
	docker build -t devenv:latest .

roscore: build
	docker run $(GENERAL_OPTIONS) devenv:latest bash -c "source /opt/ros/melodic/setup.bash && roscore"

empty_rviz: build
	xhost +local:docker
	docker run $(GENERAL_OPTIONS) $(GUI_OPTIONS) devenv:latest bash -c "source /opt/ros/melodic/setup.bash && rviz"

empty_gazebo: build
	xhost +local:docker
	docker run $(GENERAL_OPTIONS) $(GUI_OPTIONS) devenv:latest bash -c "source /opt/ros/melodic/setup.bash && gazebo"

gazebo: build
	xhost +local:docker
	docker run $(GENERAL_OPTIONS) $(GUI_OPTIONS) devenv:latest bash -c "cd /code/robot_ws && source /opt/ros/melodic/setup.bash && source /code/robot_ws/devel/setup.bash && catkin_make && roslaunch pvcchair_description gazebo.launch"

rviz: build
	xhost +local:docker
	docker run $(GENERAL_OPTIONS) $(GUI_OPTIONS) devenv:latest bash -c "cd /code/robot_ws && source /opt/ros/melodic/setup.bash && source /code/robot_ws/devel/setup.bash && catkin_make && roslaunch pvcchair_description visualize_urdf.launch"
