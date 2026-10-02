from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    ur_type = LaunchConfiguration("ur_type")
    gazebo_gui = LaunchConfiguration("gazebo_gui")
    launch_rviz = LaunchConfiguration("launch_rviz")

    controllers_file = PathJoinSubstitution(
        [
            FindPackageShare("robot_control_lab_ur"),
            "config",
            "ur_controllers_effort.yaml",
        ]
    )

    ur_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [
                    FindPackageShare("ur_simulation_gz"),
                    "launch",
                    "ur_sim_control.launch.py",
                ]
            )
        ),
        launch_arguments={
            "ur_type": ur_type,
            "controllers_file": controllers_file,
            "initial_joint_controller": "forward_effort_controller",
            "activate_joint_controller": "true",
            "launch_rviz": launch_rviz,
            "gazebo_gui": gazebo_gui,
        }.items(),
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "ur_type",
                default_value="ur5e",
                choices=["ur3e", "ur5e"],
                description="UR robot model used by the Robot Control Lab",
            ),
            DeclareLaunchArgument(
                "gazebo_gui",
                default_value="true",
                description="Start Gazebo GUI",
            ),
            DeclareLaunchArgument(
                "launch_rviz",
                default_value="false",
                description="Start RViz",
            ),
            ur_launch,
        ]
    )
