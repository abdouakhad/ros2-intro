import rclpy
from rclpy.node import Node
import time

class MyNode(Node):
    def __init__(self):
        super().__init__('my_node')
        self.timer = self.create_timer(1.0, self.timer_callback)  # Create a timer that runs every 1 second

    def timer_callback(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.get_logger().info(f"Current time: {current_time}")


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
