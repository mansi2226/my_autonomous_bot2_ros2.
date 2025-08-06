
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node 
from launch.substitutions import Command, FindExecutable
from launch.actions import ExecuteProcess, IncludeLaunchDescription, DeclareLaunchArgument
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration

def generate_launch_description():

    urdf_path= os.path.join(get_package_share_directory('mici_description'),'model','model.sdf')

    gazebo_launch= IncludeLaunchDescription(
        PythonLaunchDescriptionSource([

            PathJoinSubstitution([FindPackageShare('gazebo_ros'),'launch','gazebo.launch.py'])
        ]), 
        launch_arguments={
            'world':PathJoinSubstitution([
                FindPackageShare('mici_description'),'world','mici.world'
            ]),'use_sim_time':'true'
        }.items(),
    )
    robot_description = Command([
    PathJoinSubstitution([
        FindExecutable(name='xacro')
    ]),
    ' ',
    PathJoinSubstitution([
        FindPackageShare('mici_description'), 'urdf', 'mici.urdf.xacro'
    ])
])



    robot_state_publisher_node= Node(

        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description}],
        output='screen',
    )
    tf2_node =Node(
    package='tf2_ros',
    executable='static_transform_publisher',
    name='basefootprint_to_baselink',
    arguments=['0', '0', '0', '0', '0', '0', 'base_footprint', 'base_link']
)


    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        
        output='screen',
     )
    
  

    
    start_gazebo_ros_spawner_cmd = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', 'robot',
            '-file', urdf_path,
            
        ],
        output='screen',
    )


    return LaunchDescription([
        gazebo_launch,
        robot_state_publisher_node,
        joint_state_publisher_node ,
        tf2_node,
       
        start_gazebo_ros_spawner_cmd ,

    ])