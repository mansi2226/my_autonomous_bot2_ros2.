from launch_ros.actions import Node 
import os
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace


def generate_launch_description():
    turtlesim_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('py_launch_exam'),
                'launch',
                'turtle_world_launch.py'
            )
        ])
    )

    mimic_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('py_launch_exam'),
                'launch',
                'mimic_launch.py'
            )
        ])
    )

    broadcaster_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('py_launch_exam'),
                'launch',
                'broadcaster_launch.py'
            )
        ])
    )

    rviz = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('py_launch_exam'),
                'launch',
                'rviz_launch.py'  # ← is this correct? (maybe should be rviz_launch.py?)
            )
        ])
    )

    return LaunchDescription([
        turtlesim_world,
        mimic_launch,
        broadcaster_launch,
        rviz,
    ])
