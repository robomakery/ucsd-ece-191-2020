# ucsd-ece-191-2020

UCSD ECE 191 Fall 2020

## AWS Workspace Setup

After connecting to a new AWS Workspace, open a terminal and run the following commands to get started:

    $ sudo yum install -y docker
    $ sudo usermod -aG docker ${USER}
    $ sudo service docker start
    $ su ${USER}
    $ git clone https://github.com/robomakery/ucsd-ece-191-2020.git
    $ cd ucsd-ece-191-2020/
    $ make rviz

At this point, after the image builds, you should see the PVC Chair in rviz.
