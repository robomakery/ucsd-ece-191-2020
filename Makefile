GUI_OPTIONS=--env=DISPLAY --env=QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix
GENERAL_OPTIONS=-it --rm --privileged --net=host

bash: build
	xhost +local:docker
	docker run $(GENERAL_OPTIONS) $(GUI_OPTIONS) devenv:latest bash

build:
	docker build -t devenv:latest .

roscore: build
	docker run $(GENERAL_OPTIONS) devenv:latest bash -c "source /opt/ros/melodic/setup.bash && roscore"

gazebo: build
	xhost +local:docker
	docker run $(GENERAL_OPTIONS) $(GUI_OPTIONS) devenv:latest bash -c "source /opt/ros/melodic/setup.bash && gazebo"

rviz: build
	xhost +local:docker
	docker run $(GENERAL_OPTIONS) $(GUI_OPTIONS) devenv:latest bash -c "source /opt/ros/melodic/setup.bash && rviz"
