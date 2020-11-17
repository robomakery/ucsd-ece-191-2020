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
        wget  \
        && rm -rf /var/lib/apt/lists/*

RUN wget http://packages.osrfoundation.org/gazebo.key
RUN apt-key add gazebo.key
RUN apt-get update && apt-get install -y \
        ros-melodic-desktop-full   \
        ros-melodic-gazebo-plugins \
        python3-pip                \
        python3-apt                \
        python3-vcstool            \
        && rm -rf /var/lib/apt/lists/*

# SHELL ["/bin/bash", "-c"]

# # build custom ROS packages
# WORKDIR /catkin_ws
# RUN source /opt/ros/melodic/setup.bash && catkin_make

# initialize ROS (master uri, environments, etc.)
# COPY docker-entrypoint.sh /
# ENTRYPOINT ["/docker-entrypoint.sh"]

# # default command
# CMD ["bash"]
