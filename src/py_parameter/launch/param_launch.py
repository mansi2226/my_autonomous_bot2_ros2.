from launch import LaunchDescription
from launch_ros.actions import Node




def generate_launch_description():
    return LaunchDescription([

      Node(
          package='py_parameter',
          executable='minimal_parameter_node',  ##constuctor name given
          name ='custom_minimal_param',
          output ='screen',
          emulate_tty=True,
          parameters=[{'my_parameter':'earth'}]
      )


    ])