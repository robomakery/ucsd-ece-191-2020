bash: build
	docker run -it --rm --privileged --net=host --env=DISPLAY --env=QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix devenv:latest bash

build:
	docker build -t devenv:latest .

roscore: build
	docker run -it --rm --privileged --net=host devenv:latest bash -c "source /opt/ros/melodic/setup.bash && roscore"

gazebo: build
	docker run -it --rm --privileged --net=host --env=DISPLAY --env=QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix devenv:latest bash -c "source /opt/ros/melodic/setup.bash && gazebo"

rviz: build
	docker run -it --rm --privileged --net=host --env=DISPLAY --env=QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix devenv:latest bash -c "source /opt/ros/melodic/setup.bash && rviz"
