FROM ros:melodic

RUN apt-get update && apt-get install -q -y \
        curl  \
        git   \
        gnupg \
        groff \
        jq    \
        less  \
        tree  \
        unzip \
        vim   \
        nano  \
        gedit \
        wget  \
        && rm -rf /var/lib/apt/lists/*

RUN wget http://packages.osrfoundation.org/gazebo.key
RUN apt-key add gazebo.key
RUN apt-get update && apt-get install -y      \
        ros-melodic-desktop-full              \
        ros-melodic-joint-state-publisher-gui \
        ros-melodic-gazebo-plugins            \
        python3-pip                           \
        python3-apt                           \
        python3-vcstool                       \
        python3-colcon-common-extensions      \
        && rm -rf /var/lib/apt/lists/*
RUN rosdep update

# colcon
RUN pip3 install -U setuptools
RUN pip3 install colcon-ros-bundle

# pygame
RUN pip3 install pygame

WORKDIR /code/robot_ws
RUN /bin/bash -c "source /opt/ros/melodic/setup.bash && source /code/robot_ws/devel/setup.bash"
# SHELL ["/bin/bash", "-c"]
# RUN cd robot_ws && source /opt/ros/melodic/setup.bash && catkin_make

# # build custom ROS packages
# WORKDIR /catkin_ws

# initialize ROS (master uri, environments, etc.)
COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]

# # default command
# CMD ["bash"]
