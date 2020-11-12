#!/usr/bin/env bash

echo "$(date): Starting setup-env.sh"

# system upgrades and tools
export DEBIAN_FRONTEND=noninteractive
apt-get -y -q update && apt-get -y -q upgrade
apt-get -y -q install \
        curl  \
        tree  \
        git   \
        gnupg \
        groff \
        jq    \
        less  \
        unzip \
        vim   \
        wget

# tzdata
echo "tzdata tzdata/Areas select America" > /root/tzdata-preseed.txt
echo "tzdata tzdata/Zones/America select Los_Angeles" >> /root/tzdata-preseed.txt
debconf-set-selections /root/tzdata-preseed.txt
apt-get install -y tzdata

# ROS Melodic
cd ~
echo "deb http://packages.ros.org/ros/ubuntu bionic main" > /etc/apt/sources.list.d/ros-melodic.list
apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
wget http://packages.osrfoundation.org/gazebo.key
apt-key add gazebo.key
apt-get update
apt-get -y install \
        ros-melodic-ros-base \
        ros-melodic-gazebo-plugins \
        ros-melodic-joint-state-publisher \
        ros-melodic-interactive-markers \
        ros-melodic-robot-state-publisher \
        python3-pip \
        python3-apt \
        python3-vcstool

echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc

# build dependencies
apt-get install -y python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
rosdep init
rosdep update

# colcon
apt-get install -y python3-colcon-common-extensions
pip3 install -U setuptools
pip3 install colcon-ros-bundle
