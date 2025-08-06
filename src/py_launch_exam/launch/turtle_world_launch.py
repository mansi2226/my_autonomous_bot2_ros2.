import os 
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    config =os.path.join(get_package_share_directory('py_launch_exam'),'config','turtlesim.yaml')

    return LaunchDescription([
          Node (
              package='turtlesim',
              name='sim',
              executable='turtlesim_node',
              parameters=[config]

          )

    ])