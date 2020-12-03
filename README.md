# ucsd-ece-191-2020

UCSD ECE 191 Fall 2020

## AWS Workspace Setup

After connecting to a new AWS Workspace, open a terminal and run the following commands to get started:

    sudo yum install -y docker
    sudo usermod -aG docker ${USER}
    sudo systemctl enable docker
    sudo systemctl start docker
    su ${USER}
    make bash # Put you into Docker Container
    git clone https://github.com/robomakery/ucsd-ece-191-2020.git #If already have it and just updating use the command: git pull
    cd ucsd-ece-191-2020/
    make rviz

At this point, after the image builds, you should see the PVC Chair in rviz.
