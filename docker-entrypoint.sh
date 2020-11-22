#!/bin/bash

set -e

# setup ros environment
source "/opt/ros/melodic/setup.bash"
source "/code/robot_ws/devel/setup.bash"
exec "$@"

