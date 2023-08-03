import os
import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # Set the path to your URDF file
    pkg_path = os.path.join(get_package_share_directory('scout_description'))
    urdf_file_path = os.path.join(pkg_path,'urdf/caytu/caytu_base.xacro')

    # Declare the Gazebo launch node to spawn the URDF model
    spawn_entity = launch_ros.actions.Node(
        package='gazebo_ros', executable='spawn_entity_demo.py',
        arguments=['-entity', 'my_robot', '-x', '0.0', '-y', '0.0', '-z', '0.5', '-file', urdf_file_path],
        output='screen'
    )

    return launch.LaunchDescription([spawn_entity])


if __name__ == '__main__':
    generate_launch_description()