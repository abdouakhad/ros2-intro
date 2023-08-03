import os
import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    # Process the URDF file
    pkg_path = os.path.join(get_package_share_directory('scout_description'))
    urdf_file_path = os.path.join(pkg_path, 'urdf/caytu/caytu_base.xacro')

    # Launch Gazebo
    gazebo_launch = launch.actions.ExecuteProcess(
        cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
        output='screen'
    )


    # Declare the Gazebo spawn_entity node to spawn the URDF model
    spawn_gazebo_entity = launch_ros.actions.Node(
        package='gazebo_ros', executable='spawn_entity.py',
        arguments=['-entity', 'my_robot', '-x', '0.0', '-y', '0.0', '-z', '0.5', '-file', urdf_file_path],
        output='screen'
    )
    
     # Wait for Gazebo to start before spawning the model
    gazebo_ready = launch.actions.TimerAction(
        period=2.0,
        actions=[spawn_gazebo_entity]
    )

    return launch.LaunchDescription([gazebo_launch, gazebo_ready])


if __name__ == '__main__':
    generate_launch_description()
